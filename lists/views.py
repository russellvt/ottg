'''
List Views

TODO:
* Add unique URLs for each list
* Add URLs for adding a new item to an existing list via POST
'''

from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
    '''Home Page View

    TODO:
     * Display multiple items in the table
     * Refactor away some duplication in urls.py
    '''
    return render(request, "home.html")


def new_list(request):
    nulist = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=nulist)
    return redirect(f"/lists/{nulist.id}/")


def add_item(request, list_id):
    our_list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST["item_text"], list=our_list)
    return redirect(f"/lists/{our_list.id}/")


def view_list(request, list_id):
    our_list = List.objects.get(id=list_id)
    return render(request, "list.html", {"list": our_list})
