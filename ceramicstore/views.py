from django.http import Http404
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Collection, ProductPictures
from .serializers import ProductSerializer, CollectionSerializer, ProductPictureSerializer

# Create your views here.


class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:5]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, product_id, product_slug):
        try:
            return Product.objects.filter(id=product_id).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, product_id, product_slug, format=None):
        product = self.get_object(product_id, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class LatestCollections(APIView):
    def get(self, request, format=None):
        collections = Collection.objects.all()
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)


class CollectionDetail(APIView):
    def get_object(self, collection_id, collection_slug):
        print(collection_id)
        print(collection_slug)
        try:
            return Collection.objects.filter(id=collection_id).get(slug=collection_slug)
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request, collection_id, collection_slug):
        collection = self.get_object(collection_id, collection_slug)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)

