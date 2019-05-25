from rest_framework import serializers
from purchase.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='user.username')
    purchase_id = serializers.ReadOnlyField(source='id')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Purchase
        fields = [
            'timestamp',
            'purchase_title',
            'purchase_id',
            'user_id',
            'name',
            'phone_number',
            'email',
            'address'
        ]


