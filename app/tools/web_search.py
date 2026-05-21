from duckduckgo_search import DDGS


async def web_search(query: str):

    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=3)]

    if not results:
        return "No results found."

    # Combine top results
    combined_result = "\n\n".join([
        f"Title: {r['title']}\nSnippet: {r['body']}"
        for r in results
    ])

    return combined_result