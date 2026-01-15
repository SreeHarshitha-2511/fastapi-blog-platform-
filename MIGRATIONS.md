# Alembic migrations (project-specific notes)

## Overview
- Alembic is configured to use the application's SQLAlchemy metadata from `app.models`.
- The DB URL is taken from `app.core.config.DATABASE_URL` (wired through `alembic/env.py`).

## Common commands (run from project root)
- Create an autogenerate schema revision:
  virenv\Scripts\alembic.exe revision --autogenerate -m "create tables"

- Create an empty revision for manual edits (e.g., data seeding):
  virenv\Scripts\alembic.exe revision -m "seed initial data"

- Apply all migrations:
  virenv\Scripts\alembic.exe upgrade head

- Roll back last migration:
  virenv\Scripts\alembic.exe downgrade -1

- See current DB revision:
  virenv\Scripts\alembic.exe current

## Data migrations
- For data changes (seeding or backfills), create a manual revision and implement `upgrade()`/`downgrade()` using `op.get_bind()` and `sa.text()` to execute SQL safely.
- Example: see `migrations/versions/f069bed027b5_seed_initial_data.py` which creates an `admin` user and a sample blog post.

## Notes
- If Alembic does not detect schema differences (because the DB already has the tables from `Base.metadata.create_all()`), you can either:
  - use `alembic stamp head` to mark the current DB as at the latest revision, or
  - drop the db and run `alembic upgrade head` to have Alembic create tables via migrations.

- Adjust `migrations/env.py` if you use a different package layout or want to source the DB URL from environment variables.
