from locust import HttpUser, task
            
class User(HttpUser):
    @task
    def get_home_route(self):
        self.client.get('/')
    @task
    def post_prediction(self):
        self.client.post('/predict',json=input_data)
