# Week 10 Lab: File Management Service

**In this lab you will:** learn to managing files via the REST API

**After the end of this lab you should:** understand file manipulation through a REST API

In this Lab we will be running looking at file management in via the REST API.
It will allow the users to:

-  /list: List the list_files
- /file: Upload and Download files

### Introducing the files
There are 2 changes in this lab compared to the previous. This is to allow file manipulation functions (backend) and their corresponding REST endpoints (yaml file).
```
file_api.yml: file manager specification
src/file.py: python functions corresponding to the api endpoints
```

Look at the file_api.yml file to understand the endpoints available in this service.

### Running the service

1. Navigate to the Lab 6 directory
2. Let's build the service.
```
make docker-build
```
3. Run the service
```
make docker-start
```

4. From the browser in your local machine, navigate to
```
vm-148-X.ise.luddy.indiana.edu:11000/e222/list
```
You should be able to see the files in the current server directory listed.

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

#### Try the UI out
Do some googling and see if you can figure out how to access the Swagger UI endpoint. 
