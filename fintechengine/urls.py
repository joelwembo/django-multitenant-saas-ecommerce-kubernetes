# Django Settings
from django.contrib import admin
from django.views import generic
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings

# Django Rest Framework
from rest_framework import routers, permissions , views, serializers, status
from rest_framework.response import Response
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


# Utils and Libraries
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#apps
from apps.node_api import urls as note_urls
from apps.snippets import urls as snippets_urls
from apps.finances import urls as finances_urls
# ViewSet
from apps.node_api.views import NoteViewSet
from apps.finances.views import AccountViewSet , TransactionViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'router/notes', NoteViewSet, basename="notes")
router.register(r'router/snippets', NoteViewSet, basename="snippets")
router.register(r'router/accounts', AccountViewSet, basename="accounts")
router.register(r'router/transactions', TransactionViewSet, basename="transactions")
router.register(r'router/categories', CategoryViewSet, basename="categories")

urlpatterns = router.urls

user_list = NoteViewSet.as_view({'get': 'list'})
user_detail = NoteViewSet.as_view({'get': 'retrieve'})

schema_view = get_schema_view(
    openapi.Info(
        title="Finance & Machine Learning API",
        default_version='v1',
        description="cloudapp API built by Joel Otepa Wembo",
        terms_of_service="https://www.cloudapp.io/policies/terms/",
        contact=openapi.Contact(email="joelotepawembo@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path('api/v1/notes/', include(note_urls)),
    path('api/v1/snippets/', include(snippets_urls)),
    path('api/v1/finances/', include(finances_urls)),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),   
]

urlpatterns += router.urls
