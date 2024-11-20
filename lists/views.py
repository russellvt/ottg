'''
List Views

TODO:
* Adjust model so that items are associated with different lists
* Add unique URLs for each list
* Add URLs for adding a new item to an existing list via POST
'''

from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
    '''Home Page View

    TODO:
     * Pass existing list items to the template somehow
     * Display multiple items in the table
     * Support more than one list!
    '''
    return render(request, "home.html")


def new_list(request):
    Item.objects.create(text=request.POST["item_text"])
    return redirect("/lists/the-only-list-in-the-world/")


def view_list(request):
    items = Item.objects.all()
    return render(request, "list.html", {"items": items})
