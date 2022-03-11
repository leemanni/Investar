from django.shortcuts import render

# Create your views here.


def main_views(request):
    return render(request, 'index.html')
