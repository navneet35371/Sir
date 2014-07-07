#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
sys.path.append('/home/sss/test1/app1/libp')
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from spell_mean import *
from app1.models import *
from django.template import RequestContext
from django.shortcuts import redirect
# Create your views here.

def hello(request):
	name = 'Navneet'
	html = "<html><body>Hi %s, this seems to have worked!</body></html>" % name
	return HttpResponse(html)

def hello_template(request):
	name = 'Navneet suman'
	t = get_template('hello.html')
	html = t.render(Context({'name' : name}))
	return HttpResponse(html)

def hello_simple(request):
	name = request.build_absolute_uri(None)
	name = name[24:]
	name = query(str(name))
	return render_to_response('hello.html',{'name' : name})

def home(request):
	if request.method == 'POST':
		#name = form1(request.POST)
		#data = name.cleaned_data
		query = request.POST['query1']
		return redirect('/q='+query)
	else:
		name = 'Navneet'
	return render_to_response('index.html',{'name' : name},context_instance=RequestContext(request))
