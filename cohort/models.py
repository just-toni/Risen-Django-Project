from django.db import models

# Create your models here.

class Cohort(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
