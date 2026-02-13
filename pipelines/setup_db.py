from sqlalchemy import create_engine, text

DB_NAME = "churn_analytics"

def create_database():
    engine = create_engine("postgresql://localhost/postgres")

    with engine.connect() as conn:
        result = conn.execute(
            text(
                "SELECT 1 FROM pg_database WHERE datname=:name"
            ),
            {"name": DB_NAME},
        )

        if not result.scalar():
            conn.execute(text("COMMIT"))
            conn.execute(text(f"CREATE DATABASE {DB_NAME}"))

create_database()
