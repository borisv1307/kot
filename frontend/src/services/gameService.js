import config from './config';

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
    // [['e', True], ['1', False], ['h', True], ['2', False], ['3', True], ['e', False]]
    sendSelectedDice(envelope) {
        this.sendMessage({ command: 'selected_dice', from: envelope.from, message: envelope.data });
    }

    connect(roomName) {
        // this.socketRef = new WebSocket(
        //     'ws://' + 'localhost:8000' +
        //     '/ws/lobby/' + roomName + '/');

        const path = config.GAME_SOCKET_API_PATH + roomName + '/';
        this.socketRef = new WebSocket(path);


        this.socketRef.onopen = () => {
            console.log('WebSocket open');
        };

        this.socketRef.onmessage = e => {
            let data = e.data;
            this.socketNewMessage(data);
            console.log(data);
        };

        this.socketRef.onerror = e => {
            console.log(e.message);
        };

        this.socketRef.onclose = (e) => {
            console.log("WebSocket closed let's reopen");
            this.connect();
        };
    }

    socketNewMessage(data) {
        const parsedData = JSON.parse(data);
        const command = parsedData.command;
        if (Object.keys(this.callbacks).length === 0) {
            return;
        }
        if (command === 'messages') {
            this.callbacks[command](parsedData.messages);
        }
        if (command === 'new_message') {
            this.callbacks[command](parsedData.message);
        }
    }

    addCallbacks(messagesCallback, newMessageCallback) {
        this.callbacks['messages'] = messagesCallback;
        this.callbacks['new_message'] = newMessageCallback;
    }

    sendMessage(data) {
        try {
            this.socketRef.send(JSON.stringify({ ...data }));
        }
        catch (err) {
            console.log(err.message);
        }
    }

    state() {
        return this.socketRef.readyState;
    }

    waitForSocketConnection(callback) {
        const socket = this.socketRef;
        const recursion = this.waitForSocketConnection;
        setTimeout(
            function () {
                if (socket.readyState === 1) {
                    console.log("Connection is made")
                    if (callback != null) {
                        callback();
                    }
                    return;

                } else {
                    console.log("wait for connection...")
                    recursion(callback);
                }
            }, 1); // wait 5 milisecond for the connection...
    }

}

const GameInstance = GameService.getInstance();

export default GameInstance;