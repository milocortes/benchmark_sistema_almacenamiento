#!/bin/bash

benchmarks=( "fs-bw-sas-read.fio" "fs-bw-sas-write.fio" "fs-iops-sas-randread.fio" "fs-iops-sas-randwrite.fio" "fs-latency-sas-randread.fio" "fs-latency-sas-randwrite.fio" )
blocksizes=( "512" "1k" "2k" "4k" "8k" "16k" "32k" "64k" "128k" "256k" "512k" "1M" )

for benchmark in "${benchmarks[@]}"
do
    for blocksize in "${blocksizes[@]}"
    do
    
    echo "Benchmark: $benchmark. Block Size : $blocksize"

    done
done