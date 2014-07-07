#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.db import models
from django import forms

# Create your models here.
class search(models.Model):
	query = models.CharField(max_length=200)
	que_time = models.DateTimeField('date of query')

class form1(forms.Form):
	query1 = forms.CharField(max_length=100)