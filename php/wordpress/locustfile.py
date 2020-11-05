import random

from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    @task(3)
    def datadog_index(self):
        self.client.get("/wp-admin/index.php")

    @task
    def datadog_error(self):
        self.client.get("/error")

    @task(5)
    def view_api(self):
        self.client.get("/wp-admin/edit.php?post_type=page")