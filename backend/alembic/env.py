from alembic import context
from sqlalchemy import engine_from_config, pool
from app.models.db import Base
from app.config import DATABASE_URL

config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)
target_metadata = Base.metadata

def run_migrations_online():
    engine = engine_from_config(
        config.get_section(config.config_ini_section),
        poolclass=pool.NullPool,
    )
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()
