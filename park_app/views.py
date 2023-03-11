from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Ivent, Creater
from .serializers import IventSerializers, CreaterSerializers


class IventCreateListAPIView(ListCreateAPIView):
    queryset = Ivent.objects.all()
    serializer_class =IventSerializers


class IventRetrievUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ivent.objects.all()
    serializer_class =IventSerializers


class CreaterCreateListAPIView(ListCreateAPIView):
    queryset = Creater.objects.all()
    serializer_class = CreaterSerializers

class CreaterRetrievUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Creater.objects.all()
    serializer_class = CreaterSerializers