from django.db import models


class Cases(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_content(self):
        return [item.name for item in self.items.all()]

    class Meta:
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'

    def __str__(self):
        return self.name
    

class Items(models.Model):
    RARITY_CHOICES = [
        ('Ordinary', 'Ordinary'),
        ('Rare', 'Rare'),
        ('Epic', 'Epic'),
        ('Mythical', 'Mythical'),
        ('Legendary', 'Legendary'),
    ]

    case = models.ForeignKey(Cases, related_name='items' ,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=50, choices=RARITY_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    probability = models.FloatField()

    def get_probability(self):
        return f"{self.probability * 100:.2f}%"

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return f'{self.name}, Case: {self.case.name}'