import sys
from io import TextIOWrapper

from dotenv import load_dotenv
from langchain_core.messages import AIMessageChunk, HumanMessage

from deepagents import create_deep_agent
from llmConfig import llm

_ = load_dotenv()

# Windows 控制台默认 GBK，改为 UTF-8 以支持 emoji 等字符输出
if isinstance(sys.stdout, TextIOWrapper):
    sys.stdout.reconfigure(encoding="utf-8")

# create_deep_agent 返回 CompiledStateGraph，模型实例通过 model 参数接入
agent = create_deep_agent(
    model=llm,
    system_prompt="你是一个乐于助人的助手。",
)

if __name__ == "__main__":
    try:
        # stream_mode="messages" 逐 token 产出 (message_chunk, metadata) 二元组
        for chunk, _metadata in agent.stream(
            {"messages": [HumanMessage("讲一个猫的笑话")]},
            stream_mode="messages",
        ):
            if isinstance(chunk, AIMessageChunk) and isinstance(chunk.content, str):
                print(chunk.content, end="", flush=True)
    except Exception as e:
        print(f"调用失败: {e}")
