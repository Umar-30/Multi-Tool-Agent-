import aiosqlite

DB_NAME = "agent.db"


async def init_db():

    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute("""
            CREATE TABLE IF NOT EXISTS searches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT,
                result TEXT
            )
        """)

        await db.commit()


async def save_search(
    query: str,
    result: str
):

    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            """
            INSERT INTO searches
            (query, result)
            VALUES (?, ?)
            """,
            (query, result)
        )

        await db.commit()