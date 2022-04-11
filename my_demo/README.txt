Hello and welcome to web 4.0's Django tutorial!

We hope that our material helps you become a great rapid web developer.

DEPENDENCIES (virtual environment recommended):
1. Ensure that you have Python 3
    Download the latest version if necessary:
        https://www.python.org/downloads/

2. Install Django (Windows, macOS, Linux, Solaris)
    Using pip in the terminal:
        $ python -m pip install Django
    Help:
        https://docs.djangoproject.com/en/4.0/topics/install/


VIRTUAL ENVIRONMENT HELP:
    Terminal:
        virtualenv newenv
        cd newenv
        source bin/activate
    Help:
        https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment


START DEVELOPING!
OUR TUTORIAL:
1. Activate your virtual environment
    Terminal:
        source bin/activate
    
2. Add yourself as a superuser to view Bevo's admin page
    Terminal:
        django-admin createsuperuser

    fill out respective fields (email not necessary)

    Run the demo in terminal and pull up website:
        django-admin runserver
    
    Add "admin/" to the url and easily view the database info

3. Add the best_school field to bevo's contact model and form
    Uncomment lines in the contact direcotry in forms.py and models.py

    Change the database in the terminal:
        django-admin makemigrations contact
        django-admin migrate
    
    Rerun to view new changes in terminal:
        django-admin runserver

4. Edit bevo's about page HTML file in templates
    While the website is still up (no Ctrl+C !), navigate to the about.html file

    Add necessary info like "I am orange and like to play in fields" to
        the file and save your edits with Ctrl+s
    
    No need to rerun from the terminal or migrate-- just refresh your website
    (If you quit the server just rerun django-admin runserver in the terminal to view changes)

5. Create a new app to list bevo's friends by following steps 4-8

START NEW PROJECT:
1. Activate your virtual environment
    Terminal:
        source bin/activate
2. Create a project
    Terminal:
        cd /filepath_to_desired_location/
        django-admin startproject site_name

3. View & edit settings
    - make your code os-independent by using import os & os.path()
    https://docs.djangoproject.com/en/4.0/intro/reusable-apps/

4. Create apps
    Terminal:
        django-admin startapp app_name

    register your model in admin.py

    add your app name to INSTALLED_APPS in settings.py of the project directory

    create and edit models in models.py
        https://docs.djangoproject.com/en/4.0/topics/db/models/

5. Create views and get website ready
    create HTML files for your app's page
        https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics
    
    edit views in views.py to incorporate HTML
        https://data-flair.training/blogs/django-views/

    add the path to your url in urls.py
        https://docs.djangoproject.com/en/4.0/topics/http/urls/

6. Migrate
    Terminal:
        django-admin makemigrations app_name 
        django-admin migrate

7. Run
    django-admin runserver

8. Edit & repeat steps 3-8!

Good luck!