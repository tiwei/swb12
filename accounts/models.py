from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from social_auth.signals import socialauth_registered


class Country(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100, blank=True, null=True)


class City(models.Model):
    name = models.CharField(max_length=100)


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    country = models.ForeignKey(Country, null=True)
    city = models.ForeignKey(City, null=True)
    skills_offered = models.ManyToManyField(Skill, related_name='offered_set')
    skills_wanted = models.ManyToManyField(Skill, related_name='wanted_set')

    def __unicode__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        # country = Country.objects.get_or_create(name=)
        # 

post_save.connect(create_user_profile, sender=User)


def fill_user_profile(sender, user, response, details, **kwargs):
    if 'skills' in response and 'skill' in response['skills']:
        profile = user.get_profile()
        for sk in response['skills']['skill']:
            skill = Skill.objects.get_or_create(name=sk['skill']['name'])
            print skill
            profile.skills_offered.add(skill)

socialauth_registered.connect(fill_user_profile)
