from fastapi import FastAPI, HTTPException
from app.db.redis_conn import get_redis_connection
from app.models.User import User
from app.models.Alert import Alert
import json

app = FastAPI()

redis = get_redis_connection()


@app.post("/users/")
def create_user(user: User):
    key = f"user:{user.id}"
    if redis.exists(key):
        raise HTTPException(status_code=400, detail="User already exists")
    redis.set(key, json.dumps(user.dict()))
    return {"message": "User successfully created"}

@app.get("/users/{user_id}")
def get_user(user_id: str):
    key = f"user:{user_id}"
    user_data = redis.get(key)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return json.loads(user_data)

@app.get("/users/")
def list_users():
    keys = redis.keys("user:*")
    users = [json.loads(redis.get(k)) for k in keys]
    return users

@app.post("/alerts/")
def create_alert(alert: Alert):
    user_key = f"user:{alert.usuario_id}"
    if not redis.exists(user_key):
        raise HTTPException(status_code=404, detail="Related user does not exist")

    key = f"alert:{alert.id}"
    if redis.exists(key):
        raise HTTPException(status_code=400, detail="Alert already exists")
    redis.set(key, json.dumps(alert.dict()))
    return {"message": "Alert successfully created"}

@app.get("/alerts/{alert_id}")
def get_alert(alert_id: str):
    key = f"alert:{alert_id}"
    alert_data = redis.get(key)
    if not alert_data:
        raise HTTPException(status_code=404, detail="Alert not found")
    return json.loads(alert_data)

@app.get("/alerts/")
def list_alerts():
    keys = redis.keys("alert:*")
    alerts = [json.loads(redis.get(k)) for k in keys]
    return alerts
