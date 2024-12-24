from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA

import openai

import os

os.environ["OPENAI_API_KEY"] = ""

# Step 1: 데이터 준비
documents = [
    {"text": "Python은 인공지능과 머신러닝에 널리 사용되는 프로그래밍 언어입니다."},
    {"text": "FAISS는 벡터 검색과 유사도 검색에 사용되는 효율적인 라이브러리입니다."},
    {"text": "GPT 모델은 텍스트 생성과 언어 이해를 위한 강력한 언어 모델입니다."},
    {"text": "RAG는 검색과 생성을 결합한 기술로, 정확하고 실용적인 답변을 생성합니다."}
]

# Step 2: 데이터 벡터화 및 저장
# OpenAI Embeddings를 사용해 벡터 생성
embedding_model = OpenAIEmbeddings()  # OpenAI API 키가 설정되어 있어야 함
texts = [doc["text"] for doc in documents]
vectorstore = FAISS.from_texts(texts, embedding_model)

# Step 3: 검색 및 생성 파이프라인 구성
llm = OpenAI(model="gpt-3.5-turbo")  # GPT-3.5 사용
retriever = vectorstore.as_retriever()  # 검색 기능 생성

# Retrieval-Augmented QA Chain 생성
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# Step 4: 사용자 입력 및 RAG 실행
def ask_question(question):
    result = qa_chain({"query": question})
    answer = result["result"]
    sources = result["source_documents"]
    print(f"\n질문: {question}")
    print(f"답변: {answer}")
    print("\n참조된 문서:")
    for i, source in enumerate(sources, start=1):
        print(f"  {i}. {source.page_content}")

# 예제 실행
if __name__ == "__main__":
    user_question = "RAG는 무엇인가요?"
    ask_question(user_question)