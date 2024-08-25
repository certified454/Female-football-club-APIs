from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q


# from datetime import date
# Create your views here.
from .models import JoinForm, SportGallery, Team, Fixtures, News
from .serializers import JoinSerializer, SportGallerySerializer, TeamSerializer, FixturesSerializers, NewsSerializers


@api_view(['GET'])
def home_list(request):
    sport_gallery = SportGallery.objects.all()
    fixtures = Fixtures.objects.all()
    news = News.objects.all()

    sport_gallery_serializer = SportGallerySerializer(sport_gallery, many=True)
    fixtures_serializer = FixturesSerializers(fixtures, many=True)
    news_serializer = NewsSerializers(news, many=True)

    context = {
        'sport_gallery': sport_gallery_serializer.data,
        'fixtures': fixtures_serializer.data,
        'news': news_serializer.data
    }

    return Response(context, status=status.HTTP_200_OK)

    query = request.GET.get('query')

    if query == None:
        query = ''

    gallery = SportGallery.objects.filter(
        Q(player__icontains=query))
    serializers = SportGallerySerializer(gallery, many=True)
    return Response(serializers.data)


@api_view(['POST'])
def join(request):

    if request.method == "POST":
        join_form = request.data
        serializers = JoinSerializer(data=join_form, many=False)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)

    else:
        join_form = request.data
        serializers = JoinSerializer(join_form, many=False)
    return Response({'message': 'ensure to fill the form'})


@api_view(['POST'])
def sport_gallery(request):

    if request.method == "POST":
        gallery = request.data
        serializers = SportGallerySerializer(data=gallery, many=False)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)

    else:
        gallery = request.data
        serializers = SportGallerySerializer(gallery, many=False)
        return Response(serializers.data)
    return Response({'message': 'ensure to fill the form'})


@api_view(['GET'])
def gallery_list(request):
    if request.method == 'GET':
        gallery = SportGallery.objects.all()
        serializers = SportGallerySerializer(instance=gallery, many=True)
        return Response(serializers.data)


@api_view(['GET'])
def gallery_details(request, player):
    gallery = get_object_or_404(SportGallery, player=player)
    if request.method == 'GET':
        serializer = SportGallerySerializer(instance=gallery)
        return Response(serializer.data)


@api_view(['PUT'])
def update_gallery(request, player):
    gallery = get_object_or_404(SportGallery, player=player)

    data = request.data

    serializer = SportGallerySerializer(instance=gallery, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({'message': 'not updated '})


@api_view(['DELETE'])
def delete_gallery(request, player):
    gallery = get_object_or_404(SportGallery, player=player)

    gallery.delete()
    return Response({'message': 'gallery is deleted succesfull'})


@api_view(['POST'])
def teams(request):

    if request.method == "POST":
        team = request.data
        serializers = TeamSerializer(data=team, many=False)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, {'message': 'team was created successfully'})

    return Response({'message': 'ensure to fill in the required space'})


@api_view(['GET'])
def team_details(request, team_name):

    team = get_object_or_404(Team, team_name=team_name)
    if request.method == 'GET':
        serializer = TeamSerializer(instance=team)
        return Response(serializer.data)
    return Response({"message": "try filling the details for update"})


@api_view(['PUT'])
def update_team(request, team_name):
    team = get_object_or_404(Team, team_name=team_name)

    data = request.data

    serializer = TeamSerializer(instance=team, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({'message': 'not updated'})


@api_view(['POST'])
def fixtures(request):
    fixtures = request.data
    serializers = FixturesSerializers(data=fixtures, many=False)

    if serializers.is_valid():
        serializers.save()
        return Response({"message": "fixtures created succesfully"})
    else:
        fixtures = request.data
        serializers = FixturesSerializers(data=fixtures, many=False)
    return Response({'message': 'fill in valid data'})


@api_view(['POST'])
def news(request):
    news = request.data
    serializers = NewsSerializers(data=news, many=False)

    if serializers.is_valid():
        serializers.save()
        response = {
            'message': 'news created',
            'data': serializers.data
        }
        return Response(data=response)


@api_view(['GET'])
def news_list(request):
    if request.method == 'GET':
        news = News.objects.all()
        serializers = NewsSerializers(instance=news, many=True)
        return Response(serializers.data)


@api_view(['GET'])
def news_details(request, title):
    news = get_object_or_404(News, title=title)

    if request.method == 'GET':
        serializer = NewsSerializers(instance=news)
        return Response(serializer.data, status=status.HTTP_200_OK)
