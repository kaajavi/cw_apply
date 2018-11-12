# This is the project for Clarity Wave Application


## Infraestructure
I make a Dockerfile for run app, but, we don't use this for production!!!
 
 
 ## How to start.
 0. Install [docker](https://docs.docker.com/install/) 
 and [docker-compose](https://docs.docker.com/compose/install/)
 1. Clone this repo
 1. Config in config/settings.py the domain in ALLOWED_HOSTS variable:
    ```python
    ALLOWED_HOSTS = ['my.domain.com'] #OR ['*'] for all...
    ```  
 1. Build Dockerfile:
     ```bash
    $docker build -t app .
    ```  
 1. Create and run docker container:
    ```bash
    $docker run -d --name=cw_apply -p 5858:80 app
    ```
 1. Create superuser:  
    ```bash
    $docker exec -ti cw_apply /bin/sh
    app/ # ./manage.py createsuperuser //--> and follow steps

    ```
 1. Go to your prefered browser and put http://localhost:5858/ in your navigation bar.
 1. For create questions, go to http://localhost:5858/admin/
 1. Use the system :) 