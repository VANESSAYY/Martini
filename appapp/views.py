from django.shortcuts import render, get_object_or_404, redirect
from .models import Babo
from django.utils import timezone

# Create your views here.
def home(request):
    babos = Babo.objects
    return render(request, 'home.html', {'babos': babos})

def detail(request, babo_id):
    babo_detail = get_object_or_404(Babo, pk= babo_id)
    return render(request, 'detail.html', {'babo': babo_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    babo = Babo()
    babo.title = request.GET['title']
    babo.body = request.GET['body']
    babo.pub_date = timezone.datetime.now()
    babo.save()
    return redirect('/babo/' + str(babo.id))

def delete(request, babo_id):
    babos = Babo.objects.get(pk= babo_id)
    babos.delete()
    return redirect('home')