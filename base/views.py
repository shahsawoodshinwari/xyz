from django.shortcuts import render

# Create your views here.
def index(request):
    """displays the landing page of the base app"""
    context = {}
    return render(request, "base/index.html", context)
