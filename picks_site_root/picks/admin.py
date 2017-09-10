# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Picker, Pick

# Register your models here.

admin.site.register(Picker)
admin.site.register(Pick)