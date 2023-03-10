# About Project
- This application APIs build using FastAPI. In this application, data of employees with details can be fetched, updated, created and deleted using different request methods (GET, POST, PATCH, DELETE) in the MongoDB server. 
- Different sections of project involved - creating models (which is defining database structure of MongoDB), routes (creating routing URLS), configuration (connecting application to MongoDB server) & defining schemas (i.e to convert data to simplest form to be understood in frontend).

## [API Collection Demo](https://employee-info-fastapi.herokuapp.com/docs)

### Steps to setup and start the project locally:
1. Fork and clone the repository
2. Run `pip install virtualenv` and then command `virtualenv venv` to create your local environment for the project 
3. Run `pip install -r requirements.txt` to install all the dependencies
4. The project would be up and running by command `uvicorn main:app --reload`.


 Else you can refer to this link to run and test the APIs: https://web-production-affd.up.railway.app/docs
