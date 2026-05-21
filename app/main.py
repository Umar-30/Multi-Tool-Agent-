import asyncio

from app.agent import MultiToolAgent

from app.tools.database import init_db


async def main():

    await init_db()

    agent = MultiToolAgent()

    result = await agent.run(
        user_prompt="""
        Find latest AI news about OpenAI
        and send me summary
        """,
        email="test@example.com"
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())