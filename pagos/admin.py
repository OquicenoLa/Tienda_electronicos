from django.contrib import admin
from .models import PaymentMethod, Payment, Transaction, Refund

admin.site.register(PaymentMethod)
admin.site.register(Payment)
admin.site.register(Transaction)
admin.site.register(Refund)

# Register your models here.
