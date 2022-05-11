## apps not currently in production  
  
## cyclepics  
- flask py app. randomly cycles through cat images and renders one in a stylised html element  
- docker run as daemon container  
- default port: 2000  
**To use:**  
$ docker build -t cyclepics .  
$ bash cyclepics.sh   
  
**Dockerfile**: spins up an alpine image, installs pip, cp into container requirements.txt, templates dir, app.py.  
Docker build -t: installs flask via requirements.txt, maps port 2000, and CMD python app.py  
**app.py**: flask py app. randomly cycles through cat images and renders one in a stylised html element  
Import: flask, render_template, random  
**requirements.txt**: app requires a version of flask  
**cyclepics.sh**: docker run docker image called cyclepics  
  
## flaska (depreciated, poor design)  
- Spins up a simple flask app  
  
**Dockerfile**: Spins up an ubuntu image, installs pip, installs flask and uses flask run command for app.py  
**app.py**: outputs "hello flaska!"  

