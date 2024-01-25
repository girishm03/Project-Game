from django.urls import path
from games import views

urlpatterns = [
    path('INDEX/', views.INDEX, name='INDEX'),

    path('addcat/', views.addcat, name='addcat'),
    path('cdata/', views.cdata, name='cdata'),
    path('displaycat/', views.displaycat, name='displaycat'),
    path('Editcat/<int:dataid>/', views.Editcat, name='Editcat'),
    path('updatecategory/<int:dataid>/', views.updatecategory, name='updatecategory'),
    path('deletecategory/<int:dataid>/', views.deletecategory, name='deletecategory'),


    path('addgame/', views.addgame, name='addgame'),
    path('gamedata/', views.gamedata, name='gamedata'),
    path('displaygame/', views.displaygame, name='displaygame'),
    path('editgame/<int:game_id>/', views.editgame, name='editgame'),
    path('updategame/<int:dataid>/', views.updategame, name='updategame'),
    path('deletegame/<int:dataid>/', views.deletegame, name='deletegame'),

    path('admin_login/', views.admin_login, name='admin_login'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),

    path('displayuser/', views.displayuser, name='displayuser'),
    path('deleteuser/<int:dataid>/', views.deleteuser, name='deleteuser'),


]