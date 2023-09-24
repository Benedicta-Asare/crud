from fastapi.exceptions import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

app = FastAPI()

# In-memory database for demonstration purposes
users_db = {}

@app.post("/api/create_user", response_model=User)
def create_user(user: User):
    users_db[user.id] = user
    return user

@app.get("/api/get_user/{user_id}", response_model=User)
def get_user(user_id: int):
    user = users_db.get(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.put("/api/update_user/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    if user_id in users_db:
        users_db[user_id] = user
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/api/delete_user/{user_id}")
def delete_user(user_id: int):
    if user_id in users_db:
        del users_db[user_id]
        return {"message": f"User with ID {user_id} deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
