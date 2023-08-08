
from django.urls import  path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('',views.login,name='login'),
    path('home', views.home, name='home' ),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('login_form',views.login_form,name='login_form'),
    path('admin_panel',views.admin_panel ,name='admin_panel'),
    path('add_user_form',views.add_user_form,name='add_user_form'),
    path('edit_user',views.edit_user,name='edit_user'),
    path('add_user',views.add_user,name='add_user'),
    path('update_user/<int:id>',views.update_user,name='update_user'),
    path('update_user_form/<int:id>',views.update_user_form,name='update_user_form'),
    path('delete_user/<int:id>',views.delete_user,name='delete_user'),
    path('search_user',views.search_user,name='search_user'),
    path('add_images/',views.add_images,name='add_images'),
    path('add_imagep',views.add_imagep,name='add_imagep')
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
