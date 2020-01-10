import React from "react";
import "./GameLog.scss";

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
    //this.scrollToBottom();
  }

  componentDidUpdate() {
    //this.scrollToBottom();
  }

  scrollToBottom() {
    const chat = this.messagesEnd;
    const scrollHeight = chat.scrollHeight;
    const height = chat.clientHeight;
    const maxScrollTop = scrollHeight - height;
    chat.scrollTop = maxScrollTop > 0 ? maxScrollTop : 0;
  }

  renderMessages(messages) {
    if (messages && messages.length > 0) {
      const currentUser = this.state.username;
      // return messages.map(entry =>
      //     <li key={entry}>{entry}</li>
      // )
      return messages.map((message, i) => (
        <li
          key={message.id}
          className={message.user === currentUser ? "me" : "him"}
        >
          <h4 className="author">{message.author} </h4>
          <p>{message.content}</p>
        </li>
      ));
    }

    // return (<li key={1} className='me'>
    //     <h4 className='author'>{"asfasfasf"} </h4><p>{"asdfsdf"}</p></li>)
  }

  render() {
    const game_messages = this.state.log;
    return (
      <div className="">
        <div className="">
          {/* {
                    this.state.log.map(entry =>
                        <li key={entry}>{entry}</li>
                    )
                } */}
          <ul
            ref={el => {
              this.messagesEnd = el;
            }}
          >
            {game_messages && this.renderMessages(game_messages)}
          </ul>
        </div>
      </div>
    );
  }
}

export default GameLog;

// import React from 'react';

// import "./GameLog.css";

// const GameLog = (props) => {

//     return (
//         <div>
//             {
//                 props.data.map(entry =>
//                     <li key={entry}>{entry}</li>
//                 )
//             }
//         </div>
//     );
// }

// export default GameLog;
