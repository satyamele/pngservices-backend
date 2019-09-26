from rest_framework import permissions
from rest_framework import viewsets
from dashboard.models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
