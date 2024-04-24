To Run development server: py manage.py runserver
To create new Module : py manage.py startapp <module name>
After creating module in mysite/settings.py need to provide an entry 
INSTALLED_APPS = [
    "polls.apps.PollsConfig", # like this
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
<module name>/view.py => logic
<module name>/url.py => specify Module endpoint path and its respective function
mysite/urls.py => overall endpoint path and specify module endpoint path
<module name>/models.py => need to create model here will a take afte running the below command
Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.

Playing with the API
py manage.py shell

Database Setup
Postgresql
mysite/settings.py
