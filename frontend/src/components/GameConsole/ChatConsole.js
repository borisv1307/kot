import React from 'react';
import "./ChatConsole.css";
import Button from "react-bootstrap/Button";

// import GameLog from './GameLog'

import ChatInstance from './../../services/chatService'


const chatLogExample = [
  '-- Sammy turn –',
  'Rolled: E E H 1 2 3',
  'Decision: keep E E',
  'Rolled: E P 1 2 2',
  'Decision: keep E',
  'Rolled: 2 2 2 (TRIPPLE! +2 VP)',
  ':: Gain: E E E +2 VP ::',
  'Buy: Psychic Probe',
  'End Turn'
];

class ChatConsole extends React.Component {

  constructor(props) {
    super(props);

    ChatInstance.connect();

    this.waitForSocketConnection(() => {
      ChatInstance.initChatUser(this.props.currentUser);
      ChatInstance.addCallbacks(this.setMessages.bind(this), this.addMessage.bind(this))
      ChatInstance.fetchMessages(this.props.currentUser);
    });

    this.state = {
      username: props.username,
      gameRoom: props.gameRoom,
      loggedIn: true,
      log: chatLogExample, // this holds the name of each list
      cmd: "enter cmd"
    };

    // this.handleChange = this.handleChange.bind(this);
    // this.SubmitGameCommand = this.SubmitGameCommand.bind(this);
  }

  // SubmitGameCommand(e) {
  //   let data = this.state.log;
  //   data.push(this.state.cmd);

  //   // TO DO : Call dice REST endpoint requesting reroll.
  //   //this.props.sendMessage(this.state.message)

  //   this.setState({
  //     log: data
  //   })
  // }

  // handleChange(e) {
  //   this.setState({
  //     cmd: e.target.value
  //   })
  // }


  waitForSocketConnection(callback) {
    const component = this;
    setTimeout(
      function () {
        // Check if websocket state is OPEN
        if (ChatInstance.state() === 1) {
          console.log("Connection is made")
          callback();
          return;
        } else {
          console.log("wait for connection...")
          component.waitForSocketConnection(callback);
        }
      }, 100); // wait 100 milisecond for the connection...
  }

  componentDidMount() {
    this.scrollToBottom();
  }

  componentDidUpdate() {
    this.scrollToBottom();
  }

  scrollToBottom = () => {
    const chat = this.messagesEnd;
    const scrollHeight = chat.scrollHeight;
    const height = chat.clientHeight;
    const maxScrollTop = scrollHeight - height;
    chat.scrollTop = maxScrollTop > 0 ? maxScrollTop : 0;
  }

  addMessage(message) {
    this.setState({ messages: [...this.state.messages, message] });
  }

  setMessages(messages) {
    this.setState({ messages: messages.reverse() });
  }

  messageChangeHandler = (event) => {
    this.setState({
      message: event.target.value
    })
  }

  sendMessageHandler = (e, message) => {
    const messageObject = {
      from: this.props.currentUser,
      text: message
    };
    ChatInstance.newChatMessage(messageObject);
    this.setState({
      message: ''
    })
    e.preventDefault();
  }

  renderMessages = (messages) => {
    const currentUser = this.props.currentUser;
    return messages.map((message, i) => <li key={message.id} className={message.author === currentUser ? 'me' : 'him'}> <h4 className='author'>{message.author} </h4><p>{message.content}</p></li>);
  }

  render() {
    const messages = this.state.messages;
    const currentUser = this.props.currentUser;
    return (
      <div className='chat'>
        <div className='container'>
          <h1>Chatting as {currentUser} </h1>
          <h3>Displaying only the last 50 messages</h3>
          <ul ref={(el) => { this.messagesEnd = el; }}>
            {
              messages &&
              this.renderMessages(messages)
            }
          </ul>
        </div>
        <div className='container message-form'>
          <form onSubmit={(e) => this.sendMessageHandler(e, this.state.message)} className='form'>
            <input
              type='text'
              onChange={this.messageChangeHandler}
              value={this.state.message}
              placeholder='Type a Message'
              required />
            <Button variant="btn btn-secondary" className='submit' type='submit' value='Submit'>
              Send
            </Button>
          </form>
        </div>
      </div>
    );
  }

  // render() {
  //   return (
  //     <div className="chat_console">
  //       <GameLog data={this.state.log} />

  //       <form className="submit_game_command"
  //         onSubmit={this.SubmitGameCommand}
  //         onChange={this.handleChange}>
  //         <textarea value={this.state.value} onChange={this.handleChange}>Type Command [enter]</textarea>
  //       </form>
  //       <button onClick={this.SubmitGameCommand}>
  //         Submit Comand
  //         </button>
  //     </div>
  //   )
  // }
}

export default ChatConsole;