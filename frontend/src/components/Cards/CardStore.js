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
      card: [
        { name: 'Armor Plating', cost: 4, type: 'Keep', effect: 'Ignore damage of 1', footnote: ' ' },
        { name: 'Commuter Train', cost: 4, type: 'Discard', effect: 'Gain 2 victory points', footnote: ' ' },
        { name: 'Giant Brain', cost: 5, type: 'Keep', effect: 'You have one extra reroll each turn', footnote: ' ' }
      ]
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

  handleChange(e) {
    this.setState({ value: e });
    this.props.callbackSendCardSelectionOut(e);
  }

  clearSelected(e) {
    this.setState({ value: [] });
  }


  render() {
    return (
      <container className="card">
        <div className="row">
          <div className="col-sm">
            <div className="card" type="checkbox">
              {
                this.state.card.map((entry, index) => (
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
            <Button onClick={this.setRedirect} className="btn btn-secondary">Card Store{this.state.cardStore}</Button>
            &nbsp;&nbsp;&nbsp;
                <Button onClick={this.shuffleCards} className="btn btn-secondary">Shuffle Cards{this.state.allowShuffleCards}</Button>
          </div>
        </div>
      </container>
    );
  }
}
export default CardStore;
