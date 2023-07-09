# Import text to speech library
import gtts

# Write your mad libs program here
story = (
    "As a former army officer,Jabu enjoyed dancing.He was renown in Nairobi for that.One day Jabu and his friend "
    "Ogot,were caught dancing in the kitchen during working hours! The punishment was to dance for 7 hours non-stop!")

# Prompt user input

career = input("Enter a job title: ")
hobby = input("Enter your favorite hobby: ")
city = input("Enter your Capital City: ")
name = input("Enter your friend's name: ")
verb = input("Enter a verb: ")
number = input("Enter you shoe size: ")

# print mad_lib story

madlib_story = (
    f"As a former {career},Jabu enjoyed {hobby}.He was renown in {city} for that.One day Jabu and his friend {name},were caught {verb} in the kitchen during working hours! The punishment was to dance for {number} hours non-stop!")
print(madlib_story)

from gtts import gTTS

tts = gTTS(madlib_story)
tts.save('madlib_story.mp3')
