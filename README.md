# Hellowello
![hellowello Logo](https://res.cloudinary.com/dgiguwrz1/image/upload/v1576932986/Hello_Wello.png "HelloWello Logo")

HelloWello is a simple django app

For running it on your machine you need to do the following:

#### Setting up Django
###### Python
To run django on your machine you must have python installed
you can download python suitable for your machine here: [Python download](https://www.python.org/downloads/)

After downloading the installer, you should run it and During the installation, you will notice a window marked "Setup". Make sure you tick the "Add Python x.x to PATH" checkbox and click on "Install Now"
When the installation completes type: 

```cmd
python --version
```
in your command line(Terminal) to make sure python has been installed successfully.

###### Django
for installing django you can just run:

```cmd
pip install Django
```
if this doesn't work for you, check your enviroment variables and add pip or just run this instead:
```cmd
python -m pip install Django
```
After installing django run this in your terminal:
```cmd
django-admin --version
```
in your command line(Terminal) to make sure everything works fine and if it does, Congratulations you are done with setting up django.

#### Git
Make sure that you have git installed in your machine you can find more information [Here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)


#### Running offline
for running HelloWello in your machine you first need to follow These Steps Carefully:

* Open git bash
* Run these commands
```
git clone https://github.com/HooriaHIC/hellowello.git
cd hellowello
```
*  After that you are almost done you just need to run
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
* Open up your browser and goto http://localhost:8000
And you should see HelloWello Homepage.




