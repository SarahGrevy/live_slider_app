
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'Live_slider_app'
    players_per_group = None
    num_rounds = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    def live_slider(self, id_in_group, package):
        broadcast = {"slider_value": package["slider_value"], "disable": package["disable"]}
        return {0: broadcast}
class Player(BasePlayer):
    mutual_judgment = models.IntegerField()