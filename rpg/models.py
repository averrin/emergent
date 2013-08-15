from django.db import models
from django.contrib.auth.models import AbstractUser


class Guild(models.Model):
    name = models.CharField(max_length=40, unique=True, db_index=True)


class Title(models.Model):
    name = models.CharField(max_length=40, unique=True, db_index=True)


class Level(models.Model):
    exp = models.IntegerField()


class Hero(AbstractUser):
    avatar = models.ImageField(upload_to="avatars", null=True)

    exp = models.IntegerField(default=0)
    credits = models.IntegerField(default=0)

    titles = models.ManyToManyField(Title, null=True)
    guilds = models.ManyToManyField(Guild, null=True)

    @property
    def level(self):
        levels = Level.objects.filter(exp__lte=self.exp).order_by('exp').reverse()
        if levels:
            return levels[0]
        else:
            return None

    @property
    def level_no(self):
        if self.level is not None:
            return self.level.id
        else:
            return 0

    @property
    def next_level(self):
        next_lvl = Level.objects.filter(pk=int(self.level_no) + 1)
        if next_lvl.exists():
            return next_lvl[0]
        else:
            return self.level

    @property
    def exp_percentage(self):
        if self.exp:
            return int((float(self.exp) / float(self.next_level.exp)) * 100)
        else:
            return 0
