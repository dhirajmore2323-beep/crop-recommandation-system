from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page as default
    path('about/', views.about, name='about'),
    path('predict/', views.predict_crop, name='predict'),
    path('login/', views.login_view, name='login'),
]