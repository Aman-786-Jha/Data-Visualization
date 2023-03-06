from django.urls import path
from .views import GetView,instance_details,index,likelihood

urlpatterns = [
    path('details/',GetView),
    path('instance-details/<int:pk>',instance_details),
    path('',index),
    path('likelihood/',likelihood)
    
]
