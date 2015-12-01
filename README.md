#Pitch for tomorrow's presentation
Are you tired of organizing and publishing your scrapbooks efficiently?
Are you tired of maintaining and updating your scrapbooks?
Then, Team Forever (wew) presents to you, A Life's Journey Photo Scrapbook, because we keep memories that's better than ever.
We are providing an online platform to organize current scrapbooks, integrate it with social media and export it in different formats.

1. CREATE
(Open create scrapbook interface)
Users can create a scrapbook to organize recent photos and see gradual progress of the subject in focus.
Users can indicate how the scrapbook should be updated and the frequency of uploading photos.
The web app has a notification system that reminds the user if he should upload a photo so that the scrapbook will still be updated.

2. UPLOAD/VIEW/DELETE/DOWNLOAD PHOTOS
(Go to dashboard)
In the user dashboard, users can see his current scrapbook and archived scrapbooks.
Archived scrapbooks are just closed scrapbooks where the user's goal is already met.
(View current Scrapbook)
After creating a scrapbook, users can now upload their photos and view them immediately.
(Try to upload a photo)
The web app has an elegant and intuitive interface for better user interaction.
(View current scrapbook)
Viewing photos can be in thumbnail mode or slideshow mode.
(Hover at different photos)
In thumbnail mode, photos are arranged chronologically and a specific photo can be viewed in slideshow mode or delete it.
In slideshow mode, a photo can be downloaded or shared in social media sites like Facebook and Twitter.

#Reminder
Every time you edit this repo, make sure you have pulled the repo first, update dependencies, and update your migrations.
```
git pull origin master (https)
git pull -u origin master (SSH)
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
```

#How to run the app
Go to Linux terminal then follow the steps below:

Update software. Install python3.4, pip3, django1.8

```
sudo apt-get update --yes
sudo apt-get upgrade --yes
sudo apt-get install --yes python3.4
sudo apt-get install --yes python3-pip
sudo apt-get install --yes build-essential python
sudo apt-get install --yes python-dev
sudo apt-get install --yes libffi-dev libssl-dev
sudo -H pip install --upgrade pip
sudo -H pip install --upgrade cffi
sudo -H pip install --upgrade setuptools
sudo -H pip install --upgrade Django
sudo -H pip install --upgrade selenium
sudo -H pip3 install --upgrade pip
sudo -H pip3 install --upgrade cffi
sudo -H pip3 install --upgrade setuptools
sudo -H pip3 install --upgrade pyopenssl ndg-httpsclient pyasn1
sudo -H pip3 install --upgrade Django
sudo -H pip3 install --upgrade selenium
```


Clone repo (using HTTPS or SSH):
```
git clone https://github.com/formidablefrank/scrapbook.git
-or-
git clone git@github.com:formidablefrank/scrapbook.git
```
To clone using SSH, make sure you have submitted your public key in your account settings on GitHub.
SSH facilitates passwordless transactions.



Change working directory to repo
```
cd scrapbook
```



Make virtualenv for the repo:
```
virtualenv env -p /usr/bin/python3.4
```



Activate virtualenv and each time you modify this project:
```
source env/bin/activate
```



Install project depedencies:
```
pip3 install -r requirements.txt
```



Django make migrations (after you update models and save objects):
```
python3.4 manage.py makemigrations
python3.4 manage.py migrate [--fake]
```



Django check for errors in codebase and run the server
```
python3.4 manage.py check
python3.4 manage.py runserver
```



In your web browser, go to http://localhost:8000/



#Other Stuff

Django-Python console:
```
python3.4 manage.py shell
```

You can install PyCharms Community Edition (IDE for Python/Django projects).
This is optional, you can use basic code editors like Atom and Sublime
https://www.jetbrains.com/pycharm/download/



Next best IDE is Atom text editor
https://atom.io



Usage of Django-extensions
https://github.com/django-extensions/django-extensions



Usage of Unipath
https://github.com/mikeorr/Unipath



Deploying Python webapps on Heroku with uWSGI
http://uwsgi-docs.readthedocs.org/en/latest/tutorials/heroku_python.html



Deployment with WhiteNoise
http://whitenoise.evans.io/en/latest/



#Customizing SemanticUI
Install NodeJS:
```
apt-get install curl
curl --silent --location https://deb.nodesource.com/setup_0.12 | sudo bash -
apt-get install --yes nodejs
```



Install Gulp and JQuery (http://semantic-ui.com/introduction/getting-started.html):
```
npm install -g gulp
npm update
npm install semantic-ui --save
```


Follow install instructions. When asked for a folder name, specify 'static\'
```
cd static/
gulp build
```


Gulp: watch for changes in style configs to update css/js files
```
gulp watch
gulp serve
gulp build
```

You can now modify 'static/src/theme.config'



#Installing Pillow Package
First, reinstall project dependencies as given above.

If you encounter
```
ValueError: --enable-jpeg requested but jpeg not found, aborting.
```
during installation of Pillow, do the following:


Install the following package, make a symlink then reinstall project dependencies again.
```
sudo apt-get install libjpeg62-turbo-dev
sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
pip3 install -r requirements.txt
```



#Testing
1. Testing the whole suite
2. Testing a specific case in the suite
3. Testing unit tests on the model
```
python3 manage.py test functional_tests
python3 manage.py test functional_tests.tests.Welcome.test_can_view_photos_in_current_scrapbook
python3 manage.py test scrapbook
```
