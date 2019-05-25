from .models import Purchase
from .serializers import PurchaseSerializer
from rest_framework import generics
from rest_framework import permissions
from .permissions import PurchaseAuthorization
from rest_framework.throttling import UserRateThrottle


class PurchaseList(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = (permissions.IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PurchaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = (permissions.IsAuthenticated, PurchaseAuthorization,)
    throttle_classes = (UserRateThrottle,)

