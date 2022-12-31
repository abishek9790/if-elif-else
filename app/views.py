from django.shortcuts import render

# Create your views here
def functiond(request):
    d={'a':100,'b':500,'c':20}
    return render(request,'functiond.html',context=d)
