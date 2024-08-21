from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import JoinForm, SportGallery, Team


class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinForm
        fields = '__all__'


class SportGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = SportGallery
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(max_length=50)

    class Meta:
        model = Team
        fields = ["team_name", "team_logo",
                  "head_coach", "description", "player"]

    def validate(self, attrs):
        team_exists = Team.objects.filter(
            team_name=attrs['team_name']).exists()
        if team_exists:
            raise ValidationError('team with this name already exists')
        return super().validate(attrs)
