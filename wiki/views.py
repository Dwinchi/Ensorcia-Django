from django.shortcuts import render
from . import util
from markdown2 import *

def index(request):
    return render(request, "Ensorcia/index.html", {
        "entries": util.list_entries()
    })

def get(request, title):
    #mytext = util.get_entry(title)
    return render(request, "Ensorcia/wiki.html", {
        "mytext": markdown(util.get_entry(title)),
        "mytitle": title
    })