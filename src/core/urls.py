from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.views',
    url(r'^palestrante/([-\w]+)/$', 'speaker_detail', name='speaker_detail'),
)
