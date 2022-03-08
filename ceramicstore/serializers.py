from rest_framework import serializers

from .models import Collection, Product, ProductPictures


class ProductPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPictures
        fields = ['id', 'name', 'slug', 'get_image_url']


class ProductSerializer(serializers.ModelSerializer):
    product_pictures = ProductPictureSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "slug",
            "price",
            "get_image_url",
            "product_pictures",
            "get_collection"
        ]


class CollectionSerializer(serializers.ModelSerializer):
    ceramic_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = ['id', 'name', 'slug', 'ceramic_products']


