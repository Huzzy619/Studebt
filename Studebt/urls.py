from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from django.views.generic import TemplateView


# customize the django admin with Studebt Admin
admin.site.site_header = 'Studebt Admin'



urlpatterns = [
    path('', TemplateView.as_view(template_name="core/index.html")),

    path('auth/', include('core.urls')),

    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('auth/', include('djoser.social.urls')),

    # path('login/', LoginView.as_view()),

    
    path('debtors/', include ('mydebtors.urls')),

    # linking info_hub urls
    path('info/', include ('info_hub.urls')),


    # path('biodata/<int:pk>', BioDataView.as_view()),


    path('__debug__/', include('debug_toolbar.urls')),

    
]


#Documentation Links

# # Documentation paths

urlpatterns += [
   #  # YOUR PATTERNS
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
   #  # Optional UI:
    path(
        "api/schema/swagger",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="schema-swagger-ui",
    ),
    path(
        "api/schema/redoc",
        SpectacularRedocView.as_view(url_name="schema"),
        name="schema-redoc",
    ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)