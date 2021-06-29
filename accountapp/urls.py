from django.urls import path, include

from accountapp.views import hello_world

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'), # 주소 이름 / urls 함수 이름 불러오고 / 이림은 새로 정한다
]