# perplexity-ai-clone

Describe your project here.

# init

```bash
rye add langchain==0.2.3 langchain-openai==0.1.8 langgraph==0.0.66 langserve==0.2.2 langchain-community==0.2.4 fastapi==0.111.0 sse_starlette

rye sync
```

```bash
export OPENAI_API_KEY=
export TAVILY_API_KEY=
```

# run

```bash
rye run uvicorn main:app --reload
```

# test

```bash
# Just Requests.
>>>input
curl -X POST "http://localhost:8000/openai/invoke" -H "Content-Type: application/json" -d '{
  "input": [{"type": "human", "content": "hello"}]}'

>>>output
event: metadata
data: {"run_id": "71018dd6-d91a-40fe-9f78-976880f59707"}

event: data
data: {"content":"","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-71018dd6-d91a-40fe-9f78-976880f59707","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}

event: data
data: {"content":"I'm","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-71018dd6-d91a-40fe-9f78-976880f59707","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}

event: data
data: {"content":" sorry","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-71018dd6-d91a-40fe-9f78-976880f59707","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}

event: data
data: {"content":",","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-71018dd6-d91a-40fe-9f78-976880f59707","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}

event: data
data: {"content":" but","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-71018dd6-d91a-40fe-9f78-976880f59707","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}

event: data
data: {"content":" I","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-71018dd6-d91a-40fe-9f78-976880f59707","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}

event: data
data: {"content":" can't","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-71018dd6-d91a-40fe-9f78-976880f59707","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}

event: data
data: {"content":" provide","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-71018dd6-d91a-40fe-9f78-976880f59707","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}

event: data
data: {"content":" real","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-71018dd6-d91a-40fe-9f78-976880f59707","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}

event: data
data: {"content":"-time","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-71018dd6-d91a-40fe-9f78-976880f59707","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}

event: data
data: {"content":" information","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-71018dd6-d91a-40fe-9f78-976880f59707","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}

event: data
data: {"content":".","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-71018dd6-d91a-40fe-9f78-976880f59707","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}

...

>>>input
curl -X POST "http://localhost:8000/graph/invoke" -H "Content-Type: application/json" -d '{
  "input": {"messages": [["user", "今日の天気を教えて"]]}}'
```