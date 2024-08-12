import random

days = ['Sunday', 'Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

mood = ['happy', 'sad', 'energetic', 'calm', 'curious', 'anxious', 'excited']

times = [' morning', ' afternoon', ' night']


for day in days:
    for time in times:
        feeling = random.choice(mood)
        print(f" On " + day + time + " you were feeling " + feeling)