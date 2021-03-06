from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserSignup, UserLogin, AddUserModel, FindPlaceRecommendations, FindEventRecommendations, getAllEvents, getAllPlaces, addRating, getRatings, getUserConfig, getComuni, getEventi, getLuoghi, RuleBasedRecommender, CreateMyrrorUserModel, FindEventRecommendationsAllRecommenders, SendSperimentazione, getDatiSperimentazione

urlpatterns = {
		url(r'UserSignup/$',UserSignup.as_view()),
		url(r'UserLogin/$',UserLogin.as_view()),
		url(r'CreateMyrrorUserModel/$',CreateMyrrorUserModel.as_view()),
		url(r'AddUserModel/$',AddUserModel.as_view()),
		url(r'FindPlaceRecommendations/$',FindPlaceRecommendations.as_view()),
		url(r'FindEventRecommendations/$',FindEventRecommendations.as_view()),
		url(r'FindEventRecommendationsAllRecommenders/$',FindEventRecommendationsAllRecommenders.as_view()),
		url(r'SendSperimentazione/$',SendSperimentazione.as_view()),
		url(r'RuleBasedRecommender/$',RuleBasedRecommender.as_view()),
		url(r'getAllEvents/$',getAllEvents.as_view()),
		url(r'getAllPlaces/$',getAllPlaces.as_view()),
		url(r'getDatiSperimentazione/$',getDatiSperimentazione.as_view()),
		url(r'addRating/$',addRating.as_view()),
		url(r'getRatings/$',getRatings.as_view()),
		url(r'getUserConfig/$',getUserConfig.as_view()),
		url(r'getComuni/(?P<letters>[\w\s]+)$',getComuni.as_view()),
		url(r'getEventi/(?P<letters>[\w\s]+)$',getEventi.as_view()),
		url(r'getLuoghi/(?P<letters>[\w\s]+)$',getLuoghi.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
