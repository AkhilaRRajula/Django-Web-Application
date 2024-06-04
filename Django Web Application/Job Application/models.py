from django.db import models

class Form(models.Model):
    first_name = models.CharField(max_length=80)
    middle_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    date = models.DateField()
    occupation = models.CharField(max_length=80)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
