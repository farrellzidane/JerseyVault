import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jersey_name = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()


    @property
    def is_mood_strong(self):
        return self.price > 5