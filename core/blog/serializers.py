from rest_framework import serializers
from blog.models import Post, Employee


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'mypost', 'link', 'status')
        model = Post

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'age', 'salary')
        model = Employee
