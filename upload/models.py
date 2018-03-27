# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class File(models.Model):
    file=models.FileField(blank=False,null=False)
    remark=models.CharField(max_length=20)
    timestamp=models.DateTimeField(auto_now_add=True)
class College(models.Model):
    cname=models.CharField(max_length=200)
    clgcode=models.CharField(max_length=20)
    address=models.CharField(max_length=150)
    phone=models.CharField(max_length=20)
    principal=models.CharField(max_length=30)