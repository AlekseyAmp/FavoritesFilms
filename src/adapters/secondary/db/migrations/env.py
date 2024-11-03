from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

from src.adapters.secondary.db.tables import metadata
from src.adapters.settings import db_settings

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
section = config.config_ini_section

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def create_dbs(db_uri: str) -> None:
    """Create a database if there is no."""
    if not database_exists(db_uri):
        create_database(db_uri)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.
    """
    context.configure(
        url=str(db_settings.db_sync_url),
        target_metadata=target_metadata,
        literal_binds=True,
        version_table_schema="public",
        include_schemas=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """
    Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.
    """

    # create_dbs(str(db_settings.db_sync_url))

    config.set_section_option(section, "sqlalchemy.url", str(db_settings.db_sync_url))    
    connectable = create_engine(str(db_settings.db_sync_url))

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_schemas=True,
            version_table_schema="public",
        )

        with context.begin_transaction():
            context.run_migrations()

def run_migrations() -> None:
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        run_migrations_online()


run_migrations()
