Project Setup
=========================


1. git clone https://github.com/Arjun668/ajackus_assignment.git
2. pip install requirements.txt
3. Create "migrations" folder for each app "api/account" and "api/cms"
4. Add __init__.py file in "migrations" folder for each app "api/account" and "api/cms" 
5. Create "media" folder in the root of project

6. Run Below Command to setup database
    * python manage.py makemigrations
    * python manage.py migrate
    
7. Run below command to create Superuser 
    * python manage.py createsuperuser
    
8. Run below command to run server
    * python manage.py runserver
    
9. Now, Login to the admin with superuser credentials
10. Create 2 Group
    * Admin
    * Author
    
11. Now add your self to the admin on click of user (superuser email id) 
12. Add Some categories for content.

    
