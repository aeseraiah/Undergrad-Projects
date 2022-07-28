# AI Prediction Microservice

For this microservice, a classification of beans can be performed based on input data via the REST API. Given a file as input to the model, it will allow the users to:

-  /list: List the list_files
- /file: Upload and Download files
- /predict: Upload a file that will be used to predict bean classes 
- /explanation: Upload a file that will be used to produce the model's metrics 

### Running the service;

1. In VM, navigate to the Lab 11/my_work directory
2. Build the containerized service in VM.
```
make docker-build
```
3. Go inside of container 
```
make docker-interactive
```
4. Create and run the service
```
make docker-start
```

5. From the browser in your local machine, navigate to
```
http://vm-148-28.ise.luddy.indiana.edu:11000/e222/ui

```
You should be able to see the endpoints listed above.

#### Cleaning up
Once you are done using the container, make sure to clean the environment using the following.

Stop the container
```
make docker-stop
```

Clean the docker environment
```
make docker-clean
```
