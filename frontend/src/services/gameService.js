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

  connect(roomName) {
    const path = config.GAME_SOCKET_API_PATH + roomName + "/";
    this.socketRef = new WebSocket(path);

    this.socketRef.onopen = () => {
      console.log("WebSocket open");
    };

    this.socketRef.onmessage = e => {
      let data = e.data;
      this.socketNewMessage(data);
      console.log("Socket OnMessage: " + data);
    };

    this.socketRef.onerror = e => {
      console.log("Socket OnError: " + e.message);
    };

    this.socketRef.onclose = e => {
      console.log("Socket OnClosed, Reopening...");
      this.connect(roomName);
    };
  }

  socketNewMessage(data) {
    const parsedData = JSON.parse(data);
    const command = parsedData.command;
    const action = parsedData.action;
    if (Object.keys(this.callbacks).length === 0) {
      return;
    }

    this.callbacks[command](action);
  }

  addCallbacks(serverResponseCallback) {
    this.callbacks["server_response"] = serverResponseCallback;
  }

  addDiceCallback(diceRollCallback) {
    this.callbacks["dice_rolls_response"] = diceRollCallback;
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
