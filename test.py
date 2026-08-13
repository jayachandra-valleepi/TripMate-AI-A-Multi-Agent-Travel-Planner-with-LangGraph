from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

from backend import run_travel_agent

# result = search_flights("Plan a 7 days japan trip from Bengaluru")

# print(result) 

# res = run_travel_agent()
# print(res)

user_input = input("Enter travel request: ")

response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)

print("\nFINAL RESPONSE:\n")
print(response["answer"])