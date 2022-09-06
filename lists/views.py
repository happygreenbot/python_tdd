from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST': 
        # shorthand for creating new items without calling save() 
        # Saving item in Item table as defined in models, initialising text field with content from post request
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')
    # else:
    #     # if its a GET request, no item needs to be created, and we pass a null string to the template
    #     new_item_text = ''  
    items = Item.objects.all()
    # Third parameter in the render function is a dictionary that specifies how to map variables mentioned in the template with appropriate values
    # The dict.get call allows us to return a null string in case its a GET request, since the request object will not contain the 'item_text' key in that case
    return render(request, 'home.html')

def list_view(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items' : items})

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')
