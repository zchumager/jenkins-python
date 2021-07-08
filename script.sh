echo "Executing Shellscript"

apt-get install python3-pip -y

python3 -m pip install --upgrade pip setuptools wheel

python3 -m pip install --user pipenv

python3 -m pipenv install requests

python3 app.py