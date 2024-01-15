from django.shortcuts import render
from inventory.models import Collection

# Create your views here.
def home (request):
    return render(request, 'home.html',context={
        'collections':Collection.objects.all()[:4]
    })

#about func --> about.html


#contact func -->