                starting the ecommerce project.
step1: start your virtual environment(cmnd - python -m venv myworld).
        and start your env(your_env_foldername/scripts/activate).
step2: installing all dependencies for our project like Django, sql etc..
step3: we can install dependencies through our requirement.txt file also but one   should have to define it through the following commands - the command to create requirement.txt file (pip freeze > requirements.txt), also to the command to check what is in a requirements.txt file (cat requirements.txt) , suppose if we want to create another project and again have to install all dependencies then instead we can use our previous requirement.txt file with command (pip install -r requirements.txt) NOTE: first you have to create an virtual env in tat folder than u can install the requirement.txt 
step4: creating a project : (django-admin startproject PROJECTNAME) NOTE: at any time if we want to check what and all tools installed in our virtual env then (pip list) will help you list all of them.
step5: creating Mysql database.
NOTES: the major settings coming on to django static folder and template folder are as follows , --- in settings->TEMPLATES--at DIRS add this line [BASE_DIR / "templates"], secondly for static folder at below STATIC_URL add this line of code for setting up static folder for css , js and images, -----> STATIC_URL = '/static/'
                                STATIC_URL = '/static/'

                                STATICFILES_DIRS = [
                                os.path.join(BASE_DIR, 'static')
                                ]
                                NOTE: add import os at top
                                
the project flow will somewhat look like this ---> main project
                                                  app folder 
                                                  templates folder 
                                                  static folder 
        within the template folder we have to specify respective app folder so that all html files can go into that particular app's folder, 
step 5: creating an app inside project folder 
        now comes the part where all the major connections takes place between app and project folder 
        first: the app folder doesnt have the urls file so we will either create one or copy paste from project folder, 
        secondly: whatever the html file we create inside template>app>index.html we have to define that path into views and then direct to urls, 
        third: write the views function first by adding a redirect module, after writting up the views now import those views in urls file which is located in same app folder. 
        third: after the connections and importing of views and urls file now we have to connect app folder to projects urls file so that the project can know that on start when hit with the particular url we have to show up such an such url coming from app folder, to add in project url file one have to write code like the follwing ---- 
        from django.contrib import admin
        from django.urls import path, include
        from app import urls as appurls
        urlpatterns = [
        path('admin/', admin.site.urls),
           path('', include(appurls))
        ]