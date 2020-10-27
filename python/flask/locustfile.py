import random

from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    @task(3)
    def datadog_index(self):
        self.client.get("/")

    @task
    def datadog_error(self):
        self.client.get("/error")

    @task(5)
    def view_post(self):
        post_id = random.randint(1, 10000)
        self.client.get(f"/api/post/{post_id}", name="/api/post/")