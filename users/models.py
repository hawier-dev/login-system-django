from django.db import models


class Person(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password1 = models.CharField(max_length=65)
    password2 = models.CharField(max_length=65)

    def __repr__(self):
        return f"User named '{self.username}'"

    def __str__(self):
        return self.username
