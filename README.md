## example of rserve, zeppelin, rstudio with api

run a containerized suite of microservices - rserve, rstudio, zeppelin and flask_api for data science use. 

## how to run

- clone and enter repo 
- if on aws with amazon ami: give permissions to `chmod +x install-docker-ec2.sh` and run to install docker
- otherwise install docker and docker-compose manually
- run docker-compose up -d
- run docker ps to make sure services are running
- all services should be running on your host machine
- depending on security settings you should be able to hit http://ec2...com:port

## Scenarios

### Running code and scripts remotely via Rserve
From your client machine, change your address to the remote host:

- run a script via rserve
```
curl -X POST http://localhost:5001/run-script-rserve 

{
  "output": "hello remote client from the server machine!",
}

curl -X POST http://ec2-54-158-104-21.compute-1.amazonaws.com:5001/run-script-rserve 
{
  "output": "hello remote client from the server machine!",
  "status": "success"
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

### Using Zeppelin

Go to `http://ipaddress:8080` and you should see zeppelin interface. You can create, run notebooks. You can also run remote notebooks.

- list all your notebooks on a server
```
curl -s http://localhost:8080/api/notebook | grep -o '{"id":"[^"]*","path":"/Python Tutorial/[^"]*"}'

{"id":"2EYDJKFFY","path":"/Python Tutorial/1. IPython Basic"}
{"id":"2F1S9ZY8Z","path":"/Python Tutorial/2. IPython Visualization Tutorial"}
{"id":"2F2AVWJ77","path":"/Python Tutorial/3. Keras Binary Classification (IMDB)"}
{"id":"2C2AUG798","path":"/Python Tutorial/4. Matplotlib (Python, PySpark)"}
```

- run a notebook after creating it via the api (run by notebook ID - result is data):
```
curl http://localhost:8080/api/notebook/2KMYH5GD9

{"status":"OK","message":"","body":{"paragraphs":[{"text":"import sys\nprint(\"ran notebook\")","user":"anonymous","dateUpdated":"Feb 12, 2025 4:35:50 PM","progress":0,"config":{"editorSetting":{"language":"python","editOnDblClick":false,"completionSupport":true},"colWidth":12.0,"editorMode":"ace/mode/python","fontSize":9.0,"results":{},"enabled":true},"settings":{"params":{},"forms":{}},"results":{"code":"SUCCESS","msg":[{"type":"TEXT","data":"ran notebook\n"}]},"apps":[],"runtimeInfos":{},"progressUpdateIntervalMs":500,"jobName":"paragraph_1739378007739_311101588","id":"paragraph_1739378007739_311101588","dateCreated":"Feb 12, 2025 4:33:27 PM","dateStarted":"Feb 12, 2025 4:35:50 PM","dateFinished":"Feb 12, 2025 4:35:50 PM","status":"FINISHED"},{"user":"anonymous","progress":0,"config":{},"settings":{"params":{},"forms":{}},"apps":[],"runtimeInfos":{},"progressUpdateIntervalMs":500,"jobName":"paragraph_1739378045081_488779603","id":"paragraph_1739378045081_488779603","dateCreated":"Feb 12, 2025 4:34:05 PM","status":"READY"}],"name":"my_python_notebook","id":"2KMYH5GD9","defaultInterpreterGroup":"python","version":"0.10.1","noteParams":{},"noteForms":{},"angularObjects":{},"config":{"isZeppelinNotebookCronEnable":false},"info":{},"path":"/my_python_notebook"}}%                                                                                  

```

- you can also run a specific paragraph from a notebook:

```
http://[zeppelin-server]:[zeppelin-port]/api/notebook/job/[notebookId]/[paragraphId]
```


### Use Rstudio server

Go to `http://ipadress::8888` and you should see rstudio workbench open source for use.