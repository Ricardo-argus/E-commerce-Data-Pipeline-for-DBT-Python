# Projeto de Pipeline de Dados - Ecommerce

Este projeto implementa um pipeline de dados para um cenário de **ecommerce**, utilizando **Python, dbt e SQL**.  
O objetivo é construir uma arquitetura de dados organizada em camadas (bronze, silver, gold), garantindo qualidade, rastreabilidade e documentação clara para análises.

---

##  Visão Geral

- **Camada Bronze**: ingestão de dados brutos (ex.: `ecommerce_csv.csv`).  
- **Camada Silver**: limpeza, padronização e enriquecimento dos dados.  
- **Camada Gold**: modelos analíticos prontos para consumo em relatórios e dashboards.  
- **Testes e Qualidade**: implementados via dbt para garantir consistência.  
- **Documentação e DAG**: gerada automaticamente pelo dbt para visualização das dependências.

---

##  Arquitetura

Fluxo de dados:

1. **Ingestão**: arquivos CSV são carregados na camada bronze.  
2. **Transformação**: modelos SQL no dbt aplicam regras de negócio e qualidade.  
3. **Validação**: testes garantem integridade (ex.: valores não nulos, preços positivos).  
4. **Consumo**: camada gold disponibiliza dados prontos para análise.

---

##  Estrutura do Projeto

- **data/** → dados brutos e imagens de documentação (`ecommerce_csv.csv`, `LinearGraphdbt.png`)  
- **dbt/** → parte principal de transformação
  - **models/** → modelos SQL organizados em `bronze`, `silver`, `gold`
  - **tests/** → testes customizados
  - **seeds/** → dados estáticos (`paises.csv`)
  - **snapshots/** → controle de histórico (`clientes_snapshot.sql`)
  - **macros/** → funções reutilizáveis
  - **analyses/** → queries exploratórias
  - **dbt_project.yml** → configuração principal
- **notebooks/** → análises exploratórias em Python  
- **src/** → scripts auxiliares em Python  
- **requirements.txt** → dependências do projeto  
- **run.py** → execução do pipeline em Python  

---

##  Configuração

**1. Crie e configure o ambiente virtual:**
```bash
    python -m venv venv
```
```bash
    venv\Scripts\activate 
```
```bash
    pip install -r requirements.txt
```
### Objetivo

Este projeto foi desenvolvido como parte de um estudo prático em engenharia de dados, servindo como portfólio para demonstrar habilidades em:- Python para ingestão e automação
- dbt para transformação e qualidade
- SQL para modelagem de dados
- Documentação clara e visualização de DAGs
