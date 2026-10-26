# 🚀 Automated Market Data Lakehouse (Serverless Architecture)

Este projeto implementa uma arquitetura de dados moderna e resiliente de custo zero (Serverless), operando de ponta a ponta (End-to-End) dentro do ecossistema do GitHub.

## 🛠️ Tecnologias Utilizadas
* **Orquestração e DataOps:** GitHub Actions (pipelines automatizados e rotinas agendadas via CRON).
* **Processamento e Transformação:** Python 3.11 & DuckDB (mecanismo OLAP de altíssima performance).
* **Armazenamento (Data Lakehouse):** Arquivos colunares de alta performance (formato Parquet) na camada Gold.
* **Visualização de Dados:** Plotly Express (Dashboards interativos estáticos) hospedados no GitHub Pages.

## 📈 Diferenciais Técnicos (Nível Sênior)
* **Arquitetura Tolerante a Falhas:** Mecanismo de fallback (plano B) implementado caso a API principal sofra indisponibilidade ou rate limit.
* **Idempotência no Pipeline:** O script trata e unifica os dados diários de forma inteligente, evitando a duplicação de registros para o mesmo período de processamento.
* **Deploy Automatizado (CI/CD):** Deploy automático do dashboard em ambiente web sempre que há ingestão de dados bem-sucedida.

