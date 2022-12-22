from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:id>',views.apply,name='apply'),
    path('<int:id>',views.remove,name='remove'),
    path('new',views.new,name='new'),
    path('appliedlist',views.appliedlist,name='appliedlist')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)