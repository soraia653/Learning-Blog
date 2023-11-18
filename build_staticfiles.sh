yum install -y https://centos6.iuscommunity.org/ius-release.rpm
yum install -y python312

# Install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.12 get-pip.py

# Install project requirements
pip install -r requirements.txt

python 3.12 manage.py makemigrations
python 3.12 manage.py migrate

# Build staticfiles
python3.12 manage.py collectstatic