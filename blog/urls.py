from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('workshops/',views.workshops, name='workshops'),
    path('seminar/',views.seminar, name='seminar'),
    path('res/',views.res, name='res'),
    path('pub/',views.pub, name='pub'),
    path('app/', views.app , name='app'),
    path('pro/', views.pro , name='pro'),
]
