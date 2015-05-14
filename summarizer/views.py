from django.http import HttpResponse
import json
import re
from django.template.loader import get_template
from django import template
from src.extractor import getImageURL, getTitle
from src.summarizer import getSummary
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response

memo = {}


@csrf_exempt
def summary(request):
    url = request.GET['url']
    if url in memo and 'summary' in memo[url]:
        out = memo[url]['summary']
    else:
        out = json.dumps(getSummary(request.GET['url'], request.GET['pos_key'], request.GET['neg_key']), separators=(',',':'))
        memo[url]['summary'] = out
    return HttpResponse(out)
        
@csrf_exempt
def image(request):

    url = request.GET['url']
    if url in memo and 'image' in memo[url]:
        out = memo[url]['image']
    else:
        src = getImageURL(url)
        if src == '':
            out = ''
        else:
            out = '<img alt = ""  class="img-responsive img-rounded" alt="Reponsive image" height="200" width="200" src = "' + str(src) +'">'
        memo[url] = {}
        memo[url]['image'] = out
    return HttpResponse(out)

   
@csrf_exempt
def title(request):
    return HttpResponse(getTitle(request.GET['url']).replace('_', ' '))


def main(request):
    return render_to_response('main.html')

def result(request):
    return render_to_response('result.html')
