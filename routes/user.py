from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User
from collections import namedtuple
user = APIRouter()



@user.get("/")
async def read_data():
    result = conn.execute(users.select()).fetchall()
    print(result)
    column_names = users.columns.keys()
    # Convert the query result to a list of dictionaries
    users_list = [dict(zip(column_names, user)) for user in result]
    
    print(users_list)
    return users_list


@user.get("/{id}")
async def read_data(id: int):
    UserRow = namedtuple("UserRow", users.columns.keys())
    
    # Fetch the data from the database
    data = conn.execute(users.select().where(users.c.id == id)).fetchone()
    
    if data:
        # Create a named tuple using the fetched data
        user_namedtuple = UserRow(*data)
        
        # Convert the named tuple to a dictionary
        user_dict = user_namedtuple._asdict()
        
        # Print the converted data
        print("Converted data:", user_dict)
        return user_dict
    else:
        print("No data found for id:", id)
        return {"No data found for id:", id}


@user.post("/")
async def write_data(user : User):
    try:
        # Your logic to insert the user into the database
        conn.execute(users.insert().values(
            name=user.name,
            email=user.email,
            password=user.password
        ))
        conn.commit() 
        return {"message": "User created successfully"}
    except Exception as e:
        # Handle exceptions appropriately, log, and return an HTTP error response
        return {"error": str(e)}

@user.put("/{id}")
async def update_data(id : int, user : User):
    try:
        conn.execute(users.update().values(
            name=user.name,
            email=user.email,
            password=user.password 
        ).where(users.c.id == id))
        conn.commit()
        return {"message": "User created successfully"}
    except Exception as e:
        # Handle exceptions appropriately, log, and return an HTTP error response
        return {"error": str(e)}

@user.delete("/{id}")
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    conn.commit()
    return {"message": "User Deleted successfully"}

