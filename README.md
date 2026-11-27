# Research

A small SearXNG search client for AIVA's research experiments. It returns titles, URLs and snippets; it does not read full pages or verify claims. Search output is untrusted external content.

Install with `pip install -e .` and configure a SearXNG instance that enables JSON search. For example:

```python
from agi_research import search
results = search("ROS 2 launch documentation", base_url="http://127.0.0.1:8888")
```

The instance receives the search query. Choose an instance you trust. Agentic can use this package as an optional tool.
