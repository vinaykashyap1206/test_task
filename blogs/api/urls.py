# django imports
from django.conf.urls import url

# local imports
from blogs.api.views import ListBlogView, UpdateBlogView


urlpatterns = [
    url(r'^list$', ListBlogView.as_view(), name='list-blog'),
    url(r'^update/(?P<pk>[-\w]+)$', UpdateBlogView.as_view(), name='update-blog'),
]