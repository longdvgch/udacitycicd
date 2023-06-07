from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Time between consecutive tasks
    
class MyUser(HttpUser):
    wait_time = between(1, 3)  # Time between consecutive tasks

    @task
    def my_task(self):
        self.client.get("/path/to/endpoint")  # Perform a GET request

