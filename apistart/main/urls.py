from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'main'

router = DefaultRouter()
router.register(r'users', views.UserAPI, basename='users')
router.register(r'tasks', views.TaskAPI, basename='tasks')


urlpatterns = [
    path('', views.main, name='main'),
    path('reg/', views.UserRegistrationView.as_view(), name='reg'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

    path('api/', include(router.urls)),
    path('api/login/', views.CustomLoginAPIView.as_view(), name='login-api'),
]