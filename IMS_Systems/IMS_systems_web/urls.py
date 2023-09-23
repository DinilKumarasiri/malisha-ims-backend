from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('temp_Services/', views.Services_list, name='Services_list'),

    path('services/', views.ServicesDetail.as_view()),
    path('services/<int:pk>/', views.ServicesList.as_view()),

    path('products/', views.ProductsDetail.as_view()),
    path('products/<int:pk>/', views.ProductsList.as_view()),

    path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', views.UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', views.LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', views.LogoutAllView.as_view(), name='auth_logout_all'),
]