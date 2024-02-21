from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('<int:pk>/', views.DetailsPageView.as_view(), name='detail'),
    path('create/', views.CreatePersonView.as_view(), name='create'),
    path('delete/<int:pk>/', views.DeletePersonView.as_view(), name='delete'),
    path('update/<int:pk>/', views.UpdatePersonView.as_view(), name='update'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.LogoutPageView.as_view(), name='logout')
]
