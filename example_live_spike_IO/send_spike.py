import pyNN.spiNNaker as p


def send_spikes(label, sender):
    sender.send_spike(label, 0, send_full_keys=True)


live_spikes_connection = p.external_devices.SpynnakerLiveSpikesConnection(send_labels=["spike_injector"], local_port=12346)

live_spikes_connection.add_start_resume_callback("spike_injector", send_spikes)

while True:
    try:
        a = 1
    except KeyboardInterrupt:
        print('\n . . .\n')
        break
