import pandas as pd 
import matplotlib.pyplot as plt
import glob
import re
import os

### Obtenemos el nombre de los resultados de los benchmark
benchmark_results = glob.glob("output/*.txt")

benchmarks_test = ["fs-bw-sas-read", "fs-bw-sas-write", "fs-iops-sas-randread", "fs-iops-sas-randwrite", "fs-latency-sas-randread", "fs-latency-sas-randwrite"]
blocksizes = ["512", "1k", "2k", "4k", "8k", "16k", "32k", "64k", "128k", "256k", "512k", "1M"]

results = {benchmark : {blocksize : {"iops" : "", "bw" : "" } for blocksize in blocksizes} for benchmark in benchmarks_test}
results_numeric = {benchmark : {blocksize: {"iops" : 0, "bw" : 0 } for blocksize in blocksizes} for benchmark in benchmarks_test}


### Reunimos los resultados

for benchmark_file in  benchmark_results:

    with open(benchmark_file) as file:

        benchmark_name = "-".join(benchmark_file.split("/")[-1].split("-")[:-1])
        blocksize = benchmark_file.split("-")[-1].split(".")[0]
        data = "".join([i for i in file.readlines()])

        iops_index = data.find("IOPS=")
        bw_index = data.find("BW=")

        iops_data = data[iops_index:].split(",")[0].split("=")[-1]
        bw_data = data[bw_index:].split(" ")[0].split("=")[-1]

        iops_data_num = int(re.findall(r'\d+', iops_data)[0])
        bw_data_num = int(re.findall(r'\d+', bw_data)[0])

        if not "k" in iops_data:
            iops_data_num = iops_data_num/1000
            
        results[benchmark_name][blocksize]["iops"] = iops_data
        results[benchmark_name][blocksize]["bw"] = bw_data
        
        results_numeric[benchmark_name][blocksize]["iops"] = iops_data_num
        results_numeric[benchmark_name][blocksize]["bw"] = bw_data_num

### Generamos dataframes

dfs_benchmarks_test = {benchmark: None for benchmark in benchmarks_test}
dfs_benchmarks_test_num = {benchmark: None for benchmark in benchmarks_test}

for benchmark in benchmarks_test[:2]:
    
    datos_raw = [[f"{benchmark}.fio", "raid0", blocksize, benchmark_data["bw"], benchmark_data["iops"]]  for blocksize, benchmark_data in results[benchmark].items()]
    datos_raw_numeric = [[f"{benchmark}.fio", "raid0", blocksize, benchmark_data["bw"], benchmark_data["iops"]]  for blocksize, benchmark_data in results_numeric[benchmark].items()]

    dfs_benchmarks_test[benchmark] = pd.DataFrame(datos_raw, columns = ["Métrica", "Directorio", "Block Size", "Band Width [MB/s]", "IOPS"])
    dfs_benchmarks_test_num[benchmark] = pd.DataFrame(datos_raw_numeric, columns = ["Métrica", "Directorio", "Block Size", "Band Width [MB/s]", "IOPS"])

### Guardamos los resultados de cada test en csvs
for benchmark in benchmarks_test[:2]:
    dfs_benchmarks_test[benchmark].to_csv(f"csv/{benchmark}.csv", index = False)

### Generamos las imágenes para cada benchmark


def iops_and_bw(benchmark_name, iops_data, bw_data):
    fig, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_title(f"Benchmark : {benchmark_name}")
    ax1.set_xlabel('IO Block Size')
    ax1.set_ylabel('IOPS[k]', color=color)
    ax1.plot(blocksizes, iops_data, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel("BW[MB/s]", color=color)
    ax2.plot(blocksizes, bw_data, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    fig.tight_layout()
    plt.savefig(f'images/{benchmark_name}_iops_and_bw.jpg')
    plt.clf()

def iops_vs_bw(benchmark_name, iops_data, bw_data):
    plt.plot(dfs_benchmarks_test_num[benchmark]["IOPS"], dfs_benchmarks_test_num[benchmark]["Band Width [MB/s]"])
    plt.xlabel('IOPS[k]')
    plt.ylabel("Ancho de Banda [MB/s]")
    plt.title(f"Benchmark : {benchmark_name}. BW vs IOPS")
    plt.savefig(f'images/{benchmark_name}_iops_vs_bw.jpg')
    plt.clf()

for benchmark in benchmarks_test[:2]:
    iops_and_bw(benchmark, dfs_benchmarks_test_num[benchmark]["IOPS"], dfs_benchmarks_test_num[benchmark]["Band Width [MB/s]"])

for benchmark in benchmarks_test[:2]:    
    iops_vs_bw(benchmark, dfs_benchmarks_test_num[benchmark]["IOPS"], dfs_benchmarks_test_num[benchmark]["Band Width [MB/s]"])