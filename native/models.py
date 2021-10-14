from django.db import models

# Create your models here.
from cohort.models import Cohort


class Native(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    scvn = models.CharField(max_length=10, null=True)
    image = models.ImageField(upload_to= "image/")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name