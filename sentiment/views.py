from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from textblob import TextBlob


def inputform(request):
    if request.method == "GET":
        req = request.GET.get("iform")
        if req != None:
            if len(req) != 0:
                print(len(req))
                blob = TextBlob(req)
                b = blob.sentiment.polarity
                b = b * 100
                if b >5:
                    return HttpResponseRedirect("./positive")
                elif b <0:
                    return HttpResponseRedirect("./negative")
                else:
                    return HttpResponseRedirect("./neutral")
            else:
                return HttpResponseRedirect("./empty")


    return render(request,template_name="inputform.html",context={})


def positive(request):
    return render(request, template_name="positive.html", context={})


def negative(request):
    return render(request, template_name="negative.html", context={})


def neutral(request):
    return render(request, template_name="neutral.html", context={})


def empty(request):
    return render(request, template_name="empty.html", context={})






