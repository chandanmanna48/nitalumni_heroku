from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('user_register',views.user_register,name='user_register'),
    path('user_register_details',views.user_register_details,name='user_register_details'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('alumini_cell',views.alumini_cell,name='alumini_cell'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path(r'show_profile/(?p<email>\w+)',views.show_profile,name='show_profile'),
    path('approval',views.approval,name='approval'),
    path(r'accept/(?p<email>\w+)',views.accept,name='accept'),
    path(r'remove/(?p<email>\w+)',views.remove,name='remove'),
    path('add_images',views.add_images,name='add_images'),
    path('delete_image/<int:pk>/',views.delete_image,name='delete_image'),
    path('search_result',views.search_result,name='search_result'),
    path('contact_mail',views.contact_mail,name='contact_mail'),
   # path('info',views.info,name='info'),
]