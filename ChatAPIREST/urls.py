from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from chatAPI import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'messages', views.MessageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # re_path(r'^media/(?P<path>.*$)','django.views.static.serve', {'document_root':settings.MEDIA_URL}),
    re_path(r'^chat/',views.chat_index, name='chat_view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)