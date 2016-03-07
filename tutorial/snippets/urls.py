from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
	url(r'^snippets/$', views.snippet_list),
	url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

# Format suffixes to URLs to explicitly refer to a given format (eg. /snippets.json or /snippet/2.json)
urlpatterns = format_suffix_patterns(urlpatterns)