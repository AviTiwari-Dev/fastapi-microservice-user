"""

"""

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from ..engines.user import user_engine


user_session = async_sessionmaker(

    # Database engine used by the session factory.
    # All sessions created from this factory will use
    # this engine for database connections/queries.
    bind=user_engine,

    # Session class to use.
    # AsyncSession enables asynchronous database operations
    # using async/await syntax.
    class_=AsyncSession,

    # Prevents SQLAlchemy from expiring ORM object data
    # immediately after commit().
    #
    # If False:
    # object attributes remain accessible after commit
    # without requiring another database query.
    #
    # If True:
    # accessing attributes after commit may trigger
    # automatic database reload.
    expire_on_commit=False,

    # Automatically flushes pending SQL changes
    # before query execution.
    #
    # Example:
    # session.add(user)
    # session.execute(select(User))
    #
    # SQLAlchemy automatically sends INSERT/UPDATE
    # statements before executing SELECT query.
    autoflush=True,
)
