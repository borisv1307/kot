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
      index: [3],
      username: props.currentUser,
      gameRoom: props.currentRoom,
      value: [],
      selectedCard: [],
      card: [
        {
          name: 'Card Name',
          cost: 3,
          type: 'keep',
          effect: 'lose two hearts, gain 4 energy',
          footnote: 'footnote description'
        }
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
      <div>
        <Card className="card">
          {
            this.state.card.map((card, key) => (
              <div key={key}>
                <div>{card.name}</div>
                <div>{card.cost}</div>
                <div>{card.type}</div>
                <div>{card.footnote}</div>
              </div>
            )

            )}
        </Card>

        <Button onClick={this.setRedirect} className="btn btn-secondary">Card Store{this.state.CardStore}</Button>
        &nbsp;&nbsp;
        <Button onClick={this.shuffleCards} className="btn btn-secondary">Shuffle Cards{this.state.allowShuffleCards}</Button>
      </div>
    );
  }
}
export default CardStore;