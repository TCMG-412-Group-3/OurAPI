# OurAPI


Docker hub url: https://hub.docker.com/r/daniul/tcmg-group-3-app/


## To pull our docker image:
docker pull daniul/tcmg-group-3-app:latest


## To run our docker image:

docker run -p 8000:4000 daniul/tcmg-group-3-app:latest


## To run our automated tests:


### To test all API endpoints except for CRUD endpoints, run the following file.
AutomatedTest_p2.py

Keep in mind, the API is accessible at port 8000 on the physical machine (entering localhost:8000 on our chrome browser)

### To test the CRUD API endpoints, complete the following instructions:

#### Create a new Docker network so the server and CLI client can talk to each other (if you don't already have one configured)

```
docker network create mynet
```

#### Run the Redis container image as a server (-d flag runs in the background)

```
docker run --rm --network mynet --name redis-server -d redis
```

#### Run our docker image

```
docker run --rm --network mynet -p 8000:4000 daniul/tcmg-group-3-app:latest
```

#### Now run the following file:

```
AutomatedTest_p3.py
```

