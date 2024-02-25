import pandas as pd 
from jinja2 import Environment, FileSystemLoader

# Definimos la configuración de jinja
file_loader = FileSystemLoader('md_template')
env = Environment(loader=file_loader)

# Cargamos el template
template_output_tables = env.get_template('practica_02_md.template')

benchmarks = ["fs-bw-sas-read", "fs-bw-sas-write", "fs-iops-sas-randread", "fs-iops-sas-randwrite", "fs-latency-sas-randread", "fs-latency-sas-randwrite"]
devices = ["ext4", "raid0", "raid1", "raid5", "raid6", "raid10"]

# Enviamos la lista de tablas al template
output = template_output_tables.render(benchmarks = benchmarks, devices = devices)

with open("doc/entregable/src/practica_02.md", "w") as text_file:
    text_file.write(output)
