from django.urls import path
from .views import *

urlpatterns = [
    path('', news_list, name='news_list_url'),
    path('new/<int:pk>', new_single, name='new_single_url'),
]
