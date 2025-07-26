from django.urls import path,include
# from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import WatchListAV ,WatchDetails,StreamPlatformAV

urlpatterns = [

    # path('list/',movie_list,name='movie-list'),
    # path('<int:pk>',movie_details,name='movie-details'),

    path('list/',WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>',WatchDetails.as_view(),name='movie-details'),

    path('stream/',StreamPlatformAV.as_view(),name = 'stream-list'),
    path('stream/<int:pk>/',StreamPlatformAV.as_view(),name = 'stream-details'),


]
