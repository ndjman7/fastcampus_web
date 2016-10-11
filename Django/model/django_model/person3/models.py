from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    relationships = models.ManyToManyField('self', through ='relationship',symmetrical=False, related_name='related_to+')

RELATIONSHIP_FOLLWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)

class Relationship(models.Model):
        from_person = models.ForeignKey(Person, related_name='from_people')
        to_person = models.ForeignKey(Person, related_name='to_people')
        status = models.IntegerField(choices=RELATIONSHIP_STATUSES)
