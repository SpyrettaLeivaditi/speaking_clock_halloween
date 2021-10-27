## **Speaking clock**

### **Project Dependencies**

For your own convenience we have provided a requirements.txt file with all the required dependencies. You can install them by running
```
pip install -r requirements.txt
```

### **Instructions**

##### \> How to run
1. create recording
2. install dependencies
3. run
```flask run``` open browser from the provided link ```http://127.0.0.1:5000/```
4. In the browser, to listen the local time, just push the play button ![Screenshot](/Users/spyretta/Projects/flask_api/photos/just_press_say_time.png) 
5. In the browser, to listen a specific time you wish, press the white field and select the time  and timezone by using the selectors.![Screenshot](/Users/spyretta/Projects/flask_api/photos/pick_time.png)

### Recordings
For GDPR reasons we will not share the recordings of our voice talent, however we will share full instructions on the process of acquiring the recordings:

#####  \> Recordings reproduction

For the recordings production we used:
1. Audacity software (mono sound, 44100Hz, wav file)
2. Yeti microphone (Blue Yeti Blackout)
3. Noise cancelling cylinder
3. Macbook Pro (13-inch, 2019, Four Thunderbolt 3 ports)


#####  \>  Line-scripts of the recordings
We recorded our voice talent saying the following:
- For the number part of hours and minutes: All numbers from 1 - 59
- For special times cases like (12:00 am, 9:00 am, 12:30 pm,  and 6:00 pm), he read :
   - 12:00 am : AAAA, Hi I am casper do you wanna be my friend?
   - 9:00 am : It’s time to work!
   - 12:30 pm : It’s half past I am hungry!
   - 6:00 pm : It’s beer o’clock
- For edge cases like: o'clock, quarter past, quarter to and half past, he read:
   - It’s 10 o’clock
   - It’s quarter past 10
   - It’s quarter to 10
   - It's half past 10
- For normal time eg, 3:10 or 2:50, he read:
   - It’s 10 past 3 
   - It’s 10 to 3
   (the reason we chose to record the words "past" and "to" in a sentence and not isolated was to make them sound more natural)

##### \> Split recordings into tracks:
For splitting recordings into tracks we used the Audacity Software
We followed the following process 
[Easily split large audio files into tracks with Audacity](https://www.youtube.com/watch?v=72ewbraagj8the) tracks as .wav files with the following structure:
- The_clock_recordings
   - Original wav files (folder with the original tracks)
   - Tracks (folder with the splitted tracks)
      - Numbers (numbers that are going to be used to pronounce the hours and the minutes)
      - Sentences (special times cases)
      - Glue_words (it’s, past, quarter, o'clock etc that glue the time and give the final format of the recording of edge and bormal time cases.)


##### \> Naming formatting of WAV files
- **Numbers**: “number_1.wav”, “number_2.wav” etc.
- **Special sentences**:
   - beer_1.wav
   - casper_1.wav
   - hungry_1.wav
   - scream.wav
   - time_to_work.wav 
- **Glue sentences**:
   - Half_past.wav
   - It’s.wav
   - oclock.wav
   - Past.wav
   - quarter_past.wav
   - Quarter_to.wav
   - to_.wav

### **Contact**
- Judith Baumann (j.baumann.1@student.rug.nl ) 
- Spyretta Leivaditi (s.leivaditi@student.rug.nl )
- Kirsten Wildenburg (k.wildenburg@student.rug.nl )

### **License**
CC BY-NC-SA