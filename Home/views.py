from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def gallery(request):
    return render(request,'gallery.html')

def highlight(request):
    return render(request,'highlight.html')

def news(request):
    return render(request,'news.html')

def announcement(request):
    return render(request,'announcement.html')