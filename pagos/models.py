from djongo import models

class PaymentMethod(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Payment(models.Model):
    STATUS = [
        ('pending', 'Pendiente'),
        ('completed', 'Completado'),
        ('failed', 'Fallido'),
    ]
        
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    # orden = models.OneToOneField('carrito_pedidos.Orden', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.orden:
            self.total = self.orden.total
        super().save(*args, **kwargs)

    def update_status(self):
        successful_transaction = self.transactions.filter(status='completed').exists()
        if successful_transaction:
            self.status = 'completed'
            self.save()

    def _str_(self):
        return f"{self.user} - {self.total} - {self.status}"         

class Transaction(models.Model):
    STATUS = [
        ('pending', 'Pendiente'),
        ('completed', 'Completado'),
        ('failed', 'Fallido'),
    ]

    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name="transactions")
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.payment.update_status()

    def __str__(self):
        return f"Transacción {self.transaction_id} - {self.status}"
    
class Refund(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reembolso de {self.amount} por {self.reason}"
    

