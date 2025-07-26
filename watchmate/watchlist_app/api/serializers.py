from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform


class StreamPlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = StreamPlatform
        fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"  



    # calculate custom field
    def get_len_name(self,object):
        length = len(object.name)
        return length

    # Object-level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description should be different")
        return data

    # Field-level validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        return value


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('name is too short!!')

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True) # read_only this is argument
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.discription)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and Discription should be different!")
#         else:
#             return data
        

    ##
    # def validate_name(self,value):

    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too Short!")
    #     else:
    #         return value

    ##