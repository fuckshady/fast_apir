from fastapi import FastAPI, HTTPException
from app.db.redis_conn import get_redis_connection

from app.models.dtos.UserDTOs import UserCreateDTO, UserResponseDTO
from app.models.dtos.AlertDTOs import AlertCreateDTO, AlertResponseDTO

from fastapi import FastAPI

app = FastAPI(
    title="FAST_APIR - User and Alert Management",
    description="API for managing users and their alerts, developed for the third term project.",
    version="1.0.0",
    contact={
        "name": "fuckshady, @juanjo-villa, @keellierr",
        "url": "https://github.com/fuckshady/fast_apir",
        "email": "gonzalez.santiago.3255@eam.edu.co"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    }
)

import json

app = FastAPI()

redis = get_redis_connection()

@app.post("/users/", response_model=UserResponseDTO)
def create_user(user: UserCreateDTO):
    key = f"user:{user.user_id}"
    if redis.exists(key):
        raise HTTPException(status_code=400, detail="User already exists")
    redis.set(key, json.dumps(user.dict()))
    return user

@app.get("/users/{user_id}", response_model=UserResponseDTO)
def get_user(user_id: str):
    key = f"user:{user_id}"
    user_data = redis.get(key)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return json.loads(user_data)

@app.get("/users/", response_model=list[UserResponseDTO])
def list_users():
    keys = redis.keys("user:*")
    users = [json.loads(redis.get(k)) for k in keys]
    return users

@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    user_key = f"user:{user_id}"
    if not redis.exists(user_key):
        raise HTTPException(status_code=404, detail="User not found")
    redis.delete(user_key)
    
    alert_keys = redis.keys("alert:*")
    for alert_key in alert_keys:
        alert_data = json.loads(redis.get(alert_key))
        if alert_data.get("user_id") == int(user_id):  
            redis.delete(alert_key)

    return {"message": f"User {user_id} deleted successfully"}

@app.post("/alerts/", response_model=AlertResponseDTO)
def create_alert(alert: AlertCreateDTO):
    user_key = f"user:{alert.user_id}"
    if not redis.exists(user_key):
        raise HTTPException(status_code=404, detail="Related user does not exist")

    key = f"alert:{alert.alert_id}"
    if redis.exists(key):
        raise HTTPException(status_code=400, detail="Alert already exists")
    redis.set(key, json.dumps(alert.dict()))
    return alert

@app.get("/alerts/{alert_id}", response_model=AlertResponseDTO)
def get_alert(alert_id: str):
    key = f"alert:{alert_id}"
    alert_data = redis.get(key)
    if not alert_data:
        raise HTTPException(status_code=404, detail="Alert not found")
    return json.loads(alert_data)

@app.get("/alerts/", response_model=list[AlertResponseDTO])
def list_alerts():
    keys = redis.keys("alert:*")
    alerts = [json.loads(redis.get(k)) for k in keys]
    return alerts

@app.delete("/alerts/{alert_id}")
def delete_alert(alert_id: str):
    alert_key = f"alert:{alert_id}"
    if not redis.exists(alert_key):
        raise HTTPException(status_code=404, detail="Alert not found")
    redis.delete(alert_key)
    return {"message": f"Alert {alert_id} deleted successfully"}
