#!/bin/bash

benchmarks=( "fs-bw-sas-read.fio.template" "fs-bw-sas-write.fio.template" "fs-iops-sas-randread.fio.template" "fs-iops-sas-randwrite.fio.template" "fs-latency-sas-randread.fio.template" "fs-latency-sas-randwrite.fio.template" )
blocksizes=( "512" "1k" "2k" "4k" "8k" "16k" "32k" "64k" "128k" "256k" "512k" "1M" )

test_directorio="$1"

## Crea directorio para almacenar las pruebas
mkdir "/mnt/grp3/$test_directorio/fiotest"
mkdir "output/$test_directorio"

for benchmark in "${benchmarks[@]}"
do
    for blocksize in "${blocksizes[@]}"
    do

    echo "Test en el directorio /mnt/grp3/$test_directorio"
    echo "Benchmark: $benchmark. Block Size : $blocksize"
    #bash src/run_benchmark.sh $blocksize $benchmark $test_directorio
    done
done