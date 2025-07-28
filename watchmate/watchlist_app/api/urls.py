from django.urls import path
from watchlist_app.api.views import WatchListAV, WatchDetails, StreamPlatformAV, StreamPlatformDetailAV,ReviewList,ReviewDetails

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetails.as_view(), name='movie-details'),

    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-details'),

    path('review',ReviewList.as_view(),name='review-list'),
    path('review/<int:pk>',ReviewDetails.as_view(),name='reviw-detail'),
]
