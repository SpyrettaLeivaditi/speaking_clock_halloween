import base64
import datetime
import io
import numpy as np
import librosa
import librosa.display

from datetime import datetime
from flask import Flask, make_response, render_template
from flask_cors import CORS
from flask_restful import reqparse, Api, Resource
from scipy.io.wavfile import write

# flask project set up
app = Flask(__name__)
api = Api(app)

# bypass CORS https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
CORS(app, origins="http://localhost:5000", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
     supports_credentials=True, intercept_exceptions=False)

# Render main page (index.html)
class MainPage(Resource):
    def __init__(self):
        super(MainPage, self).__init__()

    def get(self):
        return make_response(render_template('index.html'))

# Back end API that serves the clock
class SpeakTheTime(Resource):
    def __init__(self):
        # argument parsing
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('no_input', type=str)
        self.parser.add_argument('obtained_time', type=str)
        super(SpeakTheTime, self).__init__()

    def get(self):
        args = self.parser.parse_args()
        empty_input = args['no_input']=='true'
        if empty_input:
            time_input = datetime.now().time().strftime("%I:%M %p")
        else:
            time_input = args["obtained_time"]
        sr, audio = get_time_recording(time_input)
        bytes_wav = bytes()
        byte_io = io.BytesIO(bytes_wav)
        write(byte_io, sr, audio)
        wav_bytes = byte_io.read()
        audio_data = base64.b64encode(wav_bytes).decode('UTF-8')
        return audio_data


def get_time_recording(time_input):
    """
    parses the provided time (12 hour mode), picks specific recording segments and composes the final
    wav file.
    :param time_input: the provided time in 12 hour mode (e.g., 11:28 AM)
    :return: sr, final_segment (sampling rate, np array of the final wav recording)
    """
    split_time = time_input.split(':')
    hours, minutes, is_am = int(split_time[0]), int(split_time[1].split(' ')[0]), (split_time[1].split(' ')[1] == 'AM')

    # special time cases
    if hours == 12 and minutes == 0 and is_am:
        # scream, casper1
        scream, sr = librosa.load("The_clock_recordings/tracks/sentences/scream.wav")
        casper, sr = librosa.load("The_clock_recordings/tracks/sentences/casper_1.wav")
        final_segment = np.concatenate((scream, casper))
    elif hours == 9 and minutes == 0 and is_am:
        # its time to work
        final_segment, sr = librosa.load("The_clock_recordings/tracks/sentences/time_to_work.wav")
    elif hours == 12 and minutes == 30 and not is_am:
        # it's half past i am hungry
        final_segment, sr = librosa.load("The_clock_recordings/tracks/sentences/hungry_1.wav")
    elif hours == 6 and minutes == 0 and not is_am:
        # it's beer oclock
        final_segment, sr = librosa.load("The_clock_recordings/tracks/sentences/beer_1.wav")
    else:  # general time case
        if minutes > 30:
            minutes = 60 - minutes
            if minutes == 15:
                glue_file = "quarter_to"
            else:
                glue_file = "to_"
            hours += 1
        elif 0 < minutes < 30:
            if minutes == 15:
                glue_file = "quarter_past"
            else:
                glue_file = "past"
        elif minutes == 30:
            glue_file = "half_past"
        else:
            glue_file = "oclock_final"

        if hours == 13:
            hours = 1

        # obtain segments
        start_time, sr = librosa.load("The_clock_recordings/tracks/glue_words/it's.wav")
        glue, sr = librosa.load(f"The_clock_recordings/tracks/glue_words/{glue_file}.wav")
        hour_rec, sr = librosa.load(f"The_clock_recordings/tracks/numbers/number_{hours}.wav")
        # compose segment
        if minutes == 0:
            final_segment = np.concatenate((start_time, hour_rec, glue))
        elif minutes == 15 or minutes == 30 or minutes == 45:
            final_segment = np.concatenate((start_time, glue, hour_rec))
        else:
            min_rec, sr = librosa.load(f"The_clock_recordings/tracks/numbers/number_{minutes}.wav")
            final_segment = np.concatenate((start_time, min_rec, glue, hour_rec))

    return sr, final_segment

# map resources to paths
api.add_resource(MainPage, '/')
api.add_resource(SpeakTheTime, '/speak_the_time')

if __name__ == '__main__':
    app.run(debug=True)
