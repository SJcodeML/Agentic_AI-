import os 
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI,  set_tracing_disabled, ModelSettings, funtion_tool

load_dotenv()
set_tracing_disabled(disabled=True)

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY","")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativeLanguage.googleapis.com/v1beta/openai/"


external_client = AsyncOpenAI(api_key=GEMINI_API_KEY, base_url=BASE_URL)
llm_model = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=external_client)

from agents import Agent,Runner, handoff
import asyncio

billing_agent = Agent(
    name="Billing Agent",
    instructions="Resolve billing problems end to end. Ask for any details you need."

)

refunds_agent = Agent(
    name="Refunds Agent",
    instructions="Handle refunds end to end. Ask for order ID and explain next steps."

)

triage = Agent(    
    name="Triage Agent",
    instructions=(
        "greet the user and decide where to send them:\n"
        "- if the user asks about a double charge, invoice,payment etc handoff to billing agent\n"
        "- if the user asks about refund status or returning an item, handoff to return agent\n"
        "once the handed off the specialist should continue the conversation"

    )
    handoffs=[billing_agent, handoff(refunds_agent)],
)

async def main():
    r1 = await Runner.run(triage, "Hi, I returned my headset last week. What's my refund status?")
    print("A) Final reply (from REFUNDS specialist):  , r1.final_output,  \n")

    r2 = await Runner.run(triage, "My cards was charged twice for the same order.")
    print("B) "  "Final reply (from BILLING specialist): , r2.final_output),\n")

    if __name__ == "__main__":
     asyncio.run(main())




