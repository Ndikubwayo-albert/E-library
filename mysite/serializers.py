from rest_framework import serializers
from mysite.models import Book


class Book_serializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields= ('id', 'title', 'author','description', 'book_image')
        
# class Book_serializerV2(serializers.ModelSerializer):
#     class Meta:
#         model= Book
#         fields= ('id', 'title', 'author', 'book_image')
        
        
