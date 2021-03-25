import numpy as np
import time
from mbed_cloud import ConnectAPI
from mbed_cloud.subscribe import *
from mbed_cloud.subscribe.channels import ResourceValues

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
            dps = float(result.block().get('payload').decode())
            samples[3] = np.deg2rad(dps)
        elif path == '/3334/0/5703':
            dps = float(result.block().get('payload').decode())
            samples[4] = np.deg2rad(dps)
        elif path == '/3334/0/5704':
            dps = float(result.block().get('payload').decode())
            samples[5] = np.deg2rad(dps)
        yield samples

