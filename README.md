# kot

Drexel Software Studio

game emulation of a board game Kot.

Backend documentation see \kot\backend\README.md.

Frontend documentation see \kot\frontend\README.md.

## Hosting Options

- Production: React website hosted via Django server.

  - Build React: `npm build` copies static content to frontend/build/static.
  - Run Python `python manage.py runserver` hosts static content via django server.

- Development:
  - Run React: `npm start` to run development server.
  - Run Python `python manage.py runserver` to run python development server.

## Site Map

- <http://localhost:8000/>
- <http://localhost:8000/admin/>
- <http://localhost:8000/users/>

## Api's

#### Game Model Api's

- <http://localhost:8000/api/v1/game/view/>
  Get all the games and create game
- <http://localhost:8000/api/v1/game/list/>
  Get all the games and create game (alternate version)
- <http://localhost:8000/api/v1/game/detail/?/>
  Get games by the room name ?

## Quick Start

- Install dependencies then build production React build

> `cd \kot\frontend\` </br> > `npm install` </br> > `npm run build` </br>

## Setup Details

## Setup Environments

- Do this once after first cloning KOT...

- Option 1: Use Setup Python Virtual Environment (recommended) </br> > `cd \kot\` </br> > `python -m venv env` </br> > `.\env\Scripts\activate` </br> > `pip install -r requirements.txt`</br> > `python -m pip install --upgrade pip`</br> > `cd \kot\backend\`</br> > `python manage.py runserver` </br>

- Option 2: Use Pythons Global Enviornment </br> > `cd \kot\backend\` </br> > `pip install -r requirements.txt`

  NOTE: PIP or other prompts may suggest upgrading, please do so.

- Setup React > `cd \kot\frontend\` </br> > `npm install`

## Running

- Running Python Server > `python manage.py runserver`</br>

      Runs the app in the development mode.<br /> Open a browser, go to [http://localhost:8000/](http://localhost:8000/) to view python root.

- Running React Server > `npm start`</br>

      Runs the app in the development mode.<br /> Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br /> You will also see any lint errors in the console.

## Testing

- Testing Python > `pytest`</br>

- Testing React > `cd \kot\frontend\` </br> > `npm test`

  Launches the test runner in the interactive watch mode.<br /> See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

- Testing React w/ Coverage details > `cd \kot\frontend\` </br> > `npm run coverage`
