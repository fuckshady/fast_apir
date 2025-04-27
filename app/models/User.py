from app.models.Alert import Alert

class User:
    def init(self, user_id: int, username: str, email: str, alerts=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.alerts = alerts if alerts is not None else []  

    def add_alert(self, alert: Alert):
        self.alerts.append(alert)

    def repr(self):
        return f"User(id={self.user_id}, username='{self.username}', email='{self.email}', alerts={self.alerts})"