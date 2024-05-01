This is to deploy Flask python app project through Caddy.

The steps to deply Flask app are as follows:
I have used Caddy which is a webserver which will be used to take our request to the outside world.

1. Launch an ubuntu machine & run sudo apt-get update -y"
2. Install git & clone the github repo into your machine:
	  2.1. sudo apt-get install git-all -y
    2.2. git clone <repo_url>
3. Run CURL commnds to add Caddy into the repository & install Caddy
    3.1. sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
    3.2. curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
    3.3. curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
    3.4. sudo apt-get update
    3.5. sudo apt install caddy
4. You'll be able to see the caddy home page once completion of above steps (http://<public-ip>).
5. Check/Install python3
6. Run commands to install pip and python3 virtual environment
    6.1. sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools  				# (click on Ok, if a prompt opens).
    6.2. sudo apt install python3-venv
7. Now create a virtual environment and activate(start) it.
    7.1. python3 -m venv virtualenv																# (here, virtualenv is the name of virtual environment).
    7.2. source virtual_env/bin/activate
8. Goto, your project directory and install requirement.txt
    8.1. cd to project directory
    8.2. pip install -r requirements.txt
9. Once all the requirements are installed through requirements.txt, run:
    9.1. gunicorn main:app																					# (here, main is the main.py & app is the gunicorn application ; to stop it press ctrl + c).
10. Make changes in Caddyfile
    10.1. vi Caddyfile
    10.2. Change the IP with you machine's public IP, and save the file
    10.3. sudo caddy stop
    10.4. sudo caddy start
11. Start you application
    11.1. gunicorn main:app
    11.2. gunicorn main:app &																					# to keep it running while you are logged in.
    11.3. gunicorn --bind 0.0.0.0:8000 wsgi:app --daemon					# binding the app & system Ip & port, daemon is used to keep gunicorn running when you're logged out of instance; make changes in wsgi.py file accordingly.
12. To stop the gunicorn
    12.1. run, ps xf
    12.2. kill <gunicorn-process-id>

	
