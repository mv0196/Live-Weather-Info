from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25, unique=True)
    def __str__(self):
        return self.name.title()

    class Meta:
        verbose_name_plural = 'cities'

class UserData(models.Model):
    Name = models.CharField(max_length = 100)
    Age = models.PositiveIntegerField()
    Email = models.EmailField(max_length = 100)
    Feedback = models.TextField()
    Date = models.DateTimeField(auto_now_add=True, blank=True, editable=True)

    def __str__(self):
        return self.Name
    class Meta:
        verbose_name_plural = 'User Data'
