from django.conf.urls import url
from app import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    url(r'^.*\.html', views.gentella_html, name='gentella'),

    url(r'^cases$', views.cases, name = 'cases'),

    url(r'^home$', views.home, name='home'),

    url(r'^regr$', views.regr, name = 'regr'),

    url(r'^submit_case$', views.submit_case, name = 'submit_case'),

    # The home page
    url(r'^$', views.index, name='index'),
]