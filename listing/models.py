from django.db import models
from django.contrib.auth.models import User
from accounts.models import Skill, City

class Problem(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(User)
    skills = models.ManyToManyField(Skill, null=True, blank=True)
    added_date = models.DateTimeField(auto_now=True)
    city = models.ForeignKey(City, null=True)

    class Meta:
        verbose_name = 'problem'
        verbose_name_plural = 'problems'

    def __unicode__(self):
        return self.title


from django.forms import ModelForm

class ProblemForm(ModelForm):
    class Meta:
        model = Problem
        exclude = ('user','added_date')