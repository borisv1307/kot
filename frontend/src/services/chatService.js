import config from './config';

class ChatService {
    static instance = null;
    callbacks = {};

    static getInstance() {
        if (!ChatService.instance) {
            ChatService.instance = new ChatService();
        }
        return ChatService.instance;
    }

    constructor() {
        this.socketRef = null;
    }

    connect(room) {
        // const path = config.CHAT_SOCKET_API_PATH;
        const path = 'ws://localhost:8000/ws/chat';
        this.socketRef = new WebSocket(path);
        this.socketRef.onopen = () => {
            console.log('WebSocket open');
        };
        this.socketRef.onmessage = e => {
            this.socketNewMessage(e.data);
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

    initChatUser(username) {
        this.sendMessage({ command: 'init_chat', username: username });
    }

    fetchMessages(username) {
        this.sendMessage({ command: 'fetch_messages', username: username });
    }

    newChatMessage(message) {
        this.sendMessage({ command: 'new_message', from: message.from, text: message.text });
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

const ChatInstance = ChatService.getInstance();

export default ChatInstance;