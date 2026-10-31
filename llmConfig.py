import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

# 本模块可能在 main.py 的 load_dotenv() 之前被导入，这里再兜一次底
_ = load_dotenv()

# os.getenv(key, default) 的返回类型是 str，不会再是 None
base_url: str = os.getenv("OPENAI_BASE_URL", "https://api.deepseek.com")
api_key: str = os.getenv("OPENAI_API_KEY", "")
model: str = os.getenv("OPENAI_MODEL", "deepseek-flash")

# api_key 没有安全的默认值，必须显式校验
if not api_key:
    raise SystemExit("缺少环境变量: OPENAI_API_KEY，请检查 .env 文件")

llm = ChatOpenAI(
    base_url=base_url,
    api_key=SecretStr(api_key),
    model=model,
    temperature=0.3,
)