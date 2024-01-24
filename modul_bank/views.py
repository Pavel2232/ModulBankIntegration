from rest_framework import viewsets
from modul_bank.models import Bank
from modul_bank.serializers import BankSerializers


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializers
