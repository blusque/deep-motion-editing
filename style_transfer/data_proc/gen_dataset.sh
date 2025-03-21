# #!/bin/bash

# needed=$(getopt -o d --long dataset -- "$dataset")
# data_home_path=/mnt/g/dataset

# while true
# do
#   case
#     -d | --dataset) shift; data_path=$data_home_path$dataset; shift;;
#     *) shift; break;;
#   esac
# done

# For xia
# python export_train.py --dataset xia --bvh_path ../data/mocap_xia --output_path ../data/xia --window 32 --window_step 8 --dataset_config ../global_info/xia_dataset.yml
# For bfa
# python export_train.py --dataset bfa --bvh_path /mnt/data0/mjd/mocap_bfa --output_path ../data/bfa --window 32 --window_step 8 --dataset_config ../global_info/bfa_dataset.yml
# For 100style
# python export_train.py --dataset 100style --bvh_path /mnt/data0/mjd/100style --output_path ../data/mixamo --window 32 --window_step 8 --dataset_config ../global_info/mixamo_dataset.yml

python export_train.py --dataset tencent_style --bvh_path ../data/tencent_style_raw --output_path ../data/tencent_style --window 32 --window_step 8 --dataset_config ../global_info/tencent_style.yml
