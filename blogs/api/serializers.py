# rest-framework imports
from rest_framework import serializers

# local imports
from  blogs.models import Blog


class ListBlogSerializer(serializers.ModelSerializer):
    '''
        Serializer to list blogs
    '''
    class Meta:
        model = Blog
        exclude = ('section',)


class UpdateBlogSerializer(serializers.ModelSerializer):
    '''
        Serializer to update checkmark
    '''
    def update(self, instance, validated_data):

        instance.checkmark = validated_data.get('checkmark', instance.checkmark)
        instance.save()
        return instance

    class Meta:
        model = Blog
        fields = ['checkmark']