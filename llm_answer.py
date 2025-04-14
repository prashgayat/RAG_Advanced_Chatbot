# llm_answer.py

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

def llm_answer(query, docs):
    try:
        # Concatenate the content of the retrieved documents
        context = "\n\n".join(doc.page_content for doc in docs)

        # Compose prompt
        prompt = f"""You are an expert assistant. Use the below context to answer the question. 
If the context is irrelevant or insufficient, respond with "I'm not sure based on the provided documents."

Context:
{context}

Question: {query}
Answer:"""

        # Call the OpenAI model
        llm = ChatOpenAI(
            temperature=0,
            model_name="gpt-3.5-turbo",
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        response = llm([HumanMessage(content=prompt)])
        return response.content

    except Exception as e:
        return f"❗ Error generating answer: {str(e)}"
