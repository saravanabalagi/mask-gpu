# Version of mask_gpu
__version__ = "0.0.1"

import subprocess as sp
import os

def mask_unused_gpus(expose=1, min_memory=1024):
  available_gpus = get_available_gpus(min_memory)
  print('---------------------')
  if len(available_gpus) < expose:
    print('Found only {} usable GPU(s) in the system'.format( len(available_gpus) ))
    print('Can\'t expose {} GPU(s)'.format(expose))
    return
  set_visible_devices = ','.join(map(str, available_gpus[:expose]))
  print('Exposing {} GPU(s)...'.format(expose))
  os.environ["CUDA_VISIBLE_DEVICES"] = set_visible_devices
  print('Visible GPUs: {} -> {}'.format(len(set_visible_devices), available_gpus[:expose]))

def get_available_gpus(min_memory=1024):
  COMMAND = "nvidia-smi --query-gpu=memory.free --format=csv"

  try:
    print('Finding GPUs with a minimum of {}MiB free memory...'.format(min_memory))
    _output_to_list = lambda x: x.decode('ascii').split('\n')[:-1]
    memory_free_info = _output_to_list(sp.check_output(COMMAND.split()))[1:]
    memory_free_values = [int(x.split()[0]) for i, x in enumerate(memory_free_info)]
    available_gpus = [i for i, x in enumerate(memory_free_values) if x > min_memory]
    print('GPUs available: {} -> {}'.format(len(available_gpus), available_gpus))
    return available_gpus

  except Exception as e:
    print('"nvidia-smi" is probably not installed. Could not retrieve GPU information', e)
