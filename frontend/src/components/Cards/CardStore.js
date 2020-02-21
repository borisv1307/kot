import React from 'react';
import Card from "react-bootstrap/Card";
import './CardStore.css'
import Button from 'react-bootstrap/Button';

import GameInstance from "../../services/gameService";
import MT_RESPONSE_CARD_STORE_RESPONSE from "../../services/config";


class CardStore extends React.Component {
  constructor(props, context) {
    super(props, context);

    this.handleChange = this.handleChange.bind(this);
    this.clearSelected = this.clearSelected.bind(this);

    this.state = {
      username: props.currentUser,
      gameRoom: props.currentRoom,
      value: [],
      selectedCard: [],
      data: props.data
    };

    this.cardStoreRequest = this.cardStoreRequest.bind(this);
    GameInstance.addCardCallback(this.cardUpdateHandler.bind(this));
  }

  componentDidMount() {
    // ... do something with fetchedData e.g. set the data
  }

  handleChange(e) {
    this.setState({ value: e });
    this.props.callbackSendCardSelectionOut(e);
  }

  clearSelected(e) {
    this.setState({ value: [] });
  }

  async cardStoreRequest(/*e*/) {
    try {
        const messageObject = {
          user: this.state.username,
          room: this.state.gameRoom,
          data: ""
        };
        this.sendCardStoreRequest(messageObject);
    } catch (exception) {
      console.log(exception);
    }
  }

  sendCardStoreRequest(envelope) {
    GameInstance.sendMessage({
      command: "card_store_request",
      user: envelope.user,
      room: envelope.room,
      payload: ""
    });
  }

  cardUpdateHandler(message) {
    const content = message.content;

    if (content === undefined || content === "") return;

    let card_content = [];
    try {
      card_content = JSON.parse(content);
    } catch (e) {}
    this.setState({ selectedCard: card_content });
  }

  render() {
    if (this.state.selectedCard) {
      return (
        <container className="card">
          <div className="row">
            <div className="col-sm">
              <div className="card" type="checkbox">
                {
                  this.state.selectedCard.map((entry, index) => (
                    <Card key={index}>
                      <Card.Body>
                        <Card.Title>Card: {entry.name}</Card.Title>
                        <Card.Subtitle className="mb-2 text-muted">Cost: {entry.cost}</Card.Subtitle>
                        <Card.Text>Type: {entry.type}</Card.Text>
                        <Card.Text>Effect: {entry.effect}</Card.Text>
                        <Card.Text>{entry.footnote}</Card.Text>
                      </Card.Body>
                    </Card>
                  ))
                }
              </div>
              <Button onClick={this.cardStoreRequest} className="btn btn-secondary">Card Store</Button>
              &nbsp;&nbsp;&nbsp;
                    <Button onClick={this.shuffleCards} className="btn btn-secondary">Sweep Store{this.state.allowShuffleCards}</Button>
            </div>
          </div>
        </container>
      );
    } else {
      return <div></div>
    }
  }
}
export default CardStore;