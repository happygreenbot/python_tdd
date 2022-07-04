from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    # Third parameter in the render function is a dictionary that specifies how to map variables mentioned in the template with appropriate values
    # The dict.get call allows us to return a null string in case its a GET request, since the request object will not contain the 'item_text' key in that case
    return render(request, 'home.html', {'new_item_text' : request.POST.get('item_text', '')})
