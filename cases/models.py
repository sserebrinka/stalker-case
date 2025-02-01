from django.db import models


class Cases(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def rarity(self):
        # логика
        return "Rare"

    class Meta:
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'

    def __str__(self):
        return self.name
    

class Items(models.Model):
    case = models.ForeignKey(Cases, related_name='items' ,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    probability = models.FloatField()

    def __str__(self):
        return f'{self.name}, Case: {self.case.name}'