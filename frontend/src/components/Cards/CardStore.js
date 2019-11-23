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
            <div className='row'>
             <div className='col-sm'>
            <div id='card'>
            <Card>
                <Card.Body>
                <Card.Title>Card One {this.cardName}</Card.Title>
                 <Card.Subtitle className="mb-2 text-muted">Cost (3) {this.cardCost}</Card.Subtitle>
                    <Card.Text>Type (keep){this.cardType}</Card.Text>
                    <Card.Text>
                        Description of the effects of the card {this.cardEffect}
                     </Card.Text>
                    <Card.Text>{this.cardFootnote}</Card.Text>
                    </Card.Body>
            </Card>

            <Card>
                <Card.Body>
                <Card.Title>Card One {this.cardName}</Card.Title>
                 <Card.Subtitle className="mb-2 text-muted">Cost (2) {this.cardCost}</Card.Subtitle>
                    <Card.Text>Type (discard){this.cardType}</Card.Text>
                    <Card.Text>
                        Description of the effects of the card {this.cardEffect}
                     </Card.Text>
                    <Card.Text>{this.cardFootnote}</Card.Text>
                    </Card.Body>
            </Card>

            <Card>
                <Card.Body>
                <Card.Title>Card One {this.cardName}</Card.Title>
                 <Card.Subtitle className="mb-2 text-muted">Cost (5) {this.cardCost}</Card.Subtitle>
                    <Card.Text>Type (keep){this.cardType}</Card.Text>
                    <Card.Text>
                        Description of the effects of the card {this.cardEffect}
                     </Card.Text>
                    <Card.Text>{this.cardFootnote}</Card.Text>
                    </Card.Body>
            </Card>
            </div>
                  <Button onClick={this.setRedirect} className="btn btn-secondary">Card Store {this.state.CardStore}</Button>
            </div>
             </div>
            </container>

        );
    }
}

export default CardStore;