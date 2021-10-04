from django.urls import path
from Login import views


app_name = "Login"

urlpatterns = [
    path('login/', views.login, name='login'),
] 