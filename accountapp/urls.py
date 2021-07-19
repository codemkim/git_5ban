from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'), # 주소 이름 / urls 함수 이름 불러오고 / 이림은 새로 정한다

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),

    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'), # 고유한 숫자 정보를 받아와야됨 int:pk

    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
]