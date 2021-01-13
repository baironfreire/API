from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Category

# Create your views here.
def list_category(request):
    MAX_OBJECT = 20
    cat = Category.objects.all()[:MAX_OBJECT]
    data = {"result": list(cat.values("description", "status"))}
    return JsonResponse(data)

def detail_category(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    data = {"result": {"description": cat.description, "status": cat.status}}
    return JsonResponse(data)
