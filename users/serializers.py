from rest_framework import serializers
from .models import User, UserProfile, Role

from django.contrib.auth.models import Group


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ("id", "email", "username", 'groups')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('user', 'telephone',  'postaladdress', 'name', 'role',
                  'county', 'subcounty', 'constituency', 'ward', 'school_gender', 'school_type', 'boys_pop', 'girls_pop', 'total_pop', 'teachers_pop',  'description', 'fb', 'twitter', 'website', 'other')


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', 'description')
# class SchoolSerializer(serializers.HyperlinkedModelSerializer):
#     profile = SchoolProfileSerializer(required=True)

#     class Meta:
#         model = School
#         fields = ('url', 'email', 'username', 'password', 'profile')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         profile_data = validated_data.pop('profile')
#         password = validated_data.pop('password')
#         school = School(**validated_data)
#         school.set_password(password)
#         school.save()
#         SchoolProfile.objects.create(school=school, **profile_data)
#         return school

#     def update(self, instance, validated_data):
#         profile_data = validated_data.pop('profile')
#         profile = instance.profile

#         instance.email = validated_data.get('email', instance.email)
#         instance.save()

#         profile.dob = profile_data.get('doo', profile.doo)
#         profile.address = profile_data.get('address', profile.address)
#         profile.county = profile_data.get('county', profile.county)
#         profile.zip = profile_data.get('zip', profile.zip)
#         profile.photo = profile_data.get('photo', profile.photo)
#         profile.save()

#         return instance
