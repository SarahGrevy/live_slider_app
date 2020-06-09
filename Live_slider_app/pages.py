
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Discussion(Page):
    form_model = 'player'
    form_fields = ['mutual_judgment']
    live_method = "live_slider"
page_sequence = [Discussion]