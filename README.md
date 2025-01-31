# example of communication with rserve server

run a containerized rserve inside your local machine that you can then connect with to trigger remote script running or send commands -- in this case we have a script called `my_script.R` which gets mounted as a volume when the container is created.

# how to run

- install docker
- intall docker-compose
- enable any permissions needed
- clone and enter repo
- run docker-compose up -d
- run docker ps to make sure services are running
- make sure you have python installed
- now run the `.py` files in `tests` (triggering remote script not running yet, flask api is alternative)

