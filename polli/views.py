from django.http import HttpResponse
from .models import  Question
from django.shortcuts import render
from  django.http import  Http404
def index(request):
    latest_question_list=Question.objects.all().order_by("-pub_date")[:5]
    context={'latest_question_list':latest_question_list}
    return  render(request,'polli/index.html',context);

def scemo(request):
    return HttpResponse("hello darkness my old friend and FUCK YOU")

def SEES(request,question_id):
    try:
        questione=Question.objects.get(id=question_id);
        contest={'questionello':questione}
    except:
        raise Http404()
    return render(request, "polli/SEES.html",contest)

def contarec(lista,numero):
    conta=0
    listarello=[]
    for l in lista:
        listarello.append(l);
        conta += 1;
        if conta >= int(numero):
            return listarello
    return listarello


def recents(request,quanto):
    listo=Question.objects.all().order_by("-pub_date")
    listaout=contarec(listo,quanto);
    context={'recents':listaout};
    return render(request,"polli/recents.html",context)

def count(request):
    quanto=Question.objects.count()
    contorec=0
    for q in Question.objects.all():
        if q.waspubliscied今月():
            contorec+=1
    context={'numtot':quanto,'numrec':contorec}
    return render(request,"polli/count.html",context)
