# coding: utf8

from django.conf.urls import patterns, url
from views import AddCoin, AddExp

urlpatterns = patterns('',
                       url(r'^add_coin$', AddCoin.as_view(), name='rpg-add-coin'),
                       url(r'^add_exp$', AddExp.as_view(), name='rpg-add-exp'),
                       )