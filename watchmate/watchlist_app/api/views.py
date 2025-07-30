from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
# from rest_framework import mixins

from watchlist_app.models import WatchList, StreamPlatform,Review
from watchlist_app.api.serializers import (WatchListSerializer,
                                           StreamPlatformSerializer,
                                           ReviewSerializer)

from watchlist_app.api.permissions import AdminOrReadOnly,ReviewUserOrReadOnly


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie")

        # Save the review first
        serializer.save(watchlist=watchlist, review_user=review_user)

        # Update number_rating
        watchlist.number_rating = watchlist.number_rating + 1

        # Correctly update avg_rating (running average)
        watchlist.avg_rating = (
            (watchlist.avg_rating * (watchlist.number_rating - 1)) + serializer.validated_data['rating']
        ) / watchlist.number_rating

        watchlist.save()


class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    # overwrite quary set
    def get_queryset(self):
        pk= self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]


# class ReviewDetails(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# just three lines sb kuch aa gya isme we control everything
class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

    # class StreamPlatformVS(viewsets.ReadOnlyModelViewSet):
    # queryset = StreamPlatform.objects.all()
    # serializer_class = StreamPlatformSerializer

#     #routing kri thi tb
# class StreamPlatformVS(viewsets.ViewSet):
    
#     def list(self,request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset,many=True,context={'request': request})
#         return Response(serializer.data)
    
#     def retrieve(self,request,pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset,pk=pk)
#         serializer = StreamPlatformSerializer(watchlist, context={'request': request})
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer = StreamPlatformSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- StreamPlatform List & Create ---
class StreamPlatformAV(APIView):
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- StreamPlatform Detail (Retrieve, Update, Delete) ---
class StreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Stream Platform not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Stream Platform not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(platform, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Stream Platform not found'}, status=status.HTTP_404_NOT_FOUND)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --- WatchList List & Create ---
class WatchListAV(APIView):
    def get(self, request):
        watchlist = WatchList.objects.all()
        serializer = WatchListSerializer(watchlist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- WatchList Detail (Retrieve, Update, Delete) ---
class WatchDetails(APIView):
    def get(self, request, pk):
        try:
            watch_item = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'WatchList item not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(watch_item)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            watch_item = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'WatchList item not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(watch_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            watch_item = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'WatchList item not found'}, status=status.HTTP_404_NOT_FOUND)
        watch_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
