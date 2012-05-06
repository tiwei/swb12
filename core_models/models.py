'''
Currently these models are not in use
'''


from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    """Stores information about a skill"""
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'

    def __unicode__(self):
        return self.name


class UserProfile2(models.Model):
    user = models.OneToOneField(User, unique=True)
    location = models.ForeignKey('Location', default='Berlin')
    contacts = models.ManyToManyField('self', null=True, blank=True)
    # skill = models.ManyToManyField(Skill, null=True, blank=True, through='SkillDetails')  # doesn't work
    company = models.ForeignKey('Company', null=True, blank=True)
    #pic = URLField()
    #wanted_skill = models.ManyToManyField('Skill', null=True, blank=True)

    class Meta:
        verbose_name = 'userprofile'
        verbose_name_plural = 'userprofiles'

    def __unicode__(self):
        return self.user


class Company(models.Model):
    name = models.CharField(max_length=30)



class SkillDetails(models.Model):
    STATUS_CHOICES = (('wanted','wanted'),('offered','offered'))
    user = models.ForeignKey(User)
    skill = models.ForeignKey('Skill')
    status = models.CharField(choices = STATUS_CHOICES, max_length=20)
    counter = models.PositiveIntegerField(default=0)


class Problem(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(User)
    skills = models.ManyToManyField(Skill, null=True, blank=True)
    #date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'problem'
        verbose_name_plural = 'problems'

    def __unicode__(self):
        return self.title



COUNTRIES = (
    ('DE', 'Germany'),
    ('US', 'United States'),
    ('CL', 'Chile'),
)


class Location(models.Model):
    """Stores information about the location of a user"""
    country = models.CharField(max_length=1, choices=COUNTRIES)
    city = models.CharField(max_length=20, null=True, blank=True)
    zip_code = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    slug = models.SlugField(max_length=20)

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'

    def __unicode__(self):
        return u'%s_%s' % (self.country, self.city)


class Feedback(models.Model):
    """Stores information about a feedback interaction between users."""
    text = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = 'feedback'
        verbose_name_plural = 'feedbacks'

    def __unicode__(self):
        return self.rating
