from django.urls import path, include
from . import views

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'booking/tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'), # Higher up --> preference to default router

    path('', include(router.urls)),

    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),

    path('api-token-auth/', obtain_auth_token)
]
