from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOllama
from Job_tools import job_scrapper_tool, emeail_generator_tool

model = ChatOllama(model="gemma3:1b") 
tools = [job_scrapper_tool, emeail_generator_tool]

agent = initialize_agent(tools=tools, llm=model,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

query = "Software Developer"
job_limit = 3

jobs = agent.run(f"Search for the top {job_limit} jobs for '{query}' and generate an email for me to apply to job with high experience.")

print(jobs)