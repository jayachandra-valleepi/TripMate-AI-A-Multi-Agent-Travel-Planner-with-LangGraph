import os
import asyncio
import certifi
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient


os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTES_CA_BUNDLE"] = certifi.where()

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

client = MultiServerMCPClient(
    {
        "tavily":{
            "transport" : "streamable_http",
            "url" : f"https://mcp.tavily.com/mcp/?tavilyApiKey=<TAVILY_API_KEY>"
        },
    }
)

async def get_all_tools():
    tools = await client.get_tools()
    print("\nAvailable MCP Tools:\n")

    for tool in tools:
        print(tool.name)


# This returns tavily_search tool object
tavily_sarch_tool = None

async def get_tavily_search_tool():
    global tavily_sarch_tool
    if tavily_sarch_tool is not None:
        return

    tools = await client.get_tools()
    print("\nAvailble MCP Tools:")

    for tool in tools:
        print(tool.name)

    tavily_sarch_tool = next(
        tool
        for tool in tools
        if tool.name == "tavily_search"
    )


# This function can be used to call the tavily_search tool with a query in backend.py
async def tavily_mcp_search(query : str):
    await get_tavily_search_tool()
    result = await tavily_sarch_tool.ainvoke(
        {
            "query" : query
        }
    )

    return result
    # print(result)