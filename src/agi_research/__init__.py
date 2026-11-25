"""Small, configurable research search client."""
from __future__ import annotations

import httpx


def search(query: str, *, base_url: str, limit: int = 5, timeout: float = 15) -> list[dict[str, str]]:
    """Return search snippets and source URLs from a SearXNG JSON endpoint."""
    if not isinstance(query, str) or not query.strip() or len(query) > 500:
        raise ValueError("query must contain 1–500 characters")
    if not 1 <= limit <= 10:
        raise ValueError("limit must be between 1 and 10")
    if not base_url.startswith(("http://", "https://")):
        raise ValueError("base_url must be an HTTP(S) URL")
    response = httpx.get(base_url.rstrip("/") + "/search", params={"q": query, "format": "json"}, timeout=timeout)
    response.raise_for_status()
    results = response.json().get("results", [])
    return [
        {"title": str(item.get("title") or "")[:500], "url": str(item.get("url") or "")[:2000],
         "snippet": str(item.get("content") or "")[:2000]}
        for item in results[:limit] if isinstance(item, dict)
    ]
