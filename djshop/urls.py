from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.urls import path, include

from django.conf import settings

admin_urls = [
    path('api/admin/catalog/', include(('catalog.urls.admin', 'catalog'), namespace='catalog-admin'))
]

front_urls = [
    path('api/front/catalog/', include(('catalog.urls.user', 'catalog'), namespace='catalog-front'))
]

doc_patterns = [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = [
                  path('admin/', admin.site.urls),
              ] + admin_urls + front_urls + doc_patterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = "DjShop"
admin.site.index_title = "DjShop"
admin.site.site_header = "DjShop"
