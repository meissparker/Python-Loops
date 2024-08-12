import random

days = ['Sunday', 'Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

mood = ['happy', 'sad', 'energetic', 'calm', 'curious', 'anxious', 'excited']


for day in days:
    if range(0,8):
        feeling = random.choice(mood)
        print(f"On " + day + " you were feeling " + feeling)