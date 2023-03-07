# OurAPI


Docker hub url: https://hub.docker.com/r/daniul/tcmg-group-3-app/


To pull our docker image:
docker pull daniul/tcmg-group-3-app:v4


To run our docker image:

docker run -p 8000:4000 daniul/tcmg-group-3-app:v4


To run our automated tests:

first, run a docker image via the command above, and then run the following python script:


AutomatedTest_p2.py

Keep in mind, the API is accessible at port 8000 on the physical machine (entering localhost:8000 on our chrome browser)



(AutomatedTest.py was our initial work but we created a new file for our final submission)
