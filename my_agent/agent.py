from google.adk.agents.llm_agent import Agent
import datetime

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)

# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    current_date_time = datetime.datetime.now()
    current_time_24hrs = current_date_time.time()
    current_time_12hrs = current_time_24hrs.strftime("%I:%M:%p")
    return {"status": "success", "city": city, "time": current_time_12hrs}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time],
)