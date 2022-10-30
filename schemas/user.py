# Used to Serialize the single object of MongoDB
def userEntity(item) -> dict: 
    return {
        "id": str(item["_id"]), # ["$oid"]
        "name": item["name"],
        "email": item["email"],
        "password": item["password"],
        "skills": item["skills"],
        "experience": item["experience"],
        "experience_in_years": item["experience_in_years"],
        "state": item["state"]
    }


# Used to Serialize multiple objects of MongoDB
def usersEntity(entity) -> list: 
    users = []
    for item in entity:
        users.append(userEntity(item))
    return users