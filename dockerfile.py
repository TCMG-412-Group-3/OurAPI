# specify the base image
FROM python:3.8-slim-buster

# set the working directory
WORKDIR /app

# copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the Flask app code
COPY . /app

# expose the port on which the app runs
EXPOSE 5000 # or 80? im not too sure

# do we need to define environment variable
# ENV NAME World ??

# set the app's entry point
CMD ["python", "app.py"]

# you can build the Docker image by running the following command in the project directory: "docker build -t flask-app ."
# to run the Docker container, you can use the following command: "docker run -p 5000:5000 flask-app"
# you can push the Docker image to the Docker public repository using the docker push command: "docker push username/flask-app"
