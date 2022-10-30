# Importing BaseModel from pydantics to inherit BaseeModel to define object
from pydantic import BaseModel

# Defining emp objects or emp collection for MongoDB
class emp(BaseModel):
    name: str
    email: str
    password: str
    skills: str
    experience: str 
    experience_in_years: int 
    state: str



