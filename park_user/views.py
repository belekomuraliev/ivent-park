
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import IventUser, User
from .serializers import AuthorSerializer


class AuthorRegisterAPIView(ListCreateAPIView):
    queryset = IventUser.objects.all()
    serializer_class = AuthorSerializer

