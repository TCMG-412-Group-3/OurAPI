# specify the base image
FROM python:3.10-slim-buster

RUN rm -rf /app

# set the working directory
WORKDIR /app


# copy current directory contents into app directory and install dependencies
COPY . /app


RUN pip install --trusted-host pypi.python.org -r requirements.txt

# expose the port on which the app runs
EXPOSE 4000

# do we need to define environment variable
# ENV NAME World ??

# set the app's entry point
CMD ["python", "main.py"]

# you can build the Docker image by running the following command in the project directory: "docker build -t flask-app ."
# to run the Docker container, you can use the following command: "docker run -p 4000:80 flask-app"
# you can push the Docker image to the Docker public repository using the docker push command: "docker push username/flask-app"
