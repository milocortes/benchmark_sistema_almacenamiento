#!/bin/bash

benchmarks=( "fs-bw-sas-read.fio.template" "fs-bw-sas-write.fio.template" "fs-iops-sas-randread.fio.template" "fs-iops-sas-randwrite.fio.template" "fs-latency-sas-randread.fio.template" "fs-latency-sas-randwrite.fio.template" )
blocksizes=( "512" "1k" "2k" "4k" "8k" "16k" "32k" "64k" "128k" "256k" "512k" "1M" )

for benchmark in "${benchmarks[@]}"
do
    for blocksize in "${blocksizes[@]}"
    do

    echo "Benchmark: $benchmark. Block Size : $blocksize"
    #bash src/run_benchmark.sh $blocksize $benchmark
    done
done