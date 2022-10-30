# Importing fastAPI and routes 
from fastapi import FastAPI
from routes.user import user

# Including routes too, as this file would start working of the app
app = FastAPI()
app.include_router(user)