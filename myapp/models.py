from django.db import models

# Create your models here.
class Names(models.Model):
    name = models.CharField(max_length=200)

    def new_method(self):
        return self.name + " " + str(self.pk)