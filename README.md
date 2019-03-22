# Mask GPU
A simple tool to expose only specified number of GPUs with desired memory to Tensorflow (and a few more apps, read further). This tool queries GPU free memory values using `nvidia-smi` and assigns `CUDA_VISIBLE_DEVICES` environment variable based on the specified memory and number of GPUs to expose, to expose specific GPUs. Apps such as `tensorflow-gpu` use this information and utilize only the GPUs that are exposed. If your app does not make use of `CUDA_VISIBLE_DEVICES`, then this is probably **not** what you would need.

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

Simply run ``mask-gpu`` to expose 1 GPU (with a minimum of 1024MiB free memory)
```sh
`mask-gpu`
# Remember to wrap mask-gpu in ` symbol
# Or else mask-gpu will print the command
# and you will have to manually execute it
```

## Specifying Options

By default `mask-gpu` seraches for GPUs with atleast 1024M free memory and allots 1 GPU
```sh
mask-gpu --info --min_memory 1024
# mask-gpu -i -m 1024                <--- Same as above
# Info does not execute any commands

`mask-gpu --expose 1 --min_memory 1024`
# `mask-gpu -e 3 -m 1024`            <--- Same as above
# Remember to wrap mask-gpu in ` symbol
```
You can specify your own options using the above as the template

## Unmask all (Revert)

To unmask all GPUs, i.e, to revert to what it was before using `mask-gpu`

```sh
`mask-gpu --unmask-all`
# `mask-gpu -u`                      <--- Same as above
# Remember to wrap mask-gpu in ` symbol
```

NOTE: This command will clear `CUDA_VISIBLE_DEVICES` and hence it will be erased when executing the above command

## Licence

The MIT License

Copyright (c) 2019 Saravanabalagi Ramachandran

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
