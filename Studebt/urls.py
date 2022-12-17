from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# from core.views import LoginView

# customize the django admin with Studebt Admin
admin.site.site_header = 'Studebt Admin'



urlpatterns = [
    path('', include('core.urls')),

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


schema_view = get_schema_view(
   openapi.Info(
      title="Studebt API",
      default_version='v1',
      description="Studebt API Provides backend functionality for A web based application that helps schools keep track of student's credit history.",
      terms_of_service="https://www.huzzy-portfolio.railway.app",
      contact=openapi.Contact(email="hussein.ibrahim6196@gmail.com",name="Hussein Ibrahim"),
      license=openapi.License(name="MY License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)