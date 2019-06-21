# mci-database

This repo contains the models and migrations for the [`master-client-index`](https://github.com/brighthive/master-client-index) and [mci-matching-service](https://github.com/brighthive/mci-matching-service).

## Generating a migration

This repo operates outside of a Flask app context. Migrations can only be generated with [the `revision` command](https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script). 

```
# cd into the directory with `alembic.ini`
cd mci_database/db/migrations

# create a new migration script in mci_database/db/migrations/versions
alembic revision
```

Add content to the `upgrade` and `downgrade` functions. 