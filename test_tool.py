#!/usr/bin/env python3
"""Test script to call MCP tools directly."""

from server import fetch_text

# Test the fetch_text tool
result = fetch_text("https://www.lennysnewsletter.com")

# Print the results (text content)
print(result)

