# Notification Channel class
class NotificationChannel:
    def __init__(self, name):
        self.name = name

    def notify(self, product_name):
        print(f"[{datetime.now()}] Notifying via {self.name} for product: {product_name}")