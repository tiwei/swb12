from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class Country(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)


class City(models.Model):
    name = models.CharField(max_length=100)


class Skill(models.Model):
    name = models.CharField(max_length=100)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    country = models.ForeignKey(Country)
    city = models.ForeignKey(City)
    skills_offered = models.ManyToManyField(Skill, related_name='offered_set')
    skills_wanted = models.ManyToManyField(Skill, related_name='wanted_set')

    def __unicode__(self):
        return self.user


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print dir(instance)
        

post_save.connect(create_user_profile, sender=User)
