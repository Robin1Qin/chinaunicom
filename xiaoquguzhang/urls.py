from django.urls import path

from . import views
from xiaoquguzhang.views import IndexView
app_name = 'xiaoquguzhang'
urlpatterns = [
    path('add', views.add, name='add'),
    path('radius', views.radius, name='radius'),

]
