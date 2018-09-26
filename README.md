# Outlay
This is a web-app written in Django with a purpose of providing an Expense tracking fucntionality. User can-
- Login/Signup
- Add/Edit item
- Sort/Filter table

The app is temporarily hosted [here](http://minusv.pythonanywhere.com/).
## Deploying App
### Cloning Repository
Open terminal and run the command:
```
git clone https://github.com/minusv/Outlay.git
```
### Installing Requirements
Open terminal(virtualenv) and run the following commands:
```
pip install -r requirements.txt
```
## Running App
> Complete the following steps in the directory containing `manage.py`.
### Migrating database
Open terminal(virtualenv) and run the command:
```
python manage.py migrate
```
### Running server
Open terminal(virtualenv) and run the command:
```
python manage.py runserver
```
***Congratulations!*** App is up and running!
