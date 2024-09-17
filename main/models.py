import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    jersey_name = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()


    @property
    def is_mood_strong(self):
        return self.price > 5