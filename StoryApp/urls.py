from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	             path("UserLogin.html", views.UserLogin, name="UserLogin"),
		     path("UserLoginAction", views.UserLoginAction, name="UserLoginAction"),
		     path("GenerateStory", views.GenerateStory, name="GenerateStory"),	   
		     path("GenerateStoryAction", views.GenerateStoryAction, name="GenerateStoryAction"),		     
		     path("SpeechStory", views.SpeechStory, name="SpeechStory"),	
		    ]