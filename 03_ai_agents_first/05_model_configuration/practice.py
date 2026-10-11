
# from google import genai

# client = genai.Client(api_key="")

# response = client.models.generate_content(
#     model="gemini-3.8-flash",
#     contents="tell  me about ypur self then let me know . Explain recursion in programming using a haiku.",
# )

# print(response.text)



from openai import OpenAI

client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {   "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": " Tell me who are u . who is giving me answers . Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)



# import asyncio
# from openai import AsyncOpenAI
# from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

# # Your Gemini API key and endpoint
# gemini_api_key = ""

# # Agents SDK requires an AsyncOpenAI client
# client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# # Disable OpenAI cloud tracing since we are routing to Gemini
# set_tracing_disabled(disabled=True)


# async def main():
#     agent = Agent(
#         name="Assistant",
#         instructions="You are a helpful assistant.",
#         model=OpenAIChatCompletionsModel(
#             model="gemini-3.8-flash",
#             openai_client=client,
#         ),
#     )

#     result = await Runner.run(
#         agent,
#         "Tell me who are u . who is giving me answers . Explain to me how AI works",
#     )
    
#     print(result.final_output)


# if __name__ == "__main__":
#     asyncio.run(main())