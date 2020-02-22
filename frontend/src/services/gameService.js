// we'll omit error handling and complex stuff for simplicity
const EventEmitter = {
  events: {}, // dictionary with our events
  on(event, listener) {
    // add event listeners
    if (!this.events[event]) {
      this.events[event] = { listeners: [] };
    }
    this.events[event].listeners.push(listener);
  },
  off(event) {
    // remove listeners
    delete this.events[event];
  },
  emit(name, ...payload) {
    // trigger events
    for (const listener of this.events[name].listeners) {
      listener.apply(this, payload);
    }
  }
};

class GameService {
  static instance = null;
  //callbacks = {};

  static getInstance() {
    if (!GameService.instance) {
      GameService.instance = new GameService();
    }
    return GameService.instance;
  }

  constructor() {
    this.socketRef = null;
  }

  connect(roomName, base_path) {
    const path = base_path + roomName + "/";
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
      this.connect(roomName, base_path);
    };
  }

  socketNewMessage(data) {
    const parsedData = JSON.parse(data);
    const command = parsedData.command;
    const action = parsedData.action;

    EventEmitter.emit(command, action);
  }

  addCallback(callback_lookup_key, playerValueCallback) {
    EventEmitter.on("player_status_update_response", playerValueCallback);
  }

  addGameListResponseCallback(gameListResponseCallback) {
    EventEmitter.on("game_list_response", gameListResponseCallback);
  }

  addServerResponseCallback(serverResponseCallback) {
    EventEmitter.on("server_response", serverResponseCallback);
  }

  addDiceCallback(diceRollCallback) {
    EventEmitter.on("dice_rolls_response", diceRollCallback);
  }

  addBeginTurnCallback(beginTurnCallback) {
    EventEmitter.on("begin_turn_response", beginTurnCallback);
  }

  addCardCallback(cardStoreCallback) {
    EventEmitter.on("card_store_response", cardStoreCallback);
  }

  sendMessage(data) {
    try {
      const msg = JSON.stringify({ ...data });
      this.socketRef.send(msg);
      return msg;
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
    setTimeout(function () {
      if (socket.readyState === 1) {
        console.log("Gameroom connection is made");
        if (callback != null) {
          callback();
        }
        return;
      } else {
        console.log("wait for gameroom connection...");
        recursion(callback);
      }
    }, 1); // wait 5 milisecond for the connection...
  }
}

const GameInstance = GameService.getInstance();

export default GameInstance;
