# Web-Store_2-
for Practice Stack: Python PostgreSQL Redis


Pages and Features included:
Home
Login
Register
Account
Add Product
Edit Product
Manage Products
Product List
Single Product View
How do I get setup?
Make sure you have latest python installed in your computer, you can download python from here:
https://www.tutorialspoint.com/django/django_environment.htm
Install django using pip:
pip install Django==1.11.2 or get the latest version here: https://www.djangoproject.com/download/
Verify your installation, run the following command:
python -m django –version

Setting up a new project in Django
From your command line, navigate to where you want to save your projects, then create a new project:
django-admin startproject myproject
Setup migrations
Run python manage.py makemigrations to create migrations
Run python manage.py migrate to apply those changes to the database.
Now that your project is created and configured make sure it’s working:
python manage.py runserver
Navigate to http://127.0.0.1:8000/ in your browser to view the application.
By default, the runserver command starts the development server on the internal IP at port 8000.
if you want to change the port, syntax is:
python manage.py runserver 8080
where 8080 is the different port.
if you want to share your project to other computers connected to the network, start the server like this:
python manage.py runserver 192.168.2.75:8000
Where 192.168.2.75 is your computer IP
You can quit the server with CONTROL-C.
