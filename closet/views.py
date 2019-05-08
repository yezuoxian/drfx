from random import randint

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.parsers import JSONParser

from . import models
from . import serializers
from .models import UserProfile, Product, Collocation
from .serializers import UserProfileSerializer, ProductSerializer


# Create your views here.
class ClosetListView(generics.ListCreateAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer


@csrf_exempt
def user_profile_list(request):
    """
    List all user profiles, or create a new user profile.
    """
    if request.method == 'GET':
        user_profile = UserProfile.objects.all()
        serializer = UserProfileSerializer(user_profile, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_profile_detail(request, pk):
    """
    Retrieve, update or delete a user profile.
    """
    try:
        user_profile = UserProfile.objects.get(pk=pk)
    except UserProfile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserProfileSerializer(user_profile)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserProfileSerializer(user_profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user_profile.delete()
        return HttpResponse(status=204)


@csrf_exempt
def product_list(request):
    """
    List all products, or create a new product.
    """
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def product_detail(request, pk):
    """
    Retrieve, update or delete a product.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)


@csrf_exempt
def collocation_list(request):
    """
    List all code collocations.
    """
    if request.method == 'GET':
        collocation = Collocation.objects.all()
        all_id = []
        for col in collocation:
            all_id.append(int(col.id))
        idx = randint(min(all_id), max(all_id))
        random_collocation = Collocation.objects.get(pk=idx)
        product_id = random_collocation.collocation.split(',')
        products = []
        for pid in product_id:
            try:
                product = Product.objects.get(pk=int(pid))
                products.append(product)
            except Product.DoesNotExist:
                return HttpResponse(status=500)
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
