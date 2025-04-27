class Alert:
    def init(self, alert_id: int, title: str, description: str):
        self.alert_id = alert_id
        self.title = title
        self.description = description

    def repr(self):
        return f"Alert(id={self.alert_id}, title='{self.title}', description='{self.description}')"