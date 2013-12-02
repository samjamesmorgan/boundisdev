from django.db import models

class sport(models.Model):
    CATEGORY_CHOICES = (
        ('ball', 'Ball games'),
        ('beach', 'Beach sports'),
        ('combat', 'Combat sports'),
        ('disabled', 'Disabled sports'),
        ('extreme', 'Extreme sports'),
        ('individual', 'Individual sports'),
        ('motorsport', 'Motorsport'),
        ('water', 'Water sports'),
        ('winter', 'Winter sports'),
    )
    name = models.CharField(max_length=70, unique=True)
    min_participants = models.IntegerField()
    max_participants = models.IntegerField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    def __unicode__(self):
          return self.name