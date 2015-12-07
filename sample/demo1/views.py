from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.template import RequestContext, loader
from .models import article
import random
from sqlite3 import Date
def list(request):
    startD='1991-01-01'
    endD=Date.today()

    obj = article.objects.filter( public_date__range=[startD,endD]).order_by('public_date')
#for random articles:-
    ran_art=random.choice(obj)
    obj1 = article.objects.filter( public_date__range=[startD,endD]).exclude(pk=ran_art.id).order_by('public_date')[:4]
     #for footer:

    obj2=article.objects.filter(public_date__range=[startD,endD]).order_by('?')[:4]
    context={'obj1':obj1}
    context['ran_art']=ran_art
    day = ran_art.public_date.strftime("%A")
    context['day'] = day
    context['obj2']=obj2
    return render(request, 'demo1/list.html', context)


def desc(request,id):
    startD='1991-01-01'
    endD=Date.today()
    obj1=article.objects.get(pk=id)
    context2={'obj1' : obj1}
    obj2 = article.objects.filter( public_date__range=[startD,endD]).exclude(pk=obj1.id).order_by('?')[:4]
    context2['obj2'] = obj2

    return render(request, 'demo1/disc.html', context2)
