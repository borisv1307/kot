import React from "react";
import "./GameConsole";

class GameLog extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      username: props.currentUser,
      gameRoom: props.currentRoom,
      log: props.data
    };
  }

  componentDidMount() {
    this.scrollToBottom();
  }

  componentDidUpdate() {
    this.scrollToBottom();
  }

  scrollToBottom() {
    const chat = this.messagesEnd;

    if (chat) {
      const scrollHeight = chat.scrollHeight;
      const height = chat.clientHeight;
      const maxScrollTop = scrollHeight - height;
      chat.scrollTop = maxScrollTop > 0 ? maxScrollTop : 0;
    }
  }

  renderMessages(messages) {
    if (messages && messages.length > 0) {
      const currentUser = this.state.username;
      return messages.map((message, i) => (
        <li key={i} className={message.user === currentUser ? "me" : "him"}>
          <p>{message}</p>
        </li>
      ));
    }
  }

  render() {
    const game_messages = this.props.data;
    return (
      <div className="container">
        <ul
          ref={el => {
            this.messagesEnd = el;
          }}
        >
          {game_messages && this.renderMessages(game_messages)}
        </ul>
      </div>
    );
  }
}

export default GameLog;
