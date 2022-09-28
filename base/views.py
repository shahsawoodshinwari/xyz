from django.shortcuts import render

# Create your views here.
def index(request):
    """displays the landing page of the base app"""
    context = {"points": [[1, 2], [2, 3], [3, 4], [4, 5]]}
    context["cities"] = [
        {"name": "Mumbai", "population": "19,000,000", "country": "India"},
        {"name": "Calcutta", "population": "15,000,000", "country": "India"},
        {"name": "New York", "population": "20,000,000", "country": "USA"},
        {"name": "Chicago", "population": "7,000,000", "country": "USA"},
        {"name": "Tokyo", "population": "33,000,000", "country": "Japan"},
    ]
    context["value"] = ["One", "two", "three"]

    return render(request, "base/index.html", context)
