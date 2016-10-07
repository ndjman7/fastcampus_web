from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
            ('S','Small'),
            ('M','Medium'),
            ('L','Large'),
        )
    GENDER = (
            ('','모름'),
            ('m','남성'),
            ('f','여성'),
        )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    gender = models.CharField(max_length=1, choices=GENDER, blank=True)
