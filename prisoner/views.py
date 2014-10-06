# -*- coding: utf-8 -*-
from __future__ import division
import prisoner.models as models
from prisoner._builtin import Page, WaitPage


class Decision(Page):

    template_name = 'prisoner/Decision.html'

    form_model = models.Player
    form_fields = ['decision']

    def variables_for_template(self):

        return {'friend_amount': self.subsession.friend_amount,
                'betrayed_amount': self.subsession.betrayed_amount,
                'enemy_amount': self.subsession.enemy_amount,
                'betray_amount': self.subsession.betray_amount}


class ResultsWaitPage(WaitPage):

    scope = models.Group

    def body_text(self):
        return 'Waiting for the other player to make a decision.'

    def after_all_players_arrive(self):
        for p in self.group.players:
            p.set_payoff()


class Results(Page):

    template_name = 'prisoner/Results.html'

    def variables_for_template(self):
        return {'my_payoff': self.player.payoff,
                'my_decision': self.player.decision.lower(),
                'other_player_decision': self.player.other_player().decision.lower(),
                'same_choice': self.player.decision == self.player.other_player().decision}


def pages():

    return [Decision,
            ResultsWaitPage,
            Results]
