from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def readindex(request):
    fn= int (request.POST['tbfn'])
    sn= int(request.POST['tbsn'])
    data ={'firstnumber':fn,'secondnumber':sn}
    return render(request,'Dispalay.html',data)
