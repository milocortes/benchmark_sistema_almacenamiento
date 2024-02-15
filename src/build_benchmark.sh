#!/bin/bash

input_block_size=$1
input_benchmarl_template=$2
size_template_name=$((${#input_benchmarl_template}-9))

sed -e "s/\${blocksize}/$input_block_size/" template/$input_benchmarl_template > "${input_benchmarl_template::$size_template_name}"