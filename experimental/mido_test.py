import mido

# realtime_output = mido.open_output('my_realtime_output_device')
# realtime_input = mido.open_input('my_input_device')

# # Messages created by realtime_input are sent to the realtime_output as they are received
# realtime_input.callback = realtime_output.send

# # Create another output for handling a MIDI file
# midi_file_output = mido.open_output('my_midi_file_output_device')

for i in range(5):
    for message in mido.MidiFile('midi-python-test.mid').play():
        print(message)