import os
import certifi
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from mcp.server.fastmcp import FastMCP


# SSL certificates
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()


load_dotenv()


# API Keys
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
AVIATIONSTACK_API_KEY = os.getenv("AVIATIONSTACK_API_KEY")


# Validate API keys
if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY is missing")

if not AVIATIONSTACK_API_KEY:
    raise ValueError("AVIATIONSTACK_API_KEY is missing")


client = MultiServerMCPClient(
    {
        "tavily": {
            "transport": "streamable_http",
            "url": (
                f"https://mcp.tavily.com/mcp/"
                f"?tavilyApiKey={TAVILY_API_KEY}"
            )
        },

       "aviationstack": {
        "transport": "stdio",
        "command": "uvx",
        "args": [
            "--python",
            "3.13",
            "--with",
            "mcp==1.12.4",
            "aviationstack-mcp"
        ],
        "env": {
            "AVIATION_STACK_API_KEY": AVIATIONSTACK_API_KEY
            }
    }
    }
)


async def get_all_tools():
    tools = await client.get_tools()

    print("\nAvailable MCP Tools:\n")

    for tool in tools:
        print(tool.name)