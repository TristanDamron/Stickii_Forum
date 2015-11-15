Forum for the Stickii Network

##INSTALLATION:
Stickii_Forum is a Django application, and thus only works with Django projects. Starting your own Stickii_Forum project requires python-2.7 or higher and Django-1.8 or higher. Once you have these dependencies met, open a terminal and enter:

###*cd projectparentdir && django-admin startproject forumproject*

These commands will create a new Django project called "forumproject" in the project's parent directory.
Once you've created the project, simply drag the original Stickii_Forum folder into the "forumproject" folder. Then, open the settings.py file located in your project's "forumproject" folder. In the list called "INSTALLED_APPS", add the following line:

###*'forum',*

This will add the Stickii_Forum app to your project. Now, migrate the database. You can do this by running these commands inside the "forumproject" directory:

###*python manage.py makemigrations forum && python manage.py migrate*

Finally, you must include the proper urls to the 'urls.py' file in the 'forumproject' folder. In the list called 'urlpatterns' add this line:

###*url(r'^', include('forum.urls')),*

Congratulations! You're ready to run Stickii_Forum! You can start a local server by running:

###*python manage.py runserver*

If you need assistance, check out the freenode IRC #stickii or review Django's documentation.

##The authors of this software are:
Tristan Damron
(If you worked on the project's code, add your name here!)
