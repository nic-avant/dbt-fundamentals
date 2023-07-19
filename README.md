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
      main: "/Users/npayne81/work/dbt-fundamentals/data/main.db"
    schema_directory: "/Users/npayne81/work/dbt-fundamentals/data"
```

## dbt build

`doom` is the dbt project directory so `cd doom` and `dbt build`

> Pro-tip: `pip install visidata` then use `vd` to explore `data/data.db` at the terminal!

## dbt test

To run tests on selected models `dbt test --select <model_1> <model_2> ...`

## NOTES

### Pipeline Orchestration

`dbt run --select <model>` will run for just that model. There isn't a separate
api like Kedro has for `from-nodes` or `to-nodes`, but to run downstream models
following the `ref` function you would do `dbt run --select <model>+`

### Naming Conventions

In working on this project, we established some conventions for naming our models.

Sources (src) refer to the raw table data that have been built in the warehouse through a loading process. (We will cover configuring Sources in the Sources module)
Staging (stg) refers to models that are built directly on top of sources. These have a one-to-one relationship with sources tables. These are used for very light transformations that shape the data into what you want it to be. These models are used to clean and standardize the data before transforming data downstream. Note: These are typically materialized as views.
Intermediate (int) refers to any models that exist between final fact and dimension tables. These should be built on staging models rather than directly on sources to leverage the data cleaning that was done in staging.
Fact (fct) refers to any data that represents something that occurred or is occurring. Examples include sessions, transactions, orders, stories, votes. These are typically skinny, long tables.
Dimension (dim) refers to data that represents a person, place or thing. Examples include customers, products, candidates, buildings, employees.
Note: The Fact and Dimension convention is based on previous normalized modeling techniques.
