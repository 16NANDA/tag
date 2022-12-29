from django.shortcuts import render

# Create your views here.
def sec (request):

    d = {'name':'M.SUBBADI'}
    return render(request,'first.html',d)