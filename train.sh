#!/bin/bash

nohup python -u style_transfer/train.py --gpu $1 > pretrained.log 2>&1 &
