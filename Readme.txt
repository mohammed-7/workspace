                starting the ecommerce project.
step1: start your virtual environment(cmnd - python -m venv myworld).
        and start your env(your_env_foldername/scripts/activate).
step2: installing all dependencies for our project like Django, sql etc..
step3: we can install dependencies through our requirement.txt file also but one   should have to define it through the following commands - the command to create requirement.txt file (pip freeze > requirements.txt), also to the command to check what is in a requirements.txt file (cat requirements.txt) , suppose if we want to create another project and again have to install all dependencies then instead we can use our previous requirement.txt file with command (pip install -r requirements.txt) NOTE: first you have to create an virtual env in tat folder than u can install the requirement.txt 
step4: creating a project : (django-admin startproject PROJECTNAME) NOTE: at any time if we want to check what and all tools installed in our virtual env then (pip list) will help you list all of them.
step5: creating Mysql database.
NOTES: the major settings coming on to django static folder and template folder are as follows , --- in settings->TEMPLATES--at DIRS add this line [BASE_DIR / "templates"], secondly for static folder at below STATIC_URL add this line of code for setting up static folder for css , js and images, -----> STATIC_URL = '/static/'
                                STATIC_ROOT = BASE_DIR / "static"
                                STATICFILES_DIRS = [BASE_DIR / "assets/static"]
                                after the above config in static run this following command  ->py manage.py collectstatic
the project flow will somewat look like this ---> main project
                                                  app folder 
                                                  templates folder 
                                                  static folder 
        within the template folder we have to specify respective app folder so that all html files can go into that particular app's folder, 