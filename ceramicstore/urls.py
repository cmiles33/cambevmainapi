from django.urls import path, include

from .views import LatestProductsList, ProductDetail, LatestCollections, CollectionDetail

urlpatterns = [
    path('latest-products/', LatestProductsList.as_view()),
    path('products/<slug:product_id>/<slug:product_slug>/',
         ProductDetail.as_view()),
    path('collections/', LatestCollections.as_view()),
    path('collections/<slug:collection_id>/<slug:collection_slug>/',
         CollectionDetail.as_view()),
]



