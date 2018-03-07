from django.urls import path
from learningcenter.views import ListView,DetailView

app_name = 'learningcenter'
urlpatterns = [
    path('list/', ListView.as_view(), name='list'),
    path('<int:article_id>/',DetailView.as_view(), name='detail'),

]
