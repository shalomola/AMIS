from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('settings', views.settings, name='settings'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('userassets', views.userassets, name='userassets'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('assetlist', views.assetlist, name='assetlist'),
    path('userprofiles', views.userprofiles, name='userprofiles'),
    path('assignments', views.assignments, name='assignments'),
    path('addasset', views.addasset, name='addasset'),
    path('assignasset', views.assignasset, name='assignasset'),
    path('delete_todo/<int:id>', views.todoDelete, name='delete_todo'),
    path('delete_asset/<int:id>', views.deleteAsset, name='delete_asset'),
    path('delete_staff/<int:id>', views.deleteStaff, name='delete_staff'),
]
