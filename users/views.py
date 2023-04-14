from django.shortcuts import get_object_or_404, render
from users.serializer import UserSerializer
from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticated
from users.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permission import IsEmployeeOrSameUserOrReadOnly

# Create your views here.


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            UserSerializer(instance=user).data, status=status.HTTP_201_CREATED
        )


class UserViewDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsEmployeeOrSameUserOrReadOnly]

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
