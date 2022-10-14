from django.urls import path
# Add the include function to the import
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    # In this case '' represents the root route
    path('about/', views.about, name='about'),
    path('las/', views.las_index, name='index'),
]