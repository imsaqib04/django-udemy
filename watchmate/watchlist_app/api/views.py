from watchlist_app.models import WatchList,StreamPlatform
from rest_framework import status
from rest_framework.views import APIView
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer
from rest_framework.response import Response 


class StreamPlatformAV(APIView):

    # def get(self,request):
    #     platform = StreamPlatform.objects.all()
    #     serializer = StreamPlatformSerializer(platform,many=True)
    #     return Response(serializer.data)
    
    def get(self, request, pk=None):
        if pk:
            try:
                platform = StreamPlatform.objects.get(pk=pk)
                serializer = StreamPlatformSerializer(platform)
                return Response(serializer.data)
            except StreamPlatform.DoesNotExist:
                return Response({'error': 'Stream Platform not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            platform = StreamPlatform.objects.all()
            serializer = StreamPlatformSerializer(platform, many=True)
            return Response(serializer.data)

    def post(self,request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            watch_item = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'WatchList item not found'}, status=status.HTTP_404_NOT_FOUND)
        watch_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



####

# class MovieListAV(APIView):

#     def get(self,request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class MovieDetails(APIView):

#     def get(self,request,pk):
#             try:
#                 movie = Movie.objects.get(pk=pk)
#             except Movie.DoesNotExist:
#                 return Response({'error': 'Movie not found'},status=status.HTTP_404_NOT_FOUND)
#             serializer = MovieSerializer(movie)
#             return Response(serializer.data)
        

#     def put(self,request):
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

#     def delete(self,request):
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
 
####

# @api_view(['GET','POST']) 
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies,many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET','PUT','DELETE']) 
# def movie_details(request,pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie not found'},status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


