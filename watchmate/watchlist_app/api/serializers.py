from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform,Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    
    reviews = ReviewSerializer(many=True,read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"

    def get_len_name(self, obj):
        return len(obj.title)  # assuming WatchList model has 'title' field

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-details'  # Ensure this matches URL name
    # )

    class Meta:
        model = StreamPlatform
        fields = "__all__"

    def validate(self, data):
        name = data.get('name', '')
        description = data.get('description', '')
        if name == description:
            raise serializers.ValidationError("Name and Description should be different")
        return data

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        return value
