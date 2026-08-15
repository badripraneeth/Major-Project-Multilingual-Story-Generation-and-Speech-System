
from transformers import pipeline
from googletrans import Translator
from gtts import gTTS
from playsound import playsound

translator = Translator()

def generate_story(prompt):
    generator = pipeline('text-generation', model='gpt2')
    story = generator(prompt, max_length=500, num_return_sequences=1)[0]['generated_text']
    return story

def save_story(story, filename="story.txt"):
    with open(filename, "w") as file:
        file.write(story)

def saveTranslation(story, filename):
    with open(filename, "wb") as file:
        file.write(story.encode())
    file.close()    

'''
data = input("Enter keywords : ")
story = generate_story(data)
print(story)

save_story(story)
'''

with open("story.txt", "rb") as file:
    story = file.read()
file.close()
story = story.decode()
telugu = translator.translate(story, dest='te').text
saveTranslation(telugu, "telugu.txt")
hindi = translator.translate(story, dest='hi').text
saveTranslation(hindi, "hindi.txt")

tts = gTTS(text=hindi, lang='hi', slow=False)
tts.save("hindi.mp3")
playsound("hindi.mp3")

