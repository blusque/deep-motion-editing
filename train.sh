#!/bin/bash

nohup python style_transfer/train.py --gpu $1 > style_transfer/mixamo.log &2 > 1 &
