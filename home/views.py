from django.shortcuts import render
from .models import paket,musteri,sss
# Create your views here.
def index(request):
    pakets = paket.objects.all()
    musteris = musteri.objects.all()
    ssss = sss.objects.all()
    return render(request,"index.html",{"pakets":pakets,"musteris":musteris,"ssss":ssss})
