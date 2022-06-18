from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .yasg import urlpatterns as docs_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("src.apiurls"), name="api"),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("auth/", include("djoser.urls.jwt")),
] + static(  # type: ignore
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT  # type: ignore
)  # type: ignore

urlpatterns += docs_urlpatterns  # type: ignore
