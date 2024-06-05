import requests
from django.http import JsonResponse
from .models import Task

class OPALAuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/tasks/'):
            user = request.user
            task_id = request.GET.get('id')

            # Get task owner_id from database
            task_owner_id = Task.objects.get(id=task_id).owner_id

            # Create the input for the policy
            input_data = {
                "user": {
                    "id": user.id,
                    "role": user.role
                },
                "task": {
                    "owner_id": task_owner_id
                }
            }

            # Call OPA for authorization
            response = requests.post(
                'http://localhost:8181/v1/data/todo/allow',
                json={"input": input_data}
            )

            result = response.json().get('result')

            if not result:
                return JsonResponse({"error": "Unauthorized"}, status=403)

        response = self.get_response(request)
        return response
