# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from datetime import datetime
import nflgame

# Create your views here.


def index(request):
    week = (datetime.now() - datetime(year=2017, month=9, day=1)).days/7
    return week_view(request, week)


def week_view(request, week_number=1):
    year = datetime.now().year
    games = nflgame.live._games_in_week(year, week=week_number, kind="REG")
    context = {
        'games': games,
    }

    return render(request, 'picks/picks.html', context)
