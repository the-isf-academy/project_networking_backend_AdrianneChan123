# views.py

from banjo.urls import route_get, route_post
from .models import Kpop_profile
from settings import BASE_URL

# this route gets all of the kpop profiles
@route_get(BASE_URL + 'all')
def all_kpop_profiles(args):
    kpop_profile_list = []
    for kpop_profile in Kpop_profile.objects.all():
        kpop_profile.increase_views()
        kpop_profile_list.append(kpop_profile.json_response())

    return {'kpop_profile':kpop_profile_list}

# this route picks and presents a random kpop profile 
@route_get(BASE_URL + 'random')
def random_kpop_profile(args):
    one_kpop_profile = Kpop_profile.objects.order_by('?').first()
    one_kpop_profile.increase_views()
    
    return {'kpop_profile': one_kpop_profile.json_response()}

# this route displays the chosen kpop profile by the user
@route_get(BASE_URL + 'one', args={'artist_name': str})
def one_kpop_profile(args):
    if Kpop_profile.objects.filter(artist_name=args['artist_name']).exists():
        one_kpop_profile = Kpop_profile.objects.get(artist_name=args['artist_name'])
        one_kpop_profile.increase_views()    
        return {'kpop_profile': one_kpop_profile.json_response()}
    
    else:
        return {'error': 'no kpop_profile exists'}

# this route allows the user to insert a whole new kpop profile to the API
@route_post(BASE_URL + 'new', args={'artist_name':str, 'debut': str, 'members':str, 'fandom_name':str, 'fandom_colour':str, 'company':str, 'comment':str})
def new_kpop_profile(args):
    new_kpop_profile = Kpop_profile(
        artist_name = args['artist_name'],
        debut = args['debut'],
        members = args['members'],
        fandom_name = args['fandom_name'],
        fandom_colour = args['fandom_colour'],
        company = args['company'],
        likes = 0,
        popularity = 0,
        views = 0,
        comment = args['comment']
    )
    new_kpop_profile.save()
    
    return {'kpop_profile': new_kpop_profile.json_response()}

# the user can use this route to like the kpop artist profile that they admire 
@route_post(BASE_URL + 'likes', args={'artist_name':str})
def increase_likes(args):  
    if Kpop_profile.objects.filter(artist_name=args['artist_name']).exists():
        one_kpop_profile = Kpop_profile.objects.get(artist_name=args['artist_name'])
        one_kpop_profile.increase_views()
        one_kpop_profile.increase_likes()
        return {'kpop_profile':one_kpop_profile.json_response()}
    
    else:
        return {'error': 'no kpop_profile exists'}

# this route allows the user to view the range of kpop groups under the chosen company
@route_get(BASE_URL + 'search_company', args={'company':str})
def search_company(args):
    kpop_profile_search_list = []
    for kpop_profile in Kpop_profile.objects.filter(company=args['company']):
        kpop_profile.increase_views()
        kpop_profile_search_list.append(kpop_profile.json_response())
    
    return {'kpop_profile':kpop_profile_search_list}

# this is one of my MVPs, which this route allows the user to comment on different kpop artist profiles, and once the new comment is written, the API will automatically carry out an update, where the old comment will be replaced
@route_post(BASE_URL + 'change_comment', args={'artist_name':str, 'new_comment': str})
def change_comment(args):  
    if Kpop_profile.objects.filter(artist_name=args['artist_name']).exists():
        one_kpop_profile = Kpop_profile.objects.get(artist_name=args['artist_name'])
        one_kpop_profile.renew_comment(args['new_comment'])
        one_kpop_profile.increase_views() 
        return {'kpop_profile':one_kpop_profile.json_response()}
    
    else:      
        return {'error': 'no kpop_profile exists'}

# this is my other MVP, which this route shows the user a most updated podium of the top 5 artists with the most likes
@route_get(BASE_URL + 'top_5')
def top_5(args):
    top_5 = []
    for kpop_profile in Kpop_profile.objects.order_by('-likes')[:5]:
        kpop_profile.increase_views()
        top_5.append(kpop_profile.json_response())    
    
    return {'kpop_profile': top_5}

# this route displays a general ranking of all the kpop profiles, according to the number of likes they receive
@route_get(BASE_URL + 'rankings')
def rankings(args):
    rankings = []
    for kpop_profile in Kpop_profile.objects.order_by('-likes'):
        kpop_profile.increase_views()
        rankings.append(kpop_profile.json_response())
    
    return {'kpop_profile':rankings}