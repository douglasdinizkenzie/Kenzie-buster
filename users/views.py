from django.shortcuts import render
from users.serializer import UserSerializer
from rest_framework.views import APIView, Request, Response, status

# Create your views here.


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            UserSerializer(instance=user).data, status=status.HTTP_201_CREATED
        )
