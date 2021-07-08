echo "Executing Shellscript"

apt-get install pip

python3 -m pip install --upgrade pip setuptools wheel

python3 -m pip install --user pipenv

python3 app.py