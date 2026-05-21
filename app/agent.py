from app.tools.web_search import web_search
from app.tools.database import save_search
from app.tools.email_tool import send_email

from app.services.cohere_client import co


class MultiToolAgent:

    async def run(
        self,
        user_prompt: str,
        email: str
    ):

        # AI decides search query
        response = co.chat(
            model="command-a-03-2025",
            message=f"""
            Extract the best web search query
            from this request:

            {user_prompt}

            Return ONLY the search query.
            """
        )

        search_query = response.text.strip()
        print(f"Generated Search Query: {search_query}")

        # Web Search
        search_result_raw = await web_search(
            search_query
        )
        print(f"Raw Search Snippets: {search_result_raw[:100]}...")

        # AI Summarizes/Answers based on search results
        response_final = co.chat(
            model="command-a-03-2025",
            message=f"""
            The user asked: {user_prompt}
            
            Based on these search results, provide a concise and helpful answer:
            {search_result_raw}
            
            If the search results are empty or not relevant, honestly tell the user that you couldn't find specific news but provide what you know or suggest a better query.
            """
        )
        
        result = response_final.text.strip()
        print(f"Final AI Answer: {result[:100]}...")

        # Save to DB
        await save_search(
            search_query,
            result
        )
        print("Saved to Database.")

        # Email Result
        print(f"Sending email to {email}...")
        await send_email(
            to_email=email,
            subject="AI Search Result",
            body=result
        )

        return {
            "query": search_query,
            "result": result
        }