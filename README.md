✈️ TripMate AI — A Multi-Agent Travel Planner with MCP

An open-source AI-powered travel planner that transforms a natural-language trip request into a practical travel plan with flight suggestions, hotel ideas, weather details, and a day-by-day itinerary.

TripMate AI uses a multi-agent architecture built with LangGraph, LangChain, FastAPI, MCP, PostgreSQL, and Groq.

🌍 Why TripMate AI?

Planning a trip usually means jumping between multiple websites and tools to research:

✈️ Flights
🏨 Hotels
🌤 Weather
🗺️ Places to visit
📅 Daily itineraries

TripMate AI brings these steps together into one intelligent AI-powered experience.

Simply provide a request such as:

"Plan a 7-day trip to Japan from Bengaluru."

TripMate AI coordinates multiple specialized agents to research the trip and generate a complete travel plan.

✨ Features
✈️ Flight research using AviationStack
🏨 Hotel suggestions using Tavily Search
🌤 Weather lookup and forecasting
🧠 Multi-agent orchestration using LangGraph
🔌 MCP-based tool integrations
📝 Structured day-by-day itinerary generation
💬 Natural-language travel requests
🌐 FastAPI backend
🎨 Simple web interface using HTML, CSS, JavaScript, and Jinja2
💾 Conversation state persistence using PostgreSQL
⚡ LLM-powered responses using Groq
🧠 Multi-Agent Architecture

The application uses multiple specialized AI agents coordinated through a LangGraph workflow.

                         👤 User
                            │
                            ▼
                  ┌───────────────────┐
                  │   FastAPI API     │
                  └─────────┬─────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │ LangGraph Manager │
                  │    / Workflow     │
                  └─────────┬─────────┘
                            │
          ┌─────────────────┼──────────────────┐
          │                 │                  │
          ▼                 ▼                  ▼
   ✈️ Flight Agent    🏨 Hotel Agent     🌤 Weather Agent
          │                 │                  │
          ▼                 ▼                  ▼
 AviationStack MCP     Tavily MCP        Custom Weather MCP
          │                 │                  │
          └─────────────────┼──────────────────┘
                            │
                            ▼
                  🗺️ Itinerary Agent
                            │
                            ▼
                  📝 Final Response Agent
                            │
                            ▼
                     Structured Travel Plan
                            │
                            ▼
                      💾 PostgreSQL
🔄 How the Workflow Works
1️⃣ User submits a travel request
              │
              ▼
2️⃣ LangGraph receives and processes the request
              │
              ▼
3️⃣ Flight Agent
   └── Searches flight information using AviationStack MCP
              │
              ▼
4️⃣ Hotel Agent
   └── Researches hotel options using Tavily MCP
              │
              ▼
5️⃣ Weather Agent
   └── Retrieves weather and forecast data using Custom MCP
              │
              ▼
6️⃣ Itinerary Agent
   └── Creates a practical day-by-day travel plan
              │
              ▼
7️⃣ Final Response Agent
   └── Combines all agent outputs into a structured response
              │
              ▼
8️⃣ Response returned through the FastAPI application
              │
              ▼
9️⃣ Conversation state persisted in PostgreSQL
🛠️ Tech Stack
Technology	Purpose
🐍 Python	Core application development
⚡ FastAPI	Backend API
🧠 LangGraph	Multi-agent workflow orchestration
🔗 LangChain	LLM and agent integrations
🤖 Groq	High-performance LLM inference
🔌 MCP	Model Context Protocol tool integration
🐘 PostgreSQL	Conversation and state persistence
🔍 Tavily	Hotel and travel research
✈️ AviationStack	Flight information
🌤 OpenWeather	Weather data
🎨 Jinja2	HTML template rendering
🌐 HTML / CSS / JavaScript	Frontend interface
🔌 MCP Integrations

TripMate AI integrates the Model Context Protocol (MCP) across multiple travel tools.

🔍 Tavily Search MCP

Hotel and travel research uses a remote MCP endpoint.

https://mcp.tavily.com/mcp/
✈️ AviationStack MCP

Flight information is accessed through a local MCP command:

uvx aviationstack-mcp
🌤 Custom Weather MCP

Weather functionality is implemented using a custom local MCP server:

custom_weather_mcp_server.py
MCP Client

The MCP client is implemented in:

mcp_client.py

It provides asynchronous helper functions including:

tavily_mcp_search()
aviation_mcp_call()
weather_mcp_search()
forecast_mcp_search()
extract_destination()

The main travel workflow in backend.py calls these helpers from the Flight, Hotel, and Weather Agents.

