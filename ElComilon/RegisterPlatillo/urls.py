from django.urls import path
from Register_repartidor import views
    app_name = "Register_repartidor"
        urlpatterns = [
            path('registerRepatidor/', views.Register_repatidor, name='Register_repatidor'),
        ] 