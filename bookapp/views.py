from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView,ListAPIView
from .serializers import UserRegisterserializer,Bookserializer,Reviewserializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Book,Review
from rest_framework.filters import SearchFilter,OrderingFilter
from django.db.models import Avg
#from rest_framework.response import Response
#from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

class UserRegisterview(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserRegisterserializer
    permission_classes=[AllowAny]

class Bookpagination(PageNumberPagination):
    page_size=5
    page_size_query_param='page_size'
    max_page_size=50

class Booklistview(ListCreateAPIView):
    serializer_class=Bookserializer
    queryset=Book.objects.annotate(average_rating=Avg('reviews__rating'))
    pagination_class=Bookpagination
    filter_backends=[SearchFilter,OrderingFilter,DjangoFilterBackend]
    search_fields=['title','author','isbn']
    ordering_fields=['title','author','average_rating','date']
    filterset_fields=['genre']

class Bookdetailview(RetrieveUpdateDestroyAPIView):
    serializer_class=Bookserializer
    queryset=Book.objects.annotate(average_rating=Avg('reviews__rating'))

class Reviewlistview(ListCreateAPIView):
    serializer_class=Reviewserializer
    permission_classes=[IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        book_id=self.kwargs['book_id']
        return Review.objects.filter(book_id=book_id)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user,book_id=self.kwargs['book_id'])

class Reviewdetailview(RetrieveUpdateDestroyAPIView):
    serializer_class=Reviewserializer
    permission_classes=[IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)
    
class Bookrecomendationview(ListAPIView):
    serializer_class=Bookserializer
    def get_queryset(self):
        try:
            book = Book.objects.get(pk=self.kwargs['pk'])
        except Book.DoesNotExist:
            return Book.objects.none() 
        recommendations = Book.objects.filter(genre=book.genre).exclude(pk=book.pk)
        if not recommendations.exists():
            recommendations = Book.objects.filter(author=book.author).exclude(pk=book.pk)  
        return recommendations



