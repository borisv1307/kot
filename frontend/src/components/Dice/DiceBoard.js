import React from 'react';
// import Select, { components } from 'react-select';
import { ToggleButton, ToggleButtonGroup } from 'react-bootstrap';

import "./DiceBoard.css";

// const DiceBoard = (props) => {
//     return (
//         <div>
//             <div className="dice_container">
//                 {
//                     // props.data.map(dice => {

//                     //     if (dice[1]) {
//                     //         return <li className="selected" key={dice.id}>{dice[0]}</li>
//                     //     } else {
//                     //         return <li className="unselected" key={dice.id}>{dice[0]}</li>
//                     //     }
//                     // })
//                     props.data.map(dice => {

//                         if (dice[1]) {
//                             return <li className="selected" key={dice.id}>{dice[0]}</li>
//                         } else {
//                             return <li className="unselected" key={dice.id}>{dice[0]}</li>
//                         }
//                     })


//                 }


//             </div>


//             <ToggleButtonGroupControlled />

//         </div>

//     );
// };

class DiceBoard extends React.Component {
    constructor(props, context) {
        super(props, context);

        this.handleChange = this.handleChange.bind(this);
        this.clearSelected = this.clearSelected.bind(this);

        this.state = {
            value: []
        };
    }

    handleChange(e) {
        this.setState({ value: e });
        this.props.callbackFromParent(this.state.value);
    }

    clearSelected(e) {
        this.setState({ value: [] });
    }

    render() {
        return (
            <ToggleButtonGroup
                vertical
                type="checkbox"
                value={this.state.value}
                onChange={this.handleChange}>
                {
                    this.props.data.map((entry, index) => (
                        <ToggleButton key={index} value={index + 1}>{entry[0]}</ToggleButton>
                    ))
                }
            </ToggleButtonGroup>
        );
    }
}



// export const colourOptions = [
//     { value: 'ocean', label: 'Ocean', color: '#00B8D9', isFixed: true },
//     { value: 'blue', label: 'Blue', color: '#0052CC', isDisabled: true },
//     { value: 'purple', label: 'Purple', color: '#5243AA' },
//     { value: 'red', label: 'Red', color: '#FF5630', isFixed: true },
//     { value: 'orange', label: 'Orange', color: '#FF8B00' },
//     { value: 'yellow', label: 'Yellow', color: '#FFC400' },
//     { value: 'green', label: 'Green', color: '#36B37E' },
//     { value: 'forest', label: 'Forest', color: '#00875A' },
//     { value: 'slate', label: 'Slate', color: '#253858' },
//     { value: 'silver', label: 'Silver', color: '#666666' },
// ];

// const options = [
//     { value: 'chocolate', label: 'Chocolate' },
//     { value: 'strawberry', label: 'Strawberry' },
//     { value: 'vanilla', label: 'Vanilla' },
// ];

// const controlStyles = {
//     borderRadius: '1px solid black',
//     padding: '5px',
//     background: colourOptions[2].color,
//     color: 'white',
//   };

//   const ControlComponent = props => (
//     <div style={controlStyles}>
//       {<p>Custom Control</p>}
//       <components.Control {...props} />
//     </div>
//   );

// class DiceSelector extends React.Component {

//     state = {
//         selectedOption: null,
//     };

//     constructor(props) {
//         super(props);

//         this.state = {
//             selectedOption: [], // this holds the name of each list
//         };
//     }

//     handleChange = selectedOption => {
//         this.setState(
//             { selectedOption },
//             () => console.log(`Option selected:`, this.state.selectedOption)
//         );
//     };


//     render() {
//         const { selectedOption } = this.state;

//         return (
//             <Select
//             defaultValue={colourOptions[0]}
//             isClearable
//             components={{ Control: ControlComponent }}
//             name="color"
//             options={colourOptions}
//             isMulti
//                 // value={selectedOption}
//                 // onChange={this.handleChange}
//                 // options={options}
//                 // defaultValue={[colourOptions[4], colourOptions[5]]}
//                 // isMulti
//             />
//             // <Select
//             //     onChange={this.handleChange}
//             //     options={options}
//             //     closeMenuOnSelect={false}
//             //     // components={{ DropdownIndicator }}
//             //     // defaultValue={[colourOptions[4], colourOptions[5]]}
//             //     isMulti
//             //     options={options}
//             // />
//         );
//     }
// }




export default DiceBoard;