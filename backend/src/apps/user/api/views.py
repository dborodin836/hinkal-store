from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class ActivateUser(APIView):
    """
    Sends POST request to activate user. This is necessary because activation
    requires POST not GET method.
    """

    # Not quite sure abot the security...
    permission_classes = (AllowAny,)

    def get(self, request, uid, token):
        """
        Sends POST request to the activation url.
        """
        payload = {"uid": uid, "token": token}

        url = "http://localhost:8000/auth/users/activation/"
        response = requests.post(url, data=payload)

        if response.status_code == 204:
            return Response({"message": "OK"}, response.status_code)
        return Response(response.json())
