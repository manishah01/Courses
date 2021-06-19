from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('courses',views.course),
    path('courses/add',views.add_course),
    path('courses/destroy/<int:id>',views.confirm_delete),
    path('courses/destroy/<int:id>/return', views.return_home),
    path('courses/destroy/<int:id>/confirm',views.delete_course),
]