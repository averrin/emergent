# coding: utf8

from django.conf.urls import patterns, url
from views import AddCoin, AddExp, GiveCoin, BuyView

urlpatterns = patterns('',
                       url(r'^add_coin$', AddCoin.as_view(), name='rpg-add-coin'),
                       url(r'^add_exp$', AddExp.as_view(), name='rpg-add-exp'),
                       url(r'^buy/(?P<item>.*)$', BuyView.as_view(), name='rpg-add-exp'),
                       url(r'^(?P<username>.*)/give_coin$', GiveCoin.as_view(), name='rpg-give-coin'),
                       )
