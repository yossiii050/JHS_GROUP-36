from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Set the flag to False by default
        self.maintenance_mode = False

    def process_request(self, request):
        if self.maintenance_mode:
            # Set a flag in the request object to indicate that the site is in maintenance mode
            request.maintenance_mode = True
            print(f'maintenance_mode set to {request.maintenance_mode}')
        else:
            request.maintenance_mode = False
            print(f'maintenance_mode set to {request.maintenance_mode}')

    def __call__(self, request):
        response = self.get_response(request)
        return response
