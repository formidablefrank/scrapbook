#HOW TO INSTALL APP

Update software. Install python3.4, pip3, django1.8

```
sudo apt-get update
sudo apt-get upgrade
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
git clone https://github.com/jbrayo/scrapbook.git
-or-
git clone git@github.com:jbrayo/scrapbook.git
```

Make virtualenv for the repo:
```
virtualenv env -p /usr/bin/python3.4
```

Activate virtualenv:
```
source env/bin/activate
```

Install depedencies:
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

Django-Python console:
```
python3.4 manage.py shell
```
