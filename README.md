# Data Project - django rest framework version

1. **Context of this Project**
   * This project is meant to represent the data of 10 seasons(2008-2017) of IPL in bar charts on browser using Highcharts Library of JavaScript while fetching data from RestApi built using Django REST framework.
   * Problem 1 is about plotting a bar chart of Total Runs scored by user selected teams from user given year range.
   * Problem 2 is about plotting a bar chart of Top 10 batsmen of a user selected team from user selected year.
   * Problem 3 is about plotting a bar chart of No. of umpires from each selected country by user who participated in IPL. 
   * Problem 4 is about plotting a stacked bar chart of user selected ipl teams and their total no of matches played season wise stacked in a selected year range.

2. **Setting up Environment**
    * Clone this repository using the command `git clone git@gitlab.com:mountblue/cohort-14-python/vijay_yarramsetty/dataproject-django-rest-framework.git`
    * Create a Virtual Environment for this project as we require some dependency packages to be installed.
      * `python3 -m virtualenv env` - creates a virtual environment in the root directory of cloned project
      * `source env/bin/activate` - activates virtual environment
      * Now to install dependency packages use the command `pip install -r requirements.txt`
    * We require a database and a user who is owner for that database. For this there are two helper SQL script files present in **sql_scripts** directory. The file names of these two files are self explanatory as one creates a user and a database and the other script file deletes the user and database from Postgres. To run this commands.
    * Follow these commands to create/drop databse.
      * `sudo -su postgres` - asks for your local machine root password. Enter it.
      * `psql -U postgres -f sql_scripts/create_user-db.sql` - creates a rol and DB. Both will have same names as per convention 'djangoproject'
      * `psql -U postgres -f sql_scripts/drop_user-db.sql` - for dropping both user and database from Postgres when work is done.
    * Now to update all models and django admin built-in models use the command `python manage.py migrate`
    * To load the data from csv files present in project root directory into database use the command `python manage.py adddata`
    * To start the project and access data on browser run the command `python manage.py runserver`. 
    * [Click this to view on browser](http://127.0.0.1:8000)
    * For each Question there is a dedicated button and when we click on it, the bar chart for the given input parameters will be displated using Javascript Highcharts library in the backend.
