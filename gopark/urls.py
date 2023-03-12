from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token


from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from park_user.views import AuthorRegisterAPIView, AuthorRetrieveDestroyAPIView
from park_app.views import IventCreateListAPIView,  IventRetrievUpdateDestroyAPIView, CreaterCreateListAPIView, \
    CreaterRetrievUpdateDestroyAPIView



schema_view = get_schema_view(
    openapi.Info(
        title="PDD API",
        default_version='v0.1',
        description="API для сайта Ак-Жол",
        terms_of_service="https://www.codifylab.com",
        contact=openapi.Contact(email="belek.omuraliev74@gmail.com"),
        license=openapi.License(name=" "),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/token/', obtain_auth_token),
    path('api/register/', AuthorRegisterAPIView.as_view()),
    path('api/register/<int:pk>/', AuthorRetrieveDestroyAPIView.as_view()),
    path('api/ivent/', IventCreateListAPIView.as_view()),
    path('api/ivent/<int:pk>/', IventRetrievUpdateDestroyAPIView.as_view()),
    path('api/creater/', CreaterCreateListAPIView.as_view()),
    path('api/creater/<int:pk>/', CreaterRetrievUpdateDestroyAPIView.as_view()),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_ui'),
    #path('json_doc/', schema_view.without_ui(cache_timeout=0), name='json_doc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

