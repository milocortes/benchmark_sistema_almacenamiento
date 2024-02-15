#!/bin/bash

input_block_size=$1
input_benchmarl_template=$2

size_template_name_run=$((${#input_benchmarl_template}-9))
size_template_name_result=$((${#input_benchmarl_template}-13))

run_file_name="${input_benchmarl_template::$size_template_name_run}" 
result_file_name="${input_benchmarl_template::$size_template_name_result}-$input_block_size.txt"

bash src/build_benchmark.sh $input_block_size $input_benchmarl_template

echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
date
echo "Ejecutamos el benchmark $run_file_name con parámetro $input_block_size"
echo ""
#fio $run_file_name > $result_file_name

#mv $result_file_name output/$result_file_name

rm $run_file_name