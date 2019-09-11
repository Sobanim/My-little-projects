import paho.mqtt.client as mqtt

broker_address = "192.168.100.151"

client = mqtt.Client("dmytro_broker") # name of broker
client.connect(broker_address) # ip adress broker
client.publish("semaphore", "[0, 0, 0, 0]") # send to semaphore
