from django.shortcuts import render

# Create your views here.
def About_Us(request):

    dict = {'f0':50, 'f1': 7}

    return render(request,'aboutus/about.html', dict)

def Profiles(request):

    return render(request, 'aboutus/profile.html')