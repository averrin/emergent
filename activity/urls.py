from django.conf import settings
from django.conf.urls import patterns, include, url
from views import StreamView, ChatSendView, HistoryView

urlpatterns = patterns('',
    url(r'^$', StreamView.as_view(), name='activity_stream'),
    url(r'^send$', ChatSendView.as_view(), name='activity_send'),
    url(r'^history$', HistoryView.as_view(), name='activity_history'),
)