📁 Project Structure
.
├── app.py                         # FastAPI application entry point
├── backend.py                     # LangGraph multi-agent workflow
├── mcp_client.py                  # MCP client and tool integrations
├── custom_weather_mcp_server.py   # Custom local Weather MCP server
├── requirements.txt               # Python dependencies
├── .env.example                   # Example environment variables
│
├── static/                        # CSS, JavaScript, and frontend assets
│
├── templates/                     # HTML / Jinja2 templates
│
└── tools/                         # Flight and web search integrations
📋 Prerequisites

Before running the project locally, make sure you have:

Python 3.10 or newer
PostgreSQL installed and running
API keys for:
Groq
Tavily
AviationStack
OpenWeather
uvx available for local aviationstack-mcp usage
🔐 Environment Variables

Create a .env file in the project root:

DATABASE_URL=postgresql://user:password@localhost:5432/travel_db

GROQ_API_KEY=your_groq_api_key

AVIATIONSTACK_API_KEY=your_aviationstack_api_key

TAVILY_API_KEY=your_tavily_api_key

OPENWEATHER_API_KEY=your_openweather_api_key

DEFAULT_ORIGIN_IATA=DAC

⚠️ Important: Never commit your .env file or API keys to GitHub.

Add .env to your .gitignore file:

.env
.venv/
__pycache__/
*.pyc
🚀 Installation
1. Clone the Repository
git clone <your-repository-url>
2. Navigate to the Project
cd TripMate-AI-A-Multi-Agent-Travel-Planner-with-LangGraph
3. Create a Virtual Environment
python -m venv .venv
4. Activate the Environment
Windows
.venv\Scripts\activate
macOS/Linux
source .venv/bin/activate
5. Install Dependencies

Using pip:

pip install -r requirements.txt

Or, if using uv:

uv pip install -r requirements.txt
▶️ Running the Application

Start the FastAPI application:

python app.py

Then open your browser:

http://127.0.0.1:8000/
🌐 API Endpoints
Method	Endpoint	Description
GET	/health	Health check
POST	/api/travel	Submit a travel request
📤 Example API Request
curl -X POST http://127.0.0.1:8000/api/travel \
  -H "Content-Type: application/json" \
  -d '{"message":"Plan a 3-day trip to Tokyo with a budget of $1200"}'
💬 Example Travel Requests

You can ask TripMate AI questions like:

Plan a 7-day trip to Japan from Bengaluru.
Plan a 5-day budget trip to Goa.
Suggest a 4-day trip to Dubai with hotel and flight options.
Plan a 3-day trip to Tokyo with a budget of $1200.

TripMate AI coordinates the appropriate agents and generates a structured travel plan containing relevant:

✈️ Flight suggestions
🏨 Hotel recommendations
🌤 Weather information
🗺️ Destination details
📅 Day-by-day itinerary
💾 PostgreSQL State Persistence

PostgreSQL is used to persist conversation and application state.

User Request
     │
     ▼
FastAPI
     │
     ▼
LangGraph Multi-Agent Workflow
     │
     ▼
Generate Travel Plan
     │
     ▼
PostgreSQL
     │
     ▼
Persist Conversation / Application State

This allows relevant application data to remain available even after the backend restarts or is redeployed.

🔧 Using MCP Tools

The application uses MCP behind the scenes, so no separate frontend configuration is required once the environment variables and dependencies are configured.

If you need to customize the local Weather MCP server, update the Weather MCP server command or path in:

mcp_client.py

The project uses:

Remote MCP
    │
    └── Tavily Search MCP

Local stdio MCP
    │
    └── AviationStack MCP

Custom Local MCP Server
    │
    └── Weather MCP
🤝 Contributing

Contributions are welcome! 🚀

If you would like to improve TripMate AI, add new features, or fix issues:

1. Fork the repository
2. Create a feature branch
git checkout -b feature/your-feature-name
3. Make your changes
4. Commit your changes
git add .
git commit -m "Add your feature"
5. Push your branch
git push origin feature/your-feature-name
6. Open a Pull Request
🔮 Future Improvements
🔐 User authentication and authorization
💰 Budget optimization agent
🗺️ Interactive maps and route planning
🚕 Local transportation recommendations
🍽️ Restaurant recommendation agent
❤️ Personalized travel preferences
📱 Mobile-friendly interface improvements
☁️ Cloud deployment
🧠 Long-term travel memory
📊 Travel cost estimation
🌍 Multi-language support
🙏 Acknowledgments

This project is built using modern LLM, Agentic AI, LangGraph, LangChain, MCP, and travel API technologies.

It is intended as a practical example of how multiple specialized AI agents can collaborate with real-world tools and APIs to solve a complete travel-planning problem.

⭐ Support the Project

If you find TripMate AI useful, please consider giving the repository a star ⭐.

✈️ Plan smarter. Research faster. Travel better — with TripMate AI.
