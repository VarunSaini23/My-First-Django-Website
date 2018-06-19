from django.conf.urls import url
from my_sub_app.views import english,hindi,punjabi,comedy,sci_fi,adventure
urlpatterns=[
    url(r'english/',english,name="cat-eng"),
    url(r'hindi/',hindi,name="cat-hin"),
    url(r'punjabi/',punjabi,name="cat-pun"),
    url(r'comedy/',comedy,name="cat-com"),
    url(r'sci-fi/',sci_fi,name="cat-sci-fi"),
    url(r'adventure/',adventure,name="cat-adv"),
]
