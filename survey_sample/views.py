# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants

class Survey(Page):

    template_name = 'survey_sample/Survey.html'

    form_model = models.Player
    form_fields = ['q_gender']

    def vars_for_template(self):
        self.player.set_payoff()
        return None


def pages():

    return [Survey]
