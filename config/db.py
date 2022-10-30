# Importing MongoClient to use MongoDB Atlas  
from pymongo import MongoClient

# Connection is defined with connection string from MongoDB Atlas 
conn = MongoClient("mongodb+srv://sonal:sonal@cluster0.bfxfu.mongodb.net/?retryWrites=true&w=majority") # cluster in double quotes

