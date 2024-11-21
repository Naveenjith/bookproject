from django.urls import path
from .views import Booklistview,Bookdetailview,UserRegisterview,Reviewdetailview,Reviewlistview
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('register/',UserRegisterview.as_view(),name='user_register'),
    path('token/',TokenObtainPairView.as_view(),name='token_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('books/',Booklistview.as_view(),name='booklist'),
    path('books/<int:pk>/',Bookdetailview.as_view(),name='bookdetail'),
    path('books/<int:book_id>/reviews/',Reviewlistview.as_view(),name='reviewlist'),
    path('books/<int:book_id>/reviews/<int:pk>/',Reviewdetailview.as_view(),name='review_details')
    
]