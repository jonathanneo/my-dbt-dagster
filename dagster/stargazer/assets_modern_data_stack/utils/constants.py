from dagster_postgres.utils import get_conn_string
from dagster._utils import file_relative_path


# AIRBYTE_CONFIG = {"host": "localhost", "port": "8000"}
DBT_PROJECT_DIR1 = file_relative_path(__file__, "../../transformation_dbt1")
DBT_PROFILES_DIR1 = file_relative_path(__file__, "../../transformation_dbt1/config")
DBT_CONFIG1 = {"project_dir": DBT_PROJECT_DIR1, "profiles_dir": DBT_PROFILES_DIR1}
DBT_PROJECT_DIR2 = file_relative_path(__file__, "../../transformation_dbt2")
DBT_PROFILES_DIR2 = file_relative_path(__file__, "../../transformation_dbt2/config")
DBT_CONFIG2 = {"project_dir": DBT_PROJECT_DIR2, "profiles_dir": DBT_PROFILES_DIR2}

PG_DESTINATION_CONFIG = {
    "username": "postgres",
    "password": "password",
    "host": "localhost",
    "port": 5433,
    "database": "postgres",
}

POSTGRES_CONFIG = {
    "con_string": get_conn_string(
        username=PG_DESTINATION_CONFIG["username"],
        password=PG_DESTINATION_CONFIG["password"],
        hostname=PG_DESTINATION_CONFIG["host"],
        port=str(PG_DESTINATION_CONFIG["port"]),
        db_name=PG_DESTINATION_CONFIG["database"],
    )
}
