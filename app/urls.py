from django.urls import path
# from .views import index,detail
from app import views
urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('profile/<str:username>/',views.profile),
]