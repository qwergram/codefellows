from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^upload/', views.UploadView.as_view(), name='upload'),
    url(r'^uploading/', views.upload_image, name='uploading'),
    url(r'^stats/(?P<pk>[A-z0-9.]+)', views.IndividualStatView.as_view()),
    url(r'^stats/', views.StatView.as_view(), name='stats'),
    url(r'^popularity/', views.PopularityView.as_view(), name='popularity'),
    url(r'^random/', views.CompareView.as_view(), name='compare'),
    # url(r'^cards/', views.CardsIndexView.as_view(), name='cards'),
    # url(r'^signin/', views.SignIn.as_view(), name='signin'),
    # url(r'^signup/', views.SignUp.as_view(), name='signup'),
]
