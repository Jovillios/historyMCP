# HistoryMCP

A Model Context Protocol (MCP) tool that provides access to browser history data from SQLite databases. This tool allows AI assistants to read and analyze your browsing history through the MCP interface.

## Features

- **Browser History Access**: Read the last 100 visited URLs from your browser's SQLite history database
- **MCP Integration**: Seamlessly integrates with MCP-compatible AI assistants
- **Cross-Platform**: Works with any browser that stores history in SQLite format (Chrome, Firefox, Safari, etc.)

## Installation

### Prerequisites

- Python 3.12 or higher
- A browser history SQLite database file

### Setup

1. **Clone or download this repository**

2. **Install dependencies using uv** (recommended):
   ```bash
   uv sync
   ```

3. **Set up your browser history database path**:
   
   You need to set the `SQLITE_PATH` environment variable to point to your browser's history database:

   **Chrome/Chromium:**
   ```bash
   export SQLITE_PATH="$HOME/Library/Application Support/Google/Chrome/Default/History"
   ```

   **Firefox:**
   ```bash
   export SQLITE_PATH="$HOME/Library/Application Support/Firefox/Profiles/*.default/places.sqlite"
   ```

   **Safari:**
   ```bash
   export SQLITE_PATH="$HOME/Library/Safari/History.db"
   ```

   **Note**: You may need to copy the database file to a writable location first, as browsers often lock their database files.

## Usage

### Running the MCP Server

```bash
python main.py
```

The server runs on stdio transport, which is the standard for MCP tools.

### Available Tools

#### `read_history()`

Returns the last 100 visited URLs from your browser history.

**Returns:**
- `List[Dict[str, str]]`: A list of dictionaries containing:
  - `"title"`: The title of the web page
  - `"url"`: The URL of the web page

**Example Response:**
```json
[
  {
    "title": "GitHub - Homepage",
    "url": "https://github.com"
  },
  {
    "title": "Stack Overflow - Programming Questions",
    "url": "https://stackoverflow.com"
  }
]
```

### Integration with MCP Clients

To use this tool with an MCP client, add it to your MCP configuration:

```json
{
  "mcpServers": {
    "history": {
      "command": "python",
      "args": ["/path/to/historyMCP/main.py"],
      "env": {
        "SQLITE_PATH": "/path/to/your/browser/history.db"
      }
    }
  }
}
```

## Development

### Project Structure

```
historyMCP/
├── main.py          # Main MCP server implementation
├── pyproject.toml   # Project configuration and dependencies
├── README.md        # This file
└── uv.lock          # Dependency lock file
```

### Dependencies

- `mcp[cli]>=1.10.1`: Model Context Protocol implementation
- `requests>=2.32.4`: HTTP requests for web content fetching
- `httpx>=0.28.1`: Modern HTTP client
- `pandas>=2.3.0`: Data manipulation (for future features)

### Adding New Features

The codebase is structured to easily add new tools. To add a new MCP tool:

1. Create a new function with the `@mcp.tool()` decorator
2. Define the function signature and return type
3. Add appropriate documentation

Example:
```python
@mcp.tool()
def search_history(query: str) -> List[Dict[str, str]]:
    """
    Search browser history for URLs containing the query
    
    Args:
        query: Search term to look for in URLs and titles
        
    Returns:
        List of matching history entries
    """
    # Implementation here
    pass
```

## Security Considerations

⚠️ **Important**: This tool accesses your browser history, which may contain sensitive information. Consider the following:

- Only use this tool with trusted MCP clients
- Be aware that your browsing history will be shared with AI assistants
- Consider using a separate browser profile for testing
- Review the data being shared before using in production environments

## Troubleshooting

### Common Issues

1. **"Please set the SQLITE_PATH environment variable"**
   - Make sure you've set the `SQLITE_PATH` environment variable correctly
   - Verify the path points to a valid SQLite database file

2. **"Database is locked"**
   - Close your browser completely
   - Copy the database file to a temporary location
   - Update the `SQLITE_PATH` to point to the copied file

3. **"No such file or directory"**
   - Check that the browser history database path is correct for your system
   - Ensure the file exists and is readable

### Getting Help

If you encounter issues:

1. Check that your Python version is 3.12 or higher
2. Verify all dependencies are installed correctly
3. Ensure the SQLite database path is correct and accessible
4. Check that your browser is not currently running (to avoid database locks)

## License

This project is open source. Please check the license file for more details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for bugs and feature requests.
