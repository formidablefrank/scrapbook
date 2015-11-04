INSTALL python3.4, pip3, django1.8

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
sudo apt-get install libffi-dev libssl-dev
sudo -H pip(3) install --upgrade pip
sudo -H pip(3) install --upgrade pyopenssl ndg-httpsclient pyasn1
sudo -H pip(3) install --upgrade Django

for virtualenv:
virtualenv ENV -p /usr/bin/python3.4
source ENV/bin/activate

pip3 install -r requirements.txt
chmod +x manage.py
./manage.py migrate polls / python3 manage.py migrate polls / --fake
./manage.py check
./manage.py runserver
./manage.py shell
