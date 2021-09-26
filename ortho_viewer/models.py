from django.db import models

class Orthoimage(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image/')
    

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
