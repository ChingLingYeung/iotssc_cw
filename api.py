import numpy as np
import time
from mbed_cloud.foundation import Device
from mbed_cloud import ConnectAPI
from mbed_cloud.subscribe import *
from mbed_cloud.subscribe.channels import ResourceValues
# from mbed_cloud import ResourceValues

api = ConnectAPI()

def get_resourceValues():
    channel = api.subscribe(ResourceValues(resource_path=['/3313/*', '/3334/*']))
    samples = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for result in channel:
        path = result.block().get('resource_path')
        if path == '/3313/0/5702':
            samples[0] = float(result.block().get('payload').decode())
        elif path == '/3313/0/5703':
            samples[1] = float(result.block().get('payload').decode())
        elif path == '/3313/0/5704':
            samples[2] = float(result.block().get('payload').decode())
        elif path == '/3334/0/5702':
            samples[3] = float(result.block().get('payload').decode())
        elif path == '/3334/0/5703':
            samples[4] = float(result.block().get('payload').decode())
        elif path == '/3334/0/5704':
            samples[5] = float(result.block().get('payload').decode())
        yield samples

# while True:
#     for sample in get_resourceValues():
#         print(sample)

    

# channel = api.subscribe(ResourceValues(resource_path=['/3313/*', '/3334/*']))
# for result in channel:
#   print(result.block())

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

