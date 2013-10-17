from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login$', 'django.contrib.auth.views.login',
        {"template_name": 'login.html'}),
)

urlpatterns += patterns('accounts.views',
    url(r'^$', 'login'),
)
