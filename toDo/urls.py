from django.urls import path
from django.contrib import admin
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('mark_as_done/<int:task_id>/', views.mark_as_done, name='mark_as_done'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
]
