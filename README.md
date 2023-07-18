DBT-Fundamentals

[Course Link](https://courses.getdbt.com/courses/take/fundamentals)

1. Make a virtual environment
2. `pip install -r requirements.txt` to setup you `dbt-core` and `dbt-sqlite`
3. `python init_db.py` to initialize the sqlite database `db.db` in `./data`

## init_db.py

This will create the `customers`, `orders`, and `stripe` tables in the sqlite
database for dbt transformations to consume as sources

## ~/.dbt/project.yml

You need to configure the sqlite connector in `~/.dbt/profiles.yml`.

```yaml
outputs:
  dev:
    type: sqlite
    threads: 1
    database: "database"
    schema: "main"
    schemas_and_paths:
      main: "/Users/npayne81/work/dbt-fundamentals/data/db.db"
    schema_directory: "/Users/npayne81/work/dbt-fundamentals/data"
```
