
# Dagster Orchestration Layer

This use case is documented step by step on [Configure Airbyte Connections with Python (Dagster)](https://airbyte.com/tutorials/configure-airbyte-with-python-dagster). Below is a summary on how to get started quickly.

## Getting started
setup virtual env, dependencies:
```bash
cd stargazer
pip install -e ".[dev]"
```

If you try to kick off a run immediately, it will fail, as there is no source data to ingest/transform, nor is there an active Airbyte connection. To get everything set up properly, read on.

## Set up local Postgres

We'll use a local postgres instance as the destination for our data. You can imagine the "destination" as a data warehouse (something like Snowflake).

To get a postgres instance with the required source and destination databases running on your machine, you can run:

```bash
docker pull postgres
docker run --name local-postgres -p 5433:5433 -e POSTGRES_PASSWORD=postgres -d postgres
```

## Set up Airbyte

Now, you'll want to get Airbyte running locally. The full instructions can be found [here](https://docs.airbyte.com/deploying-airbyte/local-deployment), but if you just want to run some commands (in a separate terminal):

```bash
git clone https://github.com/airbytehq/airbyte.git
cd airbyte
docker-compose up
```

## Set up dbt

Install dbt dependencies by running:

```bash
cd dbt_project_1
dbt deps 
```

```bash
cd dbt_project_2
dbt deps 
```

## Set up data and connections

```bash
dagster-me check --module assets_modern_data_stack.my_asset:airbyte_reconciler
```

```bash
dagster-me apply --module assets_modern_data_stack.my_asset:airbyte_reconciler
```
➡️ Make sure you set the environment variable `AIRBYTE_PASSWORD` on your laptop. The default password is `password`. As well as  [create](https://github.com/settings/tokens) a token  `AIRBYTE_PERSONAL_GITHUB_TOKEN` for fetching the stargazers from the public repositories.

```bash
export AIRBYTE_PASSWORD=password
export AIRBYTE_PERSONAL_GITHUB_TOKEN=your-token
```

## Start the UI of Dagster called Dagit

```bash
export DAGSTER_HOME=~"/dagster_home"
export AIRBYTE_PASSWORD=password
export POSTGRES_PASSWORD=postgres
dagster-daemon run -m assets_modern_data_stack.my_asset
```

To startup the dagster UI run:
```bash
export DAGSTER_HOME=~"/dagster_home"
export AIRBYTE_PASSWORD=password
export POSTGRES_PASSWORD=postgres
dagit -m assets_modern_data_stack.my_asset
````

You'll see the assets of airbyte, dbt that are created automatically in this demo.

You can click "materialize" inside dagit to sync airbyte connections and run dbt.
