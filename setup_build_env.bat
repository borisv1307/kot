python -m venv env
call env\Scripts\activate
pip install -r requirements.txt
python -m pip install --upgrade pip
pip install -r requirements.txt

cd backend
python manage.py migrate
start cmd.exe @cmd /k "python manage.py runserver"

cd ..
cd frontend
npm install
start cmd.exe @cmd /k "npm start"