from django.conf.urls import url

from ajnabee.rtest.views.rtest_view import RtestView,RtestAllView

urlpatterns = [
    url(r'^api/rtest/all/?$', RtestAllView.as_view(), name='rtest_all'),
    url(r'^api/rtest/(?P<pk>\d+)/?$', RtestView.as_view(), name='rtest'),
]