import config from "./config";

class GameService {
  static instance = null;
  callbacks = {};

  static getInstance() {
    if (!GameService.instance) {
      GameService.instance = new GameService();
    }
    return GameService.instance;
  }

  constructor() {
    this.socketRef = null;
  }

  // sends dice back to server formatted as an array of 2d arrays.
  // first index: the roll value
  // second index: selected or not
  // payload format: [['e', True], ['1', False], ['h', True], ['2', False], ['3', True], ['e', False]]
  sendSelectedDice(envelope) {
    this.sendMessage({
      command: "selected_dice_request",
      from: envelope.from,
      room: envelope.room,
      payload: envelope.data
    });
  }

  // payload format: [['text entered by user']
  sendGameLogCommand(envelope) {
    this.sendMessage({
      command: "gamelog_send_request",
      from: envelope.from,
      room: envelope.room,
      payload: envelope.data
    });
  }

  initUser(envelope) {
    this.sendMessage({
      command: "init_chat_request",
      from: envelope.from,
      room: envelope.room,
      payload: envelope.data
    });
  }

  // Format: [['COMMAND_TOKEN', 'COMMAND_OPTION', 'COMMAND_OPTIONS']]
  // payload example: [['cmd', 'init_player'], #]
  // payload example: [['cmd', 'refresh_player'], #]
  // payload example: [['cmd', 'store_replace_card', #]] where # indicates number of cards to return from deck
  // payload example: [['cmd', 'store_buy_card', #]] where # indicates cards id to purchase
  // payload example: [['cmd', 'chat_send'], #]

  connect(roomName) {
    // this.socketRef = new WebSocket(
    //     'ws://' + 'localhost:8000' +
    //     '/ws/lobby/' + roomName + '/');

    const path = config.GAME_SOCKET_API_PATH + roomName + "/";
    this.socketRef = new WebSocket(path);

    this.socketRef.onopen = () => {
      console.log("WebSocket open");
    };

    this.socketRef.onmessage = e => {
      let data = e.data;
      this.socketNewMessage(data);
      console.log(data);
    };

    this.socketRef.onerror = e => {
      console.log(e.message);
    };

    this.socketRef.onclose = e => {
      console.log("WebSocket closed let's reopen");
      this.connect(roomName);
    };
  }

  socketNewMessage(data) {
    const parsedData = JSON.parse(data);
    const command = parsedData.command;
    if (Object.keys(this.callbacks).length === 0) {
      return;
    }

    if (command === "server_response") {
      this.callbacks[command](parsedData.message);
    }
    // else if (command === "messages") {
    //   this.callbacks[command](parsedData.messages);
    // } else if (command === "new_message") {
    //   this.callbacks[command](parsedData.message);
    // }
  }

  addCallbacks(serverResponseCallback) {
    this.callbacks["server_response"] = serverResponseCallback;
    // this.callbacks["messages"] = messagesCallback;
    // this.callbacks["new_message"] = newMessageCallback;
  }

  sendMessage(data) {
    try {
      this.socketRef.send(JSON.stringify({ ...data }));
    } catch (err) {
      console.log(err.message);
    }
  }

  state() {
    return this.socketRef.readyState;
  }

  waitForSocketConnection(callback) {
    const socket = this.socketRef;
    const recursion = this.waitForSocketConnection;
    setTimeout(function() {
      if (socket.readyState === 1) {
        console.log("Connection is made");
        if (callback != null) {
          callback();
        }
        return;
      } else {
        console.log("wait for connection...");
        recursion(callback);
      }
    }, 1); // wait 5 milisecond for the connection...
  }
}

const GameInstance = GameService.getInstance();

export default GameInstance;
