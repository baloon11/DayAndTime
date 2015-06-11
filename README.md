
In the admin panel have been created 3 instances.

Before checking You need to adjust the time periods for each instance

In settings.py change TIME_ZONE = 'Europe/Kiev' 

(use this link http://stackoverflow.com/questions/13866926/python-pytz-list-of-timezones)


In application/models.py you can see the created model.

In application/views.py I created a function to check the times and days.

I tried to make this function as a method of the model
but for some reason in models.py datetime works not correctly.


for superuser:

login: test

pass:  test

Requirements
------------

    pip install django==1.6

(Python 2.7)