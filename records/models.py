from django.db import models

class Record(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id}--{self.name}"