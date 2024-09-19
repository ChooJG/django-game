from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'common'


urlpatterns = [
    #path('', views.index, name='index'),

    #로그인 뷰를 따로 만들지 않고 LoginView 사용 (장고 기본 제공)
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
]