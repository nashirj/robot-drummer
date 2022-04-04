from mido import MidiFile

mid = MidiFile('midi-python-test.mid')
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)


# https://stackoverflow.com/questions/27720647/sending-midi-messages-using-python-on-ubuntu