from django.urls import include, path


from . import views

app_name = 'account'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('api/', include('account.api.urls'))
]
