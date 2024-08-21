from fastapi import FastAPI

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig
from langchain_community.tools.tavily_search import TavilySearchResults

from langserve import add_routes

from langgraph.graph import StateGraph, END, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode


from typing import TypedDict, Annotated, Literal


app = FastAPI(
    title="LangChain Server",
    version="1.0"
)

@tool
def weather(query: str):
    """_summary_

    今日の天気予報をお知らせする。

    Args:
        query (str): _description_
    """
    return ["晴れのち雨です。"]

class State(TypedDict):
    messages: Annotated[list, add_messages]

def call_model(state: State, config: RunnableConfig):
    messages = state["messages"]
    response = model.invoke(messages, config)
    return {"messages": response}

def should_continue(state: State) -> Literal["__end__", "tools"]:
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:
        return END
    else:
        return "tools"

# tools = [weather]
tools = [TavilySearchResults(max_results=2)]
model = ChatOpenAI(model="gpt-4o-2024-05-13")
model = model.bind_tools(tools)

graph = StateGraph(State)
tool_node = ToolNode(tools)

graph.add_node("agent", call_model)
graph.add_node("tools", tool_node)

graph.add_edge(START, "agent")
graph.add_conditional_edges("agent", should_continue)
graph.add_edge("tools", "agent")

compiled = graph.compile()

add_routes(
    app,
    compiled,
    path="/graph"
)
