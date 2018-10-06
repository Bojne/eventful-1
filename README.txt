1) Install virtualenv
2) mkvirtualenv with python version 3 
	- mkvirtualenv -p python3 <NAME_ENV>
	- workon <NAME_ENV> *(NOTE if you're not using virtualenvwrapper, the command is source <PATH TO ENV>)
3) Install pip
4) Install requirements
	- pip install -r requirements.txt
	
5) Database Migrations (Sqlite3)
	- cd backend
	- python manage.py makemigrations
	- python manage.py migrate
	
6) Create superuser
 	- python manage.py createsuperuser

7) Start the backend server
	- python manage.py runserver
	- In browser, open 127.0.0.1/admin