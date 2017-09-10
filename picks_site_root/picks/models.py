# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Picker(models.Model):
    name = models.CharField(max_length=30)
    league = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Pick(models.Model):
    year = models.IntegerField(default=2017)
    week = models.IntegerField(default=1)
    picker = models.ForeignKey(Picker)
    team = models.CharField(max_length=30)
    is_offpick = models.BooleanField(default=False)
    is_correct = models.BooleanField(default=False)
    time_entered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.year + "/WK " + self.week + " - " + self.team

# class Games(models.Model):
#     year = models.IntegerField()
#     week = models.IntegerField()
#     home_team = models.CharField(max_length=30)
#     away_team = models.CharField(max_length=30)
#     favored = models.NullBooleanField()
#     favored_amount = models.DecimalField(max_digits=3, decimal_places=1)