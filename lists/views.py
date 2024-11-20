from django.http import HttpResponse
from django.shortcuts import render
from lists.models import Item

def home_page(request):
    '''
    TODO:
     * Don't save blank items for every request
    '''
    if request.method == "POST":
        item = Item()
        item.text = request.POST["item_text"]
        item.save()

    return render(
        request,
        "home.html",
        {"new_item_text": request.POST.get("item_text", "")},
    )
