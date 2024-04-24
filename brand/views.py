from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from brand.models import Brand
from django.core import serializers

def get(request):
    v=Brand.objects.all()
    return HttpResponse(serializers.serialize('json', v))
