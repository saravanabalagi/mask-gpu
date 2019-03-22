# Version of mask_gpu
__version__ = "0.0.1"

import subprocess as sp
import os

def mask_unused_gpus(expose=1, min_memory=1024, reverse=False, unmask_all=False, console_log=False):

  if unmask_all:
      command = 'export CUDA_VISIBLE_DEVICES='
      print(command)
      return

  available_gpus = get_available_gpus(min_memory, reverse, console_log=False)
  if len(available_gpus) < expose:
    echo_string = 'echo '
    if console_log: echo_string = ""
    print('{}Found only {} usable GPU(s) with atleast {}MiB free memory in the system; Can\'t expose {} GPU(s)'.format( echo_string, len(available_gpus), min_memory, expose ))
    return

  set_visible_devices = ','.join(map(str, available_gpus[:expose]))
  command = 'export CUDA_VISIBLE_DEVICES={}'.format(set_visible_devices)

  if console_log:
      print('Generating command for exposing {} GPU(s)...'.format(expose))
      print('Visible GPUs will be: {} -> {}'.format(len(set_visible_devices), available_gpus[:expose]))
      print('=========================================')
      print('Run the following command in your shell:')
      print("  {}".format(command))
      print('=========================================')
      print()

  else: print(command)
  return

def get_available_gpus(min_memory=1024, reverse=False, console_log=True):
  COMMAND = "nvidia-smi --query-gpu=memory.free --format=csv"

  try:
    if console_log: print('Finding GPUs with a minimum of {}MiB free memory...'.format(min_memory))
    _output_to_list = lambda x: x.decode('ascii').split('\n')[:-1]
    memory_free_info = _output_to_list(sp.check_output(COMMAND.split()))[1:]
    memory_free_values = [int(x.split()[0]) for i, x in enumerate(memory_free_info)]
    available_gpus = [i for i, x in enumerate(memory_free_values) if x > min_memory]
    if console_log: print('GPUs available: {} -> {}'.format(len(available_gpus), available_gpus))
    return sorted(available_gpus, reverse=reverse)

  except Exception as e:
    print('"nvidia-smi" is probably not installed. Could not retrieve GPU information', e)
