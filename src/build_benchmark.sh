#!/bin/bash

input_block_size=$1
input_benchmarl_template=$2
directorio_test_path=$3

size_template_name=$((${#input_benchmarl_template}-9))

echo "$directorio_test_path"
sed -e "s/\${blocksize}/$input_block_size/" -e "s/\${montajedir}/$directorio_test_path/" template/$input_benchmarl_template > "${input_benchmarl_template::$size_template_name}"