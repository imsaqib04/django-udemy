from django.urls import path,include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (WatchListAV,
                                    WatchDetails, 
                                    StreamPlatformAV, 
                                    StreamPlatformDetailAV,
                                    ReviewList,
                                    ReviewDetails,
                                    ReviewCreate,
                                    StreamPlatformVS)

router = DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetails.as_view(), name='movie-details'),

    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-details'),

    # path('review/',ReviewList.as_view(),name='review-list'),
    # path('review/<int:pk>',ReviewDetails.as_view(),name='reviw-detail'),

    path('<int:pk>/review-create/',ReviewCreate.as_view(),name='review-create'),
    path('<int:pk>/reviews/',ReviewList.as_view(),name='review-list'),
    path('review/<int:pk>/',ReviewDetails.as_view(),name='reviw-details'),
]

