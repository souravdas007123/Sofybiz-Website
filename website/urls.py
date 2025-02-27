from django.urls import path
from website import views
urlpatterns = [
    path('', views.home,name='home'),
    path('term/', views.term,name='term'),
    path('kitchen/', views.kitchen,name='kitchen'),
    path('bedroom/', views.bedroom,name='bedroom'),
    path('washroom/', views.washroom,name='washroom'),
    path('tiles/', views.tiles,name='tiles'),
    path('paint/', views.paint,name='paint'),
    path('plywood/', views.plywood,name='plywood'),
    path('falseceiling/', views.falseceiling,name='falseceiling'),
    path('wallpannel/', views.wallpannel,name='wallpannel'),
    path('constructionservice/', views.constructionservice,name='constructionservice'),
    path('interiorservice/', views.interiorservice,name='interiorservice'),
    path('lightingservice/', views.lightingservice,name='lightingservice'),


]