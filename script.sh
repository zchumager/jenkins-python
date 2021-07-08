echo "Executing Shellscript"

apt-get install python3-pip

python3 -m pip install --upgrade pip setuptools wheel

python3 -m pip install --user pipenv

python3 app.py