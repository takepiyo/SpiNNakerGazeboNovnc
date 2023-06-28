import pyNN.spiNNaker as p


def send_spikes(label, sender):
    sender.send_spike(label, 0, send_full_keys=True)


def receive_spikes(label, time, neuron_ids):
    for neuron_id in neuron_ids:
        print("receive spike at time {} from {}--{}".format(time, label, neuron_id))


live_spikes_connection = p.external_devices.SpynnakerLiveSpikesConnection(receive_labels=["pop_1"], send_labels=["spike_injector"], local_port=12345)

live_spikes_connection.add_start_resume_callback("spike_injector", send_spikes)

live_spikes_connection.add_receive_callback("pop_1", receive_spikes)

while True:
    try:
        a = 1
    except KeyboardInterrupt:
        print('\n . . .\n')
        break
