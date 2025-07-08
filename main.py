from mcp.server.fastmcp import FastMCP
import sqlite3
from typing import List, Dict
import requests
import os

SQLITE_PATH = os.environ.get("SQLITE_PATH")
if not SQLITE_PATH:
    raise ValueError("Please set the SQLITE_PATH environment variable.")

mcp = FastMCP("historyMCP")


def search_page(urls: List[str]) -> Dict[str, str]:
    """
    Get the content of the web page

    intput: urls (List of str)
    output: dict key=url, value=content)
    """
    res = {}
    for url in urls:
        response = requests.get(url)
        if response.ok:
            content = response.text
            res[url] = content
    return res


@mcp.tool()
def read_history() -> List[Dict[str, str]]:
    """
    Read last lines of the history

    Return:
        List[Dict[str, str]] : A list where each item is a dictionnary containing :
            - "title": The title of the web page
            - "url:" The url of the web page
    """

    conn = sqlite3.connect(SQLITE_PATH)
    cur = conn.cursor()
    cur.execute("SELECT url, title FROM urls ORDER BY last_visit_time DESC LIMIT 100;")
    rows = [{"title": row[1], "url": row[0]} for row in cur.fetchall()]
    return rows


if __name__ == "__main__":
    mcp.run(transport="stdio")
