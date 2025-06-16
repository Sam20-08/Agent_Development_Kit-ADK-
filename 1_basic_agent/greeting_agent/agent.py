from google.adk.agents import Agent

# There must atleast one root agent

root_agent=Agent(
  name="greeting_agent",
  model="gemini-2.0-flash",
  description="Greeting agent",
  instruction="""
      you are a helpful assisstant that greets the user.
      ask for the user name and greet them by name.
"""
)