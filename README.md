## example of rserve, zeppelin, rstudio with api

run a containerized suite of microservices - rserve, rstudio, zeppelin and flask_api for data science use. 

## how to run

- clone and enter repo 
- if on aws: give permissions to `chmod +x install-docker.sh` and run to install docker
- otherwise install docker and docker-compose manually
- run docker-compose up -d
- run docker ps to make sure services are running
- all services should be running on your host machine

## Scenarios

### Running code and scripts remotely via Rserve
From your client machine, change your address to the remote host:

- run a script via rserve
```
curl -X POST http://localhost:5001/run-script-rserve 

{
  "output": "hello remote client from the server machine!",
}
```

- send code remotely
```
curl -X POST http://localhost:5001/run-command-rserve \
     -H "Content-Type: application/json" \
     -d '{"r_code": "rnorm(10)"}'

{
  "output": [
    0.11778101020595771,
    0.3623573204499772,
    -0.7231324356359029,
    -0.04992651570409085,
    0.4960848304174492,
    -0.6608921776129493,
    -0.3384682709227272,
    -0.3318572535962269,
    2.0463444645440387,
    -0.4238149643245366
  ],
  "status": "success"
}

```

### Use Zeppelin

Go to `http://ipaddress:8080` and you should see zeppelin interface. You can create, run notebooks. You can also run remote notebooks.

### Use Rstudio server

Go to `http://ipadress::8888` and you should see rstudio workbench open source for use.