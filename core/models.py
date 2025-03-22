from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100, null=True)
    bank_name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    address = models.TextField()
    telephone = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="media/", blank=True)
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "People"
        ordering = ["-joined"]
