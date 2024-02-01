from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from myapp.CustomThrottle import ForGetViewThrottle, ForPostViewThrottle
from myapp.models import Book


# Create your views here.


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookView(APIView):


    def get(self, request):
        self.throttle_classes = [ForGetViewThrottle]
        book_data = Book.objects.all()
        serializer_ = BookSerializer(book_data, many=True)
        return Response({"data": serializer_.data})

    def post(self, request):
        self.throttle_classes = [ForPostViewThrottle]
        serializer_ = BookSerializer(data=request.data)
        if serializer_.is_valid():
            serializer_.save()
        return Response({"data": serializer_.data})
