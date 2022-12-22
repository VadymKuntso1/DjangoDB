from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:id>',views.apply,name='apply'),
    path('new',views.new,name='new')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)