from rest_framework import serializers

from .models import UserProfile, Product, Collocation

'''
class ClosetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nickname = serializers.CharField(max_length=100)
    weight = serializers.FloatField()
    height = serializers.FloatField()
    gender = serializers.ChoiceField(choices=GENDER_CHOICES, default='python')
    birth = serializers.DateField()
    age = serializers.IntegerField()
'''


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'nickname', 'weight', 'height', 'gender', 'birth', 'age',)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.height = validated_data.get('height', instance.height)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.birth = validated_data.get('birth', instance.birth)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name', 'category', 'image', 'hyperlink',)


class CollocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collocation
        fields = ('collocation',)
