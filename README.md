# Used Car Selling Website --- django project 

The basic scenario of this project is to make a website for a car business owner who wants to list his car in his website and allow the user to come to the site and browser through all of his latest cars and feature cars, search and filter the cars by model or price and make some inquiries about his cars that are out for the sale. <br>

## Link for Heroku App
Click here! -> [Heroku App](https://demo-django-0116.herokuapp.com/)

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
      
   - Django App <br>
      step 1) Pages:
         - $ python3 manage.py startapp pages
	      - Add app in instant app of setting
	      - add urls.py in pages
         - $ python3 manage.py startapp accounts <br>
      step 2) Go to Setting file <br>
      step 3) Create url.py <br>
      step 4) Create function in view.py <br>
      step 5) Create accounts folder under template and login.html <br>
      
3. Models
   - use to store data in database

4. Make css / js work 
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
