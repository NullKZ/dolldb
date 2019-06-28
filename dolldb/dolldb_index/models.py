from django.db import models

# Create your models here.

class doll(models.Model):
    DOLL_TYPES = (
        ('AR','AR'),
        ('RF','RF'),
        ('MG','MG'),
        ('HG','HG'),
        ('SG','SG'),
        ('SMG','SMG'),
    )
    RARITIES = (
        (5,'★★★★★'),
        (4,'★★★★'),
        (3,'★★★'),
        (2,'★★'),
        (1,'⚝'),
    )
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32, choices=DOLL_TYPES)
    rarity = models.PositiveSmallIntegerField(choices=RARITIES)