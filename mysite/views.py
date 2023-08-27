from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'text.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    charcount=request.POST.get('charcount','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

    if removepunc == "on":
        punctuations='''!(){}:;'"\,<>/?$%^*[]-='''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove punctuatins','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif(charcount =="on"):
        analyzed=""
        for char in djtext:
            analyzed=len(djtext)
        params = {'purpose': 'find length', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps =="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'fullcapse', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)
    elif(newlineremover =="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed+char

        params = {'purpose': 'New line removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("error")

def info(request):
    return HttpResponse("this is my website")

def contract(request):
    return HttpResponse("6398516946")
