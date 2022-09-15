from django.urls import path
from rest_framework.authtoken import views as auth_views

from core import views

app_name = 'core'

urlpatterns = [
    path('token-auth/', auth_views.obtain_auth_token, name='token-auth'),
    path('student/create/', views.CreateStudentView.as_view(), name='create-student'),
    path('student/update/<pk>/', views.UpdateStudentView.as_view(), name='update-student'),
    path('student/delete/<pk>/', views.DeleteUserView.as_view(), name='delete-student'),
    path('student/list/', views.ListStudentView.as_view(), name='list-student'),
    path('book/create/', views.CreateBookView.as_view(), name='create-book'),
    path('book/update/<pk>/', views.UpdateBookView.as_view(), name='update-book'),
    path('book/delete/<pk>/', views.DeleteBookView.as_view(), name='delete-book'),
    path('book/list/', views.ListBookView.as_view(), name='list-book'),
    path('checkout/create/', views.CreateCheckOutView.as_view(), name='create-checkout'),
    path('checkout/update/<pk>/', views.UpdateCheckOutView.as_view(), name='update-checkout'),
    path('checkout/delete/<pk>/', views.DeleteCheckOutView.as_view(), name='delete-checkout'),
    path('checkout/history/', views.ListHistoryCheckOutView.as_view(), name='checkout-history'),
]