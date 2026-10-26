import os
import datetime
import requests
import pandas as pd
import duckdb
import plotly.express as px

print("Iniciando captura de dados na API pública...")
url = "https://coingecko.com"
response = requests.get(url).json()

hoje = datetime.date.today().strftime("%Y-%m-%d")
novos_dados = [
    {"data": hoje, "ativo": "Bitcoin", "preco_usd": response["bitcoin"]["usd"], "variacao_24h": response["bitcoin"]["usd_24h_change"]},
    {"data": hoje, "ativo": "Ethereum", "preco_usd": response["ethereum"]["usd"], "variacao_24h": response["ethereum"]["usd_24h_change"]}
]
df_novos = pd.DataFrame(novos_dados)

os.makedirs("data/gold", exist_ok=True)
arquivo_gold = "data/gold/metricas_ativos.parquet"

if os.path.exists(arquivo_gold):
    df_historico = duckdb.query(f"SELECT * FROM read_parquet('{arquivo_gold}')").df()
    df_historico = df_historico[df_historico['data'] != hoje]
    df_final = pd.concat([df_historico, df_novos], ignore_index=True)
else:
    df_final = df_novos

duckdb.query(f"COPY df_final TO '{arquivo_gold}' (FORMAT PARQUET)")
print("Camada Gold updated!")

print("Gerando visualizações gráficas...")
df_grafico = duckdb.query(f"SELECT * FROM read_parquet('{arquivo_gold}')").df()

fig = px.line(df_grafico, x="data", y="preco_usd", color="ativo", 
              title="Evolução de Preço dos Ativos - Lakehouse Serverless",
              labels={"data": "Data", "preco_usd": "Preço (USD)", "ativo": "Criptoativo"},
              markers=True)

os.makedirs("docs", exist_ok=True)
fig.write_html("docs/index.html")
print("Dashboard atualizado com sucesso na pasta /docs!")
