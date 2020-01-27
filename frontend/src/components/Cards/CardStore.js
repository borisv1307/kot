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
      selectedCard: []
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
            <Button onClick={this.selectCard} className="btn btn-secondary">Card Store{this.state.cardStore}</Button>
            &nbsp;&nbsp;&nbsp;
                  <Button onClick={this.shuffleCards} className="btn btn-secondary">Shuffle Cards{this.state.allowShuffleCards}</Button>
          </div>
        </div>
      </container>
    );
  }
}
export default CardStore;
