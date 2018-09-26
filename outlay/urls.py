from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import logout


urlpatterns=[
    url(r'^$',views.home, name='home'),
    url(r'^add/', views.add_item, name='add'),
    url(r'^edit/(?P<pk>\d+)/', views.edit_item, name='edit'),
    url(r'^delete/(?P<pk>\d+)/', views.delete_item, name='delete'),
    url(r'^register/', views.register_user, name='register'),
    url(r'^login/', views.login_user, name='login'),
    url(r'^logout/', logout, {'next_page': '/login'}),
]