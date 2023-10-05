                starting the ecommerce project.
step1: start your virtual environment(cmnd - python -m venv myworld).
        and start your env(your_env_foldername/scripts/activate).
step2: installing all dependencies for our project like Django, sql etc..
step3: we can install dependencies through our requirement.txt file also but one   should have to define it through the following commands - the command to create requirement.txt file (pip freeze > requirements.txt), also to the command to check what is in a requirements.txt file (cat requirements.txt) , suppose if we want to create another project and again have to install all dependencies then instead we can use our previous requirement.txt file with command (pip install -r requirements.txt) NOTE: first you have to create an virtual env in tat folder than u can install the requirement.txt 
step4: creating a project : (django-admin startproject PROJECTNAME) NOTE: at any time if we want to check what and all tools installed in our virtual env then (pip list) will help you list all of them.
step5: creating Mysql database.