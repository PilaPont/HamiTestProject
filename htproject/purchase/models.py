from django.db import models
from phonenumber_field.modelfields import PhoneNumberField  # to validate phone numbers
from django.core.validators import validate_email  # to validate emails


class Purchase(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    purchase_title = models.CharField(max_length=150)
    user = models.ForeignKey('auth.User', related_name='purchases', on_delete=models.PROTECT)
    phone_number = PhoneNumberField()
    email = models.EmailField(blank=False)
    address = models.TextField(null=True, blank=True)

