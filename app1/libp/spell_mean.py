#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib2,html5lib,json,re,binascii
from app1.libp.google import *
#from gviz_api import *
import ordereddict
import HTMLParser

from flask import json
from flask import Flask
from flask import request
from flask import render_template
import unirest
#from google import Google
a = ''  


def duck(keyword):
	response = unirest.get("https://duckduckgo-duckduckgo-zero-click-info.p.mashape.com/?q="+keyword+"&callback=process_duckduckgo&no_html=1&no_redirect=1&skip_disambig=1&format=json",
headers={
   	"X-Mashape-Authorization": "nEqbg6i8Cxo2xN3wSScbRmnL9h1gCgSb"
}
);
	return response.body

def asciirepl(match):
	return ''
def emrepl(match):
	return ''


def query(keyword):
	keyword.replace(" ", "+")
	word_meaning(keyword)
	urlanswer=''
	fo = open("/home/sss/test1/test1/templates/url.txt", "w+")
	for url in search(keyword):
		urlanswer+=url
	fo.write(urlanswer)	
	fo.close()
	fin = open("/home/sss/test1/test1/templates/url.txt", "r")
	fink = fin.readline()
	res =''
	i = 20
	while fink:
		i-=1
		if(not fink or i < 0):
			break
		res += "<a href=\""+fink+"\">"+fink+"</a><br>"
		fink = fin.readline()
	fin.close()
	fo = open("/home/sss/test1/test1/templates/result.html", "w+")
	fo.write(res)
	fo.close()
	duck_mean(keyword)
	#return search_results

def word_meaning(keyword):
	s = "http://wordnetweb.princeton.edu/perl/webwn?s="
	s+=keyword
	f = urllib2.urlopen(s)
	null = None
	data = urllib2.urlopen("http://www.google.com/dictionary/json?callback=dict_api.callbacks.id100&q="+keyword+"&sl=en&tl=en&restrict=pr%2Cde&client=te").read()[25:-10]
	p = re.compile(r'\\x(\w{2})')
	html = p.sub(asciirepl, data)
	p = re.compile(r'em[a-z]+/em')
	text = p.sub(emrepl,html)
	#html = json2html.convert(json = html)
	style=""
	style="<table>"
	ordered_json = json.loads(text, object_pairs_hook=ordereddict.OrderedDict)
	#print ordered_json
	processed_text = htmlConvertor(ordered_json,style)
	html_parser = HTMLParser.HTMLParser()
	global a
	a = ''
	fo = open("/home/sss/test1/test1/templates/goog.html", "w")
	fo.write(html_parser.unescape(processed_text).encode('utf8'));
	fo.close()
	
def duck_mean(keyword):
    '''
    receive submitted data and process
    '''
    data = duck(keyword)
    text = data[19:-2]
    #checkbox = request.form['users']
    style=""
    #style="<table class=\"table table-condensed table-bordered table-hover\">"
    style="<table>"
    
    #json_input = json.dumps(text)
    ordered_json = json.loads(text, object_pairs_hook=ordereddict.OrderedDict)
    #print ordered_json
    processed_text = htmlConvertor(ordered_json,style)
    html_parser = HTMLParser.HTMLParser()
    global a
    a = ''
    fo = open("/home/sss/test1/test1/templates/base.html", "w")
    fo.write(html_parser.unescape(processed_text).encode('utf8'));
    fo.close()

def iterJson(ordered_json,style):
	global a
	a=a+ style 
	for k,v in ordered_json.iteritems():
		a=a+ '<tr>'
		a=a+ '<th>'+ str(k) +'</th>'
		
		if(isinstance(v,list)):
			a=a+ '<td><ul>'
			for i in range(0,len(v)):
				if(isinstance(v[i],unicode)):
					a=a+ '<li>'+unicode(v[i])+'</li>'
				elif(isinstance(v[i],int) or isinstance(v,float)):
					a=a+ '<li>'+str(v[i])+'</li>'
				elif(isinstance(v[i],list)==False):
					iterJson(v[i],style)

			a=a+ '</ul></td>'
			a=a+ '</tr>'
		elif(isinstance(v,unicode)):
			a=a+ '<td>'+ unicode(v) +'</td>'
			a=a+ '</tr>'
		elif(isinstance(v,int) or isinstance(v,float)):
			a=a+ '<td>'+ str(v) +'</td>'
			a=a+ '</tr>'
		else:
			a=a+ '<td>'
			#a=a+ '<table border="1">'
			iterJson(v,style)
			a=a+ '</td></tr>'
	a=a+ '</table>'

def htmlConvertor(ordered_json,style):
        '''
        converts JSON Object into human readable HTML representation
        generating HTML table code with raw/bootstrap styling.
        '''
        global a
        try:
                for k,v in ordered_json.iteritems():
                        pass
                iterJson(ordered_json,style)
                
        except:
                for i in range(0,len(ordered_json)):
                        if(isinstance(ordered_json[i],unicode)):
                                a=a+ '<li>'+unicode(ordered_json[i])+'</li>'
                        elif(isinstance(ordered_json[i],int) or isinstance(ordered_json[i],float)):
                                a=a+ '<li>'+str(ordered_json[i])+'</li>'
                        elif(isinstance(ordered_json[i],list)==False):
                                htmlConvertor(ordered_json[i],style)

        return a