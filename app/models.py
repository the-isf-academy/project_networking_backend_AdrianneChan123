# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Kpop_profile(Model):
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

    def change_comment(self, new_comment):
        self.comment = new_comment
        self.save()

    def increase_likes(self):
        self.likes += 1
        self.save()