from django.db import models

# Create your models here.
class it_is_fine(models.Model):
    field1_e = models.CharField(max_length=1000)
    field2_p = models.CharField(max_length=10000)
    captured_time = models.DateTimeField(auto_now=True)

    