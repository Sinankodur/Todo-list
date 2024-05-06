from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up',views.sign_up, name='sign-up'),
    path('sign-in/',views.sign_in, name='sign-in'),
    path('sign-out/',views.sign_out, name='sign-out'),
    path('add/',views.add_task, name='add-task'),
    path('confirm/<int:pk>/',views.delete_task, name='confirm-delete'),
    path('delete/<int:pk>/',views.confirm_delete, name='delete-task'),
    path('task-edit/<int:pk>/',views.edit_task, name='edit-task'),
    path('edit/<int:pk>/',views.edit_page, name='edit-page'),
    path('update-task/<int:task_id>/', views.update_task_status, name='update-task'),
]
