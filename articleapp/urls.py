from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreatView, ArticleDetailView

app_name = 'articleapp'


urlpatterns =[
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
    path('create/', ArticleCreatView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
]