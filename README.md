# kot

Drexel Software Studio

MUD game emulation of a board game Kot.

Backend documentation see \kot\backend\README.md.

Frontend documentation see \kot\frontend\README.md.

## First Time: Setup Enviorments

 * Do this once after first cloning KOT...
 * Setup Python
      > `cd \kot\backend\` </br>
      > `python -m venv env` </br>
      > `.\env\Scripts\activate` </br>
      > `pip install -r requirements.txt`

    NOTE: PIP or other prompts may suggest upgrading, please do so.

 * Setup React
      > `cd \kot\frontend\` </br>
      > `npm install`

## Running

 * Running Python Server
      > `python manage.py runserver`</br>

      Runs the app in the development mode.<br /> Open a browser, go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view python root.

 * Running React Server
      > `npm start`</br>

      Runs the app in the development mode.<br /> Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br /> You will also see any lint errors in the console.

## Testing

 * Testing Python
      > `pytest`</br>


 * Testing React
      > `cd \kot\frontend\`</br>
      > `npm test`
      
      Launches the test runner in the interactive watch mode.<br /> See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.
