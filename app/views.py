# views.py

from banjo.urls import route_get, route_post
from .models import Kpop_profile
from settings import BASE_URL

@route_get(BASE_URL + 'likes_ranking')
def likes_ranking(args):
    likes_ranking = []

    for kpop_profile in Kpop_profile.objects.order_by('-likes'):
        likes_ranking.append(kpop_profile.json_response())
    
    return {'kpop_profile': likes_ranking}