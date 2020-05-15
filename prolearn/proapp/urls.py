from django.conf.urls import url

from proapp import views

app_name = 'proapp'

urlpatterns = [
   url(r'^register/$',views.register,name='register'),
   url(r'^user_login/$',views.user_login,name='user_login'),

]