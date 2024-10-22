# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Kpop_profile(Model):
    # these are the fields of my API, with their crresponding data type 
    artist_name = StringField()
    debut = StringField()
    members = StringField()
    fandom_name = StringField()
    fandom_colour = StringField()
    company = StringField()
    likes = IntegerField()
    popularity = FloatField()
    views = IntegerField()
    comment = StringField()

    # this method returns the json response of the corresponding kpop profile, with the value of its different fields
    def json_response(self):
        return {
            'id':self.id,
            'artist_name': self.artist_name,
            'debut': self.debut,
            'members': self.members,
            'fandom_name': self.fandom_name,
            'fandom_colour': self.fandom_colour,
            'company': self.company,
            'likes': self.likes,
            'popularity': self.popularity,
            'views': self.views,
            'comment': self.comment,
        }

    # this method updates the comment of the individual kpop profile to the most recent one
    def renew_comment(self, new_comment):
        self.comment = new_comment
        self.save()

    # this method increases the likes of the kpop profile by 1
    def increase_likes(self):
        self.likes += 1
        self.save()
    
    # this method increases the views of the kpop profile by 1
    def increase_views(self):
        self.views += 1
        self.save()

    # this method calculates the percentage of popularity using likes and views, and in the views this method is constantly after increasing views  to update the popularity of the kpop profile to the latest version
    def calculate_popularity(self):
        self.popularity = (self.likes/self.views) * 100
        self.save()