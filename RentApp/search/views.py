from django.shortcuts import render

# Create your views here.
from django.shortcuts import  render,redirect
from app1.models import Item
from django.db.models import Q



def search(request):
    query = ""
    item = None
    if (request.method == "POST"):
        query = request.POST['q']
        if (query == ""):
            item = Item.objects.all()
        else:
            item = Item.objects.filter(
                Q(name__icontains=query) | Q(category__name__icontains=query))

    return render(request, 'search.html', {'query': query, 'item': item})

