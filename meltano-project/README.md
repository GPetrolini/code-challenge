- Desafio Indicium - Minha Jornada com Dados e Pipelines

Olá! Este projeto foi minha tentativa de construir um pipeline de dados robusto, utilizando algumas ferramentas incríveis como Meltano, Airflow (na plataforma Astro), e PostgreSQL. O desafio era extrair, transformar e carregar dados de diferentes fontes para um banco de dados, e depois gerar um arquivo CSV com os resultados de uma consulta específica.

- O Que Usei Nessa Aventura

- **Meltano:** Para conectar e mover os dados de um lugar para outro.
- **Airflow (Astro):** Para organizar e automatizar todo o fluxo de dados.
- **PostgreSQL:** Nosso banco de dados, tanto como fonte quanto destino.
- **Docker:** Para garantir que tudo rodasse perfeitamente, sem problemas de instalação.
- **Python:** Para criar os scripts que transformam e consultam os dados.

- Como o Projeto Está Organizado

├── dags/
│   └── indicium_challenge.py  # O coração do Airflow, nosso DAG
├── data/                     # Onde os dados moram
├── query_script.py            # O script que faz a mágica com o SQL
├── docker-compose.yml         # O mapa do Docker
└── README.md                 # Este arquivo, seu guia


- Como Tentei Fazer Tudo Funcionar

1.  **Primeiros Passos:**
    * Configurei o ambiente Docker com todas as ferramentas necessárias.
    * Organizei os dados de origem no diretório `data/`.

2.  **Meltano em Ação:**
    * Usei o Meltano para conectar ao PostgreSQL e aos arquivos CSV, e mover os dados para o banco de dados de destino.

3.  **Airflow no Comando:**
    * Criei um DAG no Airflow para automatizar a execução do script `query_script.py`, que gera o arquivo `result.csv`.

- O Que Aprendi e os Desafios

* **Meltano e Docker:** A instalação do Meltano no Docker me deu um nó na cabeça! Tive que mexer no `Dockerfile` várias vezes até entender o que estava acontecendo.
* **Configurações do PostgreSQL:** As variáveis de ambiente para o PostgreSQL também me deram trabalho. Mas consegui ajustar tudo no `docker-compose.yml` e no `query_script.py`.
* **Tempo:** O tempo foi meu maior inimigo. Não consegui completar tudo como queria, mas aprendi muito no processo.

- Resultados

* Infelizmente, devido aos problemas que encontrei, não consegui gerar o `result.csv` como planejado.
* Mas, o código está aqui, pronto para ser explorado e melhorado!

- Observações

* As configurações de conexão com o PostgreSQL estão no `docker-compose.yml` e no `query_script.py`.
* O DAG do Airflow automatiza a execução do script `query_script.py`.

- Referências

* **Sites:**
    * [Extract CSV data and load it to PostgreSQL using Meltano ELT](https://dev.to/zompro/extract-csv-data-and-load-it-to-postgresql-using-meltano-elt-4ipf)
    * [Install Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli/?tab=linux)
    * [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    * [target-csv](https://github.com/MeltanoLabs/target-csv)
    * [target-postgres](https://github.com/MeltanoLabs/target-postgres)
    * [tap-postgres](https://github.com/MeltanoLabs/tap-postgres)
    * [Containerization](https://docs.meltano.com/guide/containerization/)
    * [Getting Started](https://docs.meltano.com/getting-started/)

* **Vídeos:**
    * [Meltano ELT: Extract CSV data and load it to PostgreSQL](https://www.youtube.com/watch?v=01MR38eDXz8)
    * [Airflow on Astro](https://www.youtube.com/watch?v=CGxxVj13sOs)

- Contato

Se tiver alguma dúvida, me manda um e-mail!