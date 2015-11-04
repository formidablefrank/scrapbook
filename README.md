#How to run the app
Go to Linux terminal then follow the steps below:

Update software. Install python3.4, pip3, django1.8

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get intsall python3.4
sudo apt-get install python3-pip
sudo apt-get install libffi-dev libssl-dev
sudo -H pip install --upgrade pip
sudo -H pip install --upgrade pyopenssl ndg-httpsclient pyasn1
sudo -H pip install --upgrade Django
sudo -H pip3 install --upgrade pip
sudo -H pip3 install --upgrade pyopenssl ndg-httpsclient pyasn1
sudo -H pip3 install --upgrade Django
```

Clone repo (using HTTPS or SSL):
```
git clone https://github.com/formidablefrank/scrapbook.git
-or-
git clone git@github.com:formidablefrank/scrapbook.git
```

Change working directory to repo
```
cd scrapbook
```

Make virtualenv for the repo:
```
virtualenv env -p /usr/bin/python3.4
```

Activate virtualenv:
```
source env/bin/activate
```

Install project depedencies:
```
pip3 install -r requirements.txt
```

Install NodeJS:
```
apt-get install curl
curl --silent --location https://deb.nodesource.com/setup_0.12 | sudo bash -
apt-get install --yes nodejs
```

Install Gulp and JQuery (http://semantic-ui.com/introduction/getting-started.html):
```
npm install -g gulp
npm install jquery
npm update
npm install semantic-ui --save
cd semantic/
gulp build
```

Gulp watch for changes in style configs to update css/js files
```
gulp watch
gulp serve
gulp build
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

Django-Python console:
```
python3.4 manage.py shell
```

#Options for IDE
Lastly, install PyCharms Community Edition (IDE for Python/Django projects).
This is optional, you can use basic code editors like Atom and Sublime
https://www.jetbrains.com/pycharm/download/

Next best is Atom Text Editor
https://atom.io
