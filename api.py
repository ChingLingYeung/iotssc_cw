import numpy as np
import time
from mbed_cloud.foundation import Device
from mbed_cloud import ConnectAPI
from mbed_cloud.subscribe import *
from mbed_cloud.subscribe.channels import ResourceValues
# from mbed_cloud import ResourceValues

api = ConnectAPI()

# for device in Device().list(max_results=10):
#     print("Hello device %s" % device.name)

# notification = api.subscribe(
#   api.subscribe.channels.DeviceStateChanges(device_id=1234)
# ).next().block()
# print(notification)
# channel = subscribe.channels(ResourceValues(resource_path=['/4/0/1', '/3/*']))
# api.subscribe.channels.ResourceValues()
# test = ResourceValues(resource_path=['/4/0/1', '/3/*'])
channel = api.subscribe(ResourceValues(resource_path=['/3313/*', '/3334/*']))
for result in channel:
  print(result.block())

def data_generator():
    interval = 0.2
    x = 1
    while True:
        mu = np.sin(x)
        sigma = np.cos(x) + 1.1
        observations = np.random.normal(loc=mu, scale=sigma, size=500) + np.random.normal(loc=0.01, scale=0.01, size=500)
        yield observations
        sleep_t = np.random.uniform(low=1, high=3)
        time.sleep(sleep_t)
        x += interval * sleep_t

