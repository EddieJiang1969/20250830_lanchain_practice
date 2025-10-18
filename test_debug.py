from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_ollama.llms import OllamaLLM

# 建立模型
model = OllamaLLM(model="llama3.2:latest")

# 建立提示模板
prompt = ChatPromptTemplate.from_template("請介紹 {topic}")

# 使用 LCEL 語法建立鏈
chain = prompt | model | StrOutputParser()

# 執行
result = chain.invoke({"topic": "人工智慧"})
print(result)
