from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.views',
    url(r'^palestrante/([-\w]+)/$', 'speaker_detail', name='speaker_detail'),
    url(r'^palestras/(\d+)/$', 'talk_detail', name='talk_detail'),
    url(r'^palestras/$', 'talks', name='talks'),
)
