from locust import SequentialTaskSet, HttpUser, task, constant


class TestCase(SequentialTaskSet):

    @task
    def TC_001(self):
        with self.client.get("/", catch_response=True) as response:
            if response.text != "Success":
                response.failure("Got wrong response")
            elif response.elapsed.total_seconds() > 0.5:
                response.failure("Request took too long")

    @task
    def TC_002(self):
        with self.client.get("/top/up", catch_response=True) as response:
            if response.text != "Success":
                response.failure("Got wrong response")
            elif response.elapsed.total_seconds() > 0.5:
                response.failure("Request took too long")

    @task
    def TC_003(self):
        with self.client.post("/login", {"username": "hamburg@gmail.com", "password": "H@8790"}) as response:
            if response.text != "Success":
                response.failure("Entered wrong credential")
            elif response.elapsed.total_seconds() > 0.5:
                response.failure("Entered wrong credential")


class MyTest(HttpUser):
    wait_time = constant(1)
    host = "https://bikroy.com/"
    wait_time = constant(1)
    wait_time = constant(1)
    tasks = [TestCase]

# with self.client.get("/") as response:
# print(response.status_code)
# if "Welcome to Bikroy.com" in response.text and response.elapsed.total_seconds() < 10.0:
# response.success()
# logging.info("Home Page load success")
# else:
# response.failure("Home page took too long to load and/or text check has failed.")
# logging.error("Home page didn't load successfully.")


# self.client.post("/login", {"username":"admin", "password":"admin"}
