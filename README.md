Markdown

- Desafio Indicium - Pipeline de Dados com Meltano, Airflow e PostgreSQL

Este projeto implementa um pipeline de dados utilizando Meltano, Airflow (Astro), PostgreSQL e Docker para extrair, transformar e carregar dados de diferentes fontes, gerando um arquivo CSV com os resultados de uma consulta específica.

- Ferramentas Utilizadas

* **Meltano:** Extração e carregamento de dados (ELT).
* **Airflow (Astro):** Orquestração do pipeline de dados.
* **PostgreSQL:** Banco de dados de origem e destino.
* **Docker:** Conteinerização das aplicações.
* **Python:** Scripts de transformação e consulta.

- Estrutura do Projeto

├── dags/
│   └── indicium_challenge.py  # DAG do Airflow
├── data/                     # Dados de origem
├── query_script.py            # Consulta SQL e geração do CSV
├── docker-compose.yml         # Configuração do Docker
└── README.md                 # Este arquivo


- Desafios Principais

* Configuração do Meltano no Docker.
* Gerenciamento das variáveis de ambiente do PostgreSQL.
* Limitação de tempo para conclusão do projeto.

- Observações

* As configurações de conexão com o PostgreSQL estão em `docker-compose.yml` e `query_script.py`.
* O DAG do Airflow automatiza a execução do script `query_script.py`.

- Referências

* [Extract CSV data and load it to PostgreSQL using Meltano ELT](https://dev.to/zompro/extract-csv-data-and-load-it-to-postgresql-using-meltano-elt-4ipf)
* [Install Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli/?tab=linux)
* [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
* [target-csv](https://github.com/MeltanoLabs/target-csv)
* [target-postgres](https://github.com/MeltanoLabs/target-postgres)
* [tap-postgres](https://github.com/MeltanoLabs/tap-postgres)
* [Containerization](https://docs.meltano.com/guide/containerization/)
* [Getting Started](https://docs.meltano.com/getting-started/)
* [Meltano ELT: Extract CSV data and load it to PostgreSQL](https://www.youtube.com/watch?v=01MR38eDXz8)
* [Airflow on Astro](https://www.youtube.com/watch?v=CGxxVj13sOs)
