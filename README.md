# Used Car Selling Website --- django project 

The basic scenario of this project is to make a website for a car business owner who wants to list his car in his website and allow the user to come to the site and browser through all of his latest cars and feature cars, search and filter the cars by model or price and make some inquiries about his cars that are out for the sale. <br>

## Link for Heroku App
Click here! -> [Heroku App](https://demo-django-0116.herokuapp.com/)

## Solid Features
1. Search Function
	- search cars by name, model, location, year, price
2. Pagination
	- list any numbers of car you want in a single page
3. Send Message
	- For customers, they can send a message to request for more information to a certian car they interested in
	- For the same car, one login account can send only one message
4. Login 
	- can login by facebook and google
5. Register
	- need to be different username with other members
	- email account need to include @
	- Confirm password needs to be same as password
6. Send Email
	- when users request for more information
	- or use the "Contact Us" service in the website
	- Admin will recieve users' message by receiving the email
7. Messages
	- successful or unsuccessful login will both pop out messages to inform users
8. Admin	
	- maintain users' personal information
	- put information of cars (featured/ name/ city/ color/ vin/ Used/ .......)
	- authenticated site 

## Database
Dynamically store data from PostgreSQL database

## Basic Idea & Steps
1. Create a website 
   - For car business owners who want to list their cars
   - For customers who want a user-friendly website
   
2. Details of building the project
   - Virtual Environment <br>
      I want my project in isolated environment.
      * $ python -m venv env
      * $ source ./env/bin/activate
      
   - Software (install)
      * git gui
      * pycharm (python editor)
      
   - Django Project
      * $ pip install django==3.0.7
      * $ pip install --upgrade pip
      * $ django-admin startproject carzone
      
3. Django App <br>
   - $ python3 manage.py startapp {app_name} <br>
   - Add app(created_app/app.py) in instant app of setting(project) <br>
	```python 
	'pages.apps.PagesConfig', 
	```	
   - Manually create urls.py in created_app <br>
   	```python
	  path('', views.home, name='home'), 
	  ```
   - Create a function in created_app/views.py to render a html page <br>
	```python
     def home(request): 
     	return render(request, 'pages/home.html', data) 
 	```
   - create exact .html under templates folders	
  	 - you should create templates folder under your porject, it is the place you put all the html files in		
   - announce it project/setting.py
   ```python
   	TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
	...
	```
4. Models
   - use to store data in database

5. Make css / js work 
   - $ python3 manage.py collectstatic
      
## Deployed to Heroku
1. Create Procfile and runtime.txt
2. install Heroku (macOS) and prepared
   - $ brew tap heroku/brew && brew install heroku
   - $ heroku login
   - $ pip install gunicorn psycopg2-binary 
   - $ pip install dj-database-url
   - $ pip install whitenoise
   - update setting.py
3. Add all packages to your project
   - $ pip freeze > requirements.txt
4. Push to Git
   - git init
   - git add -A
   - git commit -m "message"
   - git push
 5. Create Heroku App
 	- $ heroku create name
   	- $ git push origin main
   	- $ heroku open
   	- $ heroku run python manage.py collectstatic 
