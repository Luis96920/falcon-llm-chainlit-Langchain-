import chainlit as cl
from chainlit import AskUserMessage, Message
from decouple import config
from langchain import PromptTemplate, LLMChain

from app.services.llm import FalconLLM

falcon_llm = FalconLLM(
    name="Falcon",
    repo_id="tiiuae/falcon-7b-instruct",
    hf_api_token=config("HF_API_TOKEN"),
    temperature=0.1,
    max_new_tokens=2000,
).get_llm()


@cl.langchain_factory
def factory():
    template = """Question: {question}
  Answer: Let's think step by step.
  """
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=falcon_llm, verbose=False)

    return llm_chain


@cl.on_message
def on_message(message: str):
    cl.Message(
        content=f"This is my answer: {message}",
    ).send()


@cl.on_chat_start
def main():
    res = AskUserMessage(content="What is your name?", timeout=30).send()
    if res:
        Message(
            content=f"Your name is: {res['content']}.\nChainlit installation is working!\nYou can now ask me questions.",
        ).send()
