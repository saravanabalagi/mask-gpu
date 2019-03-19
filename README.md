# Mask GPU
A simple tool to expose only specified number of GPUs with desired memory to Tensorflow

## Dependencies
- nvidia-smi

## Installation
```sh
pip install mask-gpu
```
## Quick Start

To show available GPUs info
```sh
mask-gpu --info
# Outputs the following
# Finding GPUs with a minimum of 1024MiB free memory...
# GPUs available: 6 -> [0, 1, 4, 5, 6, 7]
```

Simply run `mask-gpu` to expose 1 GPU
```sh
mask-gpu
# Finding GPUs with a minimum of 1024MiB free memory...
# GPUs available: 6 -> [0, 1, 4, 5, 6, 7]
# ---------------------
# Alloting 1 GPU(s)...
# Visible GPUs: 1 -> [0]
```
## Specifying Options

By default `mask-gpu` seraches for GPUs with atleast 1024M free memory and allots 1 GPU
```sh
mask-gpu --info --min_memory 1024
# mask-gpu -s -m 1024                <--- Same as above

mask-gpu --expose 1 --min_memory 1024
# mask-gpu -e 3 -m 1024              <--- Same as above
```
You can specify your own options using the above as the template
