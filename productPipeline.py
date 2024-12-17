import time
from datetime import datetime, timedelta
import threading
from abc import ABC, abstractmethod
from depoymentServices import DeploymentFactory
from notificationServices import NotificationChannel
from logging_module import log



@dataclass
class Product:
    name: str
    scheduled_time: str
    target_types: list
    notification_channels: list
    

    @log
    def build(self):
        print(f"[{datetime.now()}] Building product: {self.name}")

    
    @log
    def deploy(self):
        for target_type in self.target_types:
            target = DeploymentFactory.get_target(target_type) # We use the  factory pattern to create deploy on different repos in runtime
            target.deploy(self.name)
    @log
    def notify(self):
        for channel in self.notification_channels: # Here we add channel notification as composition mode in the product class..
            channel.notify(self.name)



# Pipeline class
class Pipeline:
    def __init__(self, product):
        self.product = product

    def run(self):
        try:
            print(f"\n[{datetime.now()}] Starting pipeline for product: {self.product.name}")
            self.product.build()
            self.product.deploy()
            self.product.notify()
            print(f"[{datetime.now()}] Pipeline completed for product: {self.product.name}")
        except Exception as e:
            print(f"[ERROR] Pipeline failed:  {self.product.name}: {e}")
            return 


# Function to schedule pipelines daily
def schedule_pipeline(product):
    while True:
        now = datetime.now()
        scheduled_time = datetime.strptime(product.scheduled_time, "%H:%M").replace(
            year=now.year, month=now.month, day=now.day
        )
        
        # Schedule for next day if time has passed
        if now > scheduled_time:
            scheduled_time += timedelta(days=1)
        
        wait_time = (scheduled_time - now).total_seconds()
        print(f"[{datetime.now()}] Scheduled pipeline for {product.name} at {product.scheduled_time}. Waiting {wait_time} seconds...")
        time.sleep(wait_time)
        
        pipeline = Pipeline(product)
        pipeline.run()



# entry point..
def main():
    # Define notification channels
    mail = NotificationChannel("Mail")
    slack = NotificationChannel("Slack")

    # Define products and their pipelines
    products = [
        Product(name="Product_A", scheduled_time="14:30", target_types=["Artifactory", "S3"], notification_channels=[mail]),
        Product(name="Product_B", scheduled_time="15:00", target_types=["Nexus"], notification_channels=[slack, mail]),
    ]

    # Schedule pipelines in separate threads
    threads = []
    for product in products:
        thread = threading.Thread(target=schedule_pipeline, args=(product,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
