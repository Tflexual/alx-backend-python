import asyncio
import aiosqlite

async def async_fetch_users():
    async with aiosqlite.connect("my_database.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()

async def async_fetch_older_users():
    async with aiosqlite.connect("my_database.db") as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            return await cursor.fetchall()

async def fetch_concurrently():
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    print("All users:", results[0])
    print("Users older than 40:", results[1])

# Run the async function
asyncio.run(fetch_concurrently())
