# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import File,College
admin.site.register(File)

class CrAdm(admin.ModelAdmin):
    list_display=['cname','clgcode','address','phone','principal']
admin.site.register(College,CrAdm)
# Register your models here.
