from django.urls import path
from .views import Gaims, DitailPost, addComments, AddLike,DelLike


urlpatterns = [
    path('', Gaims.as_view(), name ='home'),
    path('<int:pk>/', DitailPost.as_view()),
     path('review/<int:pk>/', addComments.as_view(), name='add_comment' ),
     path('<int:pk>/add_like/', AddLike.as_view(), name='add_like' ),
     path('<int:pk>/del_like/',  DelLike.as_view(), name='del_like' ),
   
   
]