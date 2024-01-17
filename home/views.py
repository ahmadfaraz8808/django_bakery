from django.shortcuts import render
from inventory.models import Collection

# Create your views here.
def home (request):
    return render(request, 'home.html',context={
        'collections':Collection.objects.all()[:4]
    })

#about func --> about.html
def about(request):
    return render(request,'about.html')

#contact func --> contact.html
def contact(request):
    if request.method == 'POST':
        email= request.form.get('email')
        name=request.form.get('name')
        message=request.form.get('message')
        #save to database with the contact model
    return render(request,'contact.html')

#gallery func--> gallery.html