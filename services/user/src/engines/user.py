"""

"""

from sqlalchemy.ext.asyncio import create_async_engine

from ..configurations.engine import engine_configuration_variables


user_engine = create_async_engine(

    # Database connection URL.
    # Example:
    # postgresql+asyncpg://username:password@host:5432/database
    url=engine_configuration_variables.URL,

    # Enables SQL query logging in terminal.
    # Useful during development/debugging.
    # Should usually be False in production.
    echo=engine_configuration_variables.ECHO,

    # Number of persistent database connections
    # maintained inside the connection pool.
    # These connections stay ready for reuse.
    pool_size=engine_configuration_variables.POOL_SIZE,

    # Maximum temporary extra connections allowed
    # beyond pool_size during high traffic/load.
    max_overflow=engine_configuration_variables.MAX_OVERFLOW,

    # Maximum number of seconds to wait for
    # an available connection before raising timeout error.
    pool_timeout=engine_configuration_variables.POOL_TIMEOUT,

    # Recreates database connections after specified seconds
    # to avoid stale/disconnected connections.
    # Useful for cloud databases/load balancers.
    pool_recycle=engine_configuration_variables.POOL_RECYCLE,

    # Enables SQLAlchemy 2.0 style behavior/features.
    # Recommended for modern SQLAlchemy usage.
    future=engine_configuration_variables.FUTURE,

    # Additional asyncpg driver configuration.
    connect_args={

        "server_settings": {

            # Disables PostgreSQL JIT (Just-In-Time compilation).
            # Helps avoid some asyncpg/PostgreSQL performance
            # and compatibility issues in certain environments.
            "jit": "off",
        }
    },
)
