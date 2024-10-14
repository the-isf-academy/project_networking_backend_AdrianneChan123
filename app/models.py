# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Kpop_profile(Model):
    artist_name = IntegerField()
    debut = StringField()
    fandom_name = StringField()
    fandom_colour = StringField()
    likes = IntegerField()
    popularity = FloatField()
    comment = StringField()
    views = IntegerField()

    def json_response(self):
        return {
            'id':self.id,
            'artist_name': self.artist_name,
            'debut': self.debut,
            'fandom_name': self.fandom_name,
            'fandom_colour': self.fandom_colour,
            'likes': self.likes,
            'popularity': self.popularity,
            'comment': self.comment,
            'views': self.views
        }

    def increase_likes(self):
        self.likes += 1
        self.save()