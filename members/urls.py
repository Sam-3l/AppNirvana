from django.urls import path
from . import views
urlpatterns = [
    path('members/', views.members, name='members'),
    path('hoor/', views.sccn, name='sccn'),
    path('user_inp/', views.get_values, name='get_values'),
    path('login/', views.login, name='login'),
    path('userhome/<int:id>', views.userhome, name='userhome'),
    path('userprofile/<int:id>', views.userprofile, name='userprofile'),
    path('profiledit/<int:id>', views.profiledit, name='edit_profile'),
    path('profilesave/<int:id>', views.profilesave, name='save_profile'),
    path('post/<int:id>', views.post, name='user_post'),
    path('postsave/<int:id>', views.postsave, name='save_post')
]