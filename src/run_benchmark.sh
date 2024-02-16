#!/bin/bash

input_block_size=$1
input_benchmarl_template=$2
test_directorio=$3


#directorio_test_path="/mnt/grp3/$test_directorio"
#fio_test_path="/mnt/grp3/$test_directorio/fiotest"

size_template_name_run=$((${#input_benchmarl_template}-9))
size_template_name_result=$((${#input_benchmarl_template}-13))

run_file_name="${input_benchmarl_template::$size_template_name_run}" 
result_file_name="${input_benchmarl_template::$size_template_name_result}-$input_block_size-$test_directorio.txt"

bash src/build_benchmark.sh $input_block_size $input_benchmarl_template $test_directorio

echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
date
echo "Ejecutamos el benchmark $run_file_name con parámetro $input_block_size"
echo ""
fio $run_file_name > $result_file_name

mv $result_file_name "output/$test_directorio/$result_file_name"

rm $run_file_name