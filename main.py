import os
import zipfile
import tabula
import pandas as pd

# Extraindo todas as tabelas do PDF
tables = tabula.read_pdf("Anexo_1.pdf", pages='all', lattice=True)
# Concatenar todas as tabelas em um único DataFrame
all_tables = pd.concat(tables, ignore_index=True)

all_tables.columns = all_tables.columns.str.replace("OD", "Seg. Odontológica")
all_tables.columns = all_tables.columns.str.replace("AMB", "Seg. Ambulatorial")

# Salvar o DataFrame concatenado em um único arquivo CSV
all_tables.to_csv("rol_procedimentos.csv", index=False)
print(tables)

zip_file = "Teste_Rafael.zip"

# Compactar o arquivo CSV em um arquivo ZIP
with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write("rol_procedimentos.csv", os.path.basename("rol_procedimentos.csv"))

