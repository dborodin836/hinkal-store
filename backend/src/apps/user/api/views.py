from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class ActivateUser(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, uid, token):
        payload = {"uid": uid, "token": token}

        url = "http://localhost:8000/auth/users/activation/"
        response = requests.post(url, data=payload)

        if response.status_code == 204:
            return Response({}, response.status_code)
        else:
            return Response(response.json())
