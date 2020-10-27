from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    @task(3)
    def datadog_index(self):
        self.client.get("/sample")

    @task(1)
    def view_item(self):
        # item_id = random.randint(1, 10000)
        # self.client.get(f"/item?id={item_id}", name="/item")
        self.client.get("/sample/hello.jsp")
        self.client.get("/sample/hello")