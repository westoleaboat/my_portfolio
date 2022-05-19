from django.urls import path

# Import views.py 
from . import views

urlpatterns = [
    path('', views.index),       # this will invoke whatever is defined in views.py
    #path('blog/index.html', views.index),
    path('blog/graphs.html', views.graphs),
    path('blog/guis.html', views.guis),
]
