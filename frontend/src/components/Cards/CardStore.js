import React from 'react';
import Card from "react-bootstrap/Card";
import './CardStore.css'
import Button from 'react-bootstrap/Button';
import GameInstance from "../../services/gameService";

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
      cardName: 'Card Name',
      cardCost: 3,
      cardType: 'keep',
      cardEffect: 'lose two hearts, gain 4 energy',
      cardFootnote: 'Description',

    };
  }

  componentDidMount() {
    // ... do something with fetchedData e.g. set the data
  }

  sendSelectedCard() {

    let selected = this.state.selectedCard;

    if (selected && selected.length > 0) {
      const messageObject = {
        from: this.props.currentUser,
        data: selected
      };

      GameInstance.sendSelectedCard(messageObject);
      this.setState({
        message: ''
      })
    }
  }

  randomCardsCommand(user, room, cmd) {
    return {
      command: "randomcards_send_request",
      user: user,
      room: room,
      payload: 3
    };
  }

  handleChange(e) {
    this.setState({ value: e.Button });
    this.props.callbackSendCardSelectionOut(e);
  }

  clearSelected(e) {
    this.setState({ value: [] });
  }


  render() {
    return (
      <container className="card">
        <div className='row'>
          <div className='col-sm'>
            <div id='card'>
              <Card>
                <Card.Body>
                  <Card.Title>{this.state.cardName}</Card.Title>
                  <Card.Subtitle className="mb-2 text-muted">Cost: {this.state.cardCost}</Card.Subtitle>
                  <Card.Text>Card Type: {this.state.cardType}</Card.Text>
                  <Card.Text>Effect: {this.state.cardEffect}</Card.Text>
                  <Card.Text>Footnote: {this.state.cardFootnote}</Card.Text>
                </Card.Body>
              </Card>

              <Card>
                <Card.Body>
                  <Card.Title>{this.state.cardName}</Card.Title>
                  <Card.Subtitle className="mb-2 text-muted">Cost: {this.state.cardCost}</Card.Subtitle>
                  <Card.Text>Card Type: {this.state.cardType}</Card.Text>
                  <Card.Text>Effect: {this.state.cardEffect}</Card.Text>
                  <Card.Text>Footnote: {this.state.cardFootnote}</Card.Text>
                </Card.Body>
              </Card>

              <Card>
                <Card.Body>
                  <Card.Title>{this.state.cardName}</Card.Title>
                  <Card.Subtitle className="mb-2 text-muted">Cost: {this.state.cardCost}</Card.Subtitle>
                  <Card.Text>Card Type: {this.state.cardType}</Card.Text>
                  <Card.Text>Effect: {this.state.cardEffect}</Card.Text>
                  <Card.Text>Footnote: {this.state.cardFootnote}</Card.Text>
                </Card.Body>
              </Card>
            </div>
            <Button onClick={this.setRedirect} className="btn btn-secondary">Card Store{this.state.CardStore}</Button>
            &nbsp;&nbsp;&nbsp;
                <Button onClick={this.shuffleCards} className="btn btn-secondary">Shuffle Cards{this.state.allowShuffleCards}</Button>
          </div>
        </div>
      </container>

    );
  }
}

export default CardStore;
