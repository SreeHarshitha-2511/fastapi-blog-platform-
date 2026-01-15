"""
Core configuration for the application.

For now this keeps the database URL in one place so it can be
re-used both by the application and Alembic.
"""

DATABASE_URL = "postgresql://postgres:root@localhost:5432/fastapi"

