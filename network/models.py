from django.db import models
from users.models import CustomUser  # Импортируем CustomUser

class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.model}"

class Network(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, related_name='networks')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='customers')
    debt = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    creation_time = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField(default=0) #Уровень иерархии

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Автоматическое определение уровня
        if self.supplier:
            self.level = self.supplier.level + 1
        else:
            self.level = 0
        super().save(*args, **kwargs)