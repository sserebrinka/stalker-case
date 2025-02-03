from django.db import models
from django.contrib.auth.models import User
from cases.models import Cases, Items


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/profile_images/', blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cases = models.ManyToManyField(Cases, blank=True)
    items = models.ManyToManyField(Items, blank=True)

    class Meta:
        db_table = 'Profile'
    
    def __str__(self):
        return f'{self.user.username} Profile'
