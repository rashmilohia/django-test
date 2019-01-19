First create a Django virtual env on your local system:
1. Rashmis-MacBook-Air:~ rashmilohia$ mkdir django-projects
2. Rashmis-MacBook-Air:~ rashmilohia$ cd django-projects
3. Rashmis-MacBook-Air:django-projects rashmilohia$ python3 -m venv django-env
4. Rashmis-MacBook-Air:django-projects rashmilohia$ . django-env/bin/activate
5. (django-env) Rashmis-MacBook-Air:django-projects rashmilohia$ django-env/bin/django-admin.py startproject rashmi_django_test GitHub/django-test/
Here I have locally cloned my github directroy django-test in GitHub Desktop app. I am now basically creating a new project rashmi_django_test under this folder to get started with my Django app
6. (django-env) Rashmis-MacBook-Air:django-test rashmilohia$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK
7. (django-env) Rashmis-MacBook-Air:django-test rashmilohia$ python manage.py runserver
8. I have used crisy forms so incase you donot already have it installed in your system please install it using:
pip install django-crispy-forms
     
