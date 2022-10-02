
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from opinion_ate import views

router = routers.DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'dishes', views.DishViewSet)

# urls for the entire project #
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('api/', include('blog_api.urls', namespace='blog_api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('restaurants/', include(router.urls)),
]
