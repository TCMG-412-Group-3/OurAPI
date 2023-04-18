# OurAPI


Docker hub url: https://hub.docker.com/r/daniul/tcmg-group-3-app/

Docker hub url for CLI: https://hub.docker.com/r/daniul/tcmg-group-3-app-cli/tags


## To pull our docker image:
docker pull daniul/tcmg-group-3-app:latest


## To run our docker image:

docker run -p 8000:4000 daniul/tcmg-group-3-app:latest


## To run our automated tests (before API deployment to GCP):


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

## To run automated tests (with API deployment to GCP):

### Run the following docker command

```
docker run --platform linux/arm64 -it daniul/tcmg-group-3-app:latest sh
```
### Run the following command (replacing the python script with AutomatedTest_p2 or AutomatedTest_p3 respectively.

```
python3 AutomatedTest_p2.py
```
#### or

```
python3 AutomatedTest_p3.py
```

## To run our CLI:

### Pull the following docker image

```
docker pull daniul/tcmg-group-3-app-cli:latest
```
### Run the docker image with the --help flag to see how to use the CLI

#### If on M1/M2 Apple Chip
```
docker run --platform linux/arm64 --rm -it daniul/tcmg-group-3-app-cli:latest --help
```
#### If on other platforms
```
docker run --platform linux/amd64 --rm -it daniul/tcmg-group-3-app-cli:latest --help
````

### Here's an example of how to run the cli via Docker on a M1/M2 chip

```
docker run --platform linux/arm64 --rm -it daniul/tcmg-group-3-app-cli:latest is-prime 23

```



hi
