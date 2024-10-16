#!/bin/bash

cd ./data_proc
bash ./gen_dataset.sh
cd ..
bash ./train.sh