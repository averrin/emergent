from django.db import models
from django.contrib.auth.models import AbstractUser


class Guild(models.Model):
    name = models.CharField(max_length=40, unique=True, db_index=True)


class Title(models.Model):
    name = models.CharField(max_length=40, unique=True, db_index=True)


class Level(models.Model):
    exp = models.IntegerField()


class Hero(AbstractUser):
    avatar = models.ImageField(upload_to="avatars")

    exp = models.IntegerField(default=0)
    credits = models.IntegerField(default=0)

    titles = models.ManyToManyField(Title)
    guilds = models.ManyToManyField(Guild)

    @property
    def level(self):
        levels = Level.objects.filter(exp__lte=self.exp).order_by('exp').reverse()
        if levels:
            return levels[0]
        else:
            return None
