***Flask app randomly cycles through cat images and displays them through index.html***<br/>
contains:

**Dockerfile**: spins up an alpine distro, installs pip, installs flask via requirements.txt, exposes port 5000, and runs app.py<br/>
**app.py**:  flask app randomly cycles through cat images and displays them through index.html<br/>
**requirements.txt**: requires flask (see Dockerfile)<br/>
