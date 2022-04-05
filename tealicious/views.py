import email
from unicodedata import name
from django.shortcuts import render,redirect
from .models import Event,Franchise,categories,AddItem

# Create your views here.
def index(request):

    #menu
    cat=categories.objects.all();
    items=AddItem.objects.all();
    categoryID = request.GET.get('category');
    if categoryID:
     item = AddItem.get_all_item_by_category_id(categoryID);
    else:
     item = AddItem.objects.all()[0:1];
    
   
    


    # event form
    if request.method == 'POST' and 'event' in request.POST:
        ename=request.POST.get('ename')
        eemail=request.POST.get('eemail')
        enumber=request.POST.get('PhoneNumber')
        venue=request.POST.get('venue')
        date=request.POST.get('date')

        event = Event(
            Fullname=ename,
            email=eemail,
            number=enumber,
            venue=venue,
            Date=date,
        )

        event.save()


    # franchise form
    if request.method == 'POST' and 'franchise' in request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('PhoneNumber')
        location=request.POST.get('Location')

        franchise = Franchise(
            Fullname=name,
            email=email,
            number=number,
            Location=location,
        )

        franchise.save()

    params={
        'cat':cat,
        'items':items, 
        'item':item,   }


    return render(request,'index.html',params)