from ddgs import DDGS

def search_web(query: str, max_results: int = 5) -> str:

    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append(
                f"Title: {r['title']}\n"
                f"Body: {r['body']}\n"
            )

    return "\n\n".join(results)