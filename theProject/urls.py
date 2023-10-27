from django.contrib import admin
from django.urls import path , include
from login import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    #path('committeeChairs/', include('committeeChairs.urls')), # this is a link to committee chairs app
    # path('doctors/', include('doctors.urls')), # this is a link to doctors app
    # path('students/', include('students.urls')), # this is a link to students app

]

if settings.DEBUG:
  #  urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT) # This is a setting URL for media (:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # This is a setting URL for media (:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()

#    path('',views.index, name='index'),