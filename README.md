# A Life's Journey
## Photo Scrapbook
### *Keeping memories that's better than ever.*


**Developers**
- Francis Dimzon
- Gushi Montes
- Frank Rayo
- Herbie Villafranca
- JP Yusiong


**Adviser**
- Prof. Susan Festin


CS 260 - Advanced Software Engineering

Department of Computer Science

National Graduate School of Engineering

University of the Philippines Diliman



*In applying test-driven development and a necessary requirement for completion of the said course.*

**Development Environment**

*Backend Framework*: Django 1.8, Python 3.5

*Backend Dependencies*: *see 'requirements.txt'*

*Testing Library*: Python Unit Test, Selenium

*Frontend Framework*: Semantic UI, JQueryUI

*Asset Management*: Gulp

*IDE*: Jetbrains PyCharms *Community Edition*



## Pitch for tomorrow's presentation
- Are you tired of organizing and publishing your scrapbooks efficiently?
- Are you tired of maintaining and updating your scrapbooks?
- We, Team Forever :3 presents to you, *A Life's Journey Photo Scrapbook* keeping memories that's better than ever.
- We are providing an online platform to organize current scrapbooks, integrate it with social media and export it in different formats.

### Create Scrapbook

(Open create scrapbook interface)
- Users can create a scrapbook to organize recent photos and see gradual progress of the subject in focus.
- Users can indicate how the scrapbook should be updated and the frequency of uploading photos.
- The web app has a notification system that reminds the user if he should upload a photo so that the scrapbook will still be updated.

### Upload/View/Share/Delete Photos

- (Go to dashboard)
- In the user dashboard, users can see his current scrapbook and archived scrapbooks.
- Archived scrapbooks are just closed scrapbooks where the user's goal is already met.
- (View current Scrapbook)
- After creating a scrapbook, users can now upload their photos and view them immediately.
- The user just need to input the name of the picture and its description.
- (Try to upload a photo)
- The web app has an elegant and intuitive interface for better user interaction.
- (View current scrapbook)
- Viewing photos can be in thumbnail mode or slideshow mode.
- (Hover at different photos)
- In thumbnail mode, photos are arranged chronologically and a specific photo can be viewed in slideshow mode or delete it.
- (Click the view button)
- In slideshow mode, a photo can be downloaded or shared in social media sites like Facebook and Twitter.
- Again, the webapp will notify the user if he should upload more photos to keep the recent scrapbook updated.

### Close Scrapbook

- If the user has already completed the scrapbook and met his goal, he can already archive or close the scrapbook.
- Closing the scrapbook will make it read-only and photos cannot be uploaded anymore.

### Publish Scrapbook

- This webapp also provides the user ways on how to export scrapbooks in printable formats like PDF.

### Conclusion
- Say goodbye to hardbound and thick photo albums!
- This is more than just Instagram or Flickr or Photobucket.
- Using cloud storage, we offer everyone more flexibility in managing their active scrapbooks and access them anytime, anywhere.
- Because we believe that treasuring memories better should be easy as much as possible
- Again, this is *A Life's Journey Photo Scrapbook*, keeping memories that's better than ever.

### Appendix: *What other features can be implemented*
- User management and authentication system
- Email notification system
- Edit photo name, edit description
- Download whole scrapbook
- Social media API integration for sharing
- Maps API integration for geospatial visualization
- Making video slide shows
- Publish as AVI video

------------------------------------------------------------------------------------------------------------------------

#Development Reminders
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

#Markdown Basics
Click the link: [Visit Github!](https://help.github.com/articles/markdown-basics/)
