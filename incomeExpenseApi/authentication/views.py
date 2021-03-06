from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializers = self.serializer_class(data=user)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        user_data = serializers.data

        return Response(user_data, status=status.HTTP_201_CREATED)
