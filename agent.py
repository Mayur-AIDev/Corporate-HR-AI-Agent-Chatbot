import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint,HuggingFaceEmbeddings
embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

load_dotenv()
My_Token = os.environ.get("my_token")

# Switch to Qwen-2.5-7B-Instruct: No gating rules, fully public model
llm_endpoint = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    temperature=0.1,
    huggingfacehub_api_token=My_Token
)


llm = ChatHuggingFace(llm=llm_endpoint)