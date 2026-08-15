from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
import os
from transformers import pipeline
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import warnings
warnings.filterwarnings('ignore')

global username, story_data, prompt
generator = pipeline('text-generation', model='gpt2')
translator = Translator()

def SpeechStory(request):
    if request.method == 'GET':
        skill_id = request.GET['rid']
        playsound("StoryApp/static/story.mp3")
        return render(request, 'GenerateStory.html', {})

def GenerateStoryAction(request):
    if request.method == 'POST':
        global username, generator, translator
        keywords = request.POST.get('t1', False)
        language = request.POST.get('t2', False)
        speech = request.POST.get('t3', False)
        story = generator(keywords, max_length=500, num_return_sequences=1)[0]['generated_text']
        if language == 'hi':
            story = translator.translate(story, dest='hi').text
        elif language == 'te':
            story = translator.translate(story, dest='te').text
        if os.path.exists('StoryApp/static/story.txt'):
            os.remove('StoryApp/static/story.txt')
        with open('StoryApp/static/story.txt', "wb") as file:
            file.write(story.encode())
        file.close()
        output = ""
        if speech == 'yes':
            if os.path.exists('StoryApp/static/story.mp3'):
                os.remove('StoryApp/static/story.mp3')
            tts = gTTS(text=story, lang=language, slow=False)
            tts.save("StoryApp/static/story.mp3")
            output+='<tr><td><a href=\'SpeechStory?rid=story.mp3\'><font size="3" color="blue">Click Here to Speech story</font></a></td></tr>'
        output += '<tr><td><font size="3" color="black">Generated Story Details</td><tr>'
        output += '<td><textarea name="t1" rows="15" cols="70">'+story+'</textarea></td></tr>'
        context= {'data1':output}
        return render(request, 'Output.html', context)

def GenerateStory(request):
    if request.method == 'GET':
       return render(request, 'GenerateStory.html', {})

def UserLogin(request):
    if request.method == 'GET':
       return render(request, 'UserLogin.html', {})

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def UserLoginAction(request):
    global username
    if request.method == 'POST':
        status = "none"
        users = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        if users == 'admin' and password == 'admin':
            context= {'data':'Welcome '+users}
            return render(request, "UserScreen.html", context)
        else:
            context= {'data':'Invalid username'}
            return render(request, 'UserLogin.html', context)

    
