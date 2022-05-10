# Apps that are not in development or production at this time.  
  
## cyclepics
- Flask python app that randomly cycles through cat images and displays them through index.html  
**Dockerfile**: spins up an alpine distro image, installs pip, installs flask via requirements.txt, maps port 5000, and runs app.py  
**app.py**: flask app randomly cycles through cat images and displays them through index.html  
**requirements.txt**: app requires flask *(see Dockerfile)*  
  
## flaska
- Spins up a simple flask app  
**Dockerfile**: Spins up an ubuntu image, installs pip, installs flask and uses flask run command for app.py  
**app.py**: outputs "Hello flasktestapp User!"  

