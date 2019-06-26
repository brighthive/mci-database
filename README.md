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

## Pulling updates downstream

The `master-client-index` and `mci-matching-service` require this repo in their respective Pipfiles. The Pipfile.lock lists the dependency, like so:

```
"mci-database": {
    "editable": true,
    "git": "https://github.com/brighthive/mci-database.git",
    "ref": "53086d7fc8816b79f1fcb6845af54d1ab7620dd2"
}
```

The "ref" attribute points to a particular commit: this should be the most recent commit to master.

The Pipfile contains the reference as such:

```
mci-database = {editable = true,git = "https://github.com/brighthive/mci-database.git",ref = "master"}
```

If you find that your MCI container or matching service do not have the correct migrations, then check the "ref" number. You can also manually uninstall and re-install this repo with:

```
pipenv uninstall mci-database
pipenv install -e git+https://github.com/brighthive/mci-database.git@master#egg=mci_database
```