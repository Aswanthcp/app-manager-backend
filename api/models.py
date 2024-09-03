from django.db import models
from django.conf import settings


class App(models.Model):
    name = models.CharField(max_length=255)
    app_link = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    points = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Task(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to="screenshots/")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.user.username} - {self.app.name}"
