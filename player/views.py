from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response


from .models import Player


class LevelUpView(APIView):
    def get(self, request, player_id):
        player = get_object_or_404(Player, id=player_id)
        player.points += 100
        player.save()
        boost = player.add_boost('speed')

        return Response({
            'username': player.username,
            'points': player.points,
            'new_boost': boost.boost_type,
            'acquired_at': boost.acquired_at
        }, status=status.HTTP_200_OK)
