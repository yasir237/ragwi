from stores.llm.LLMProviderFactory import LLMProviderFactory
from stores.llm.LLMEnums import LLMEnum
from stores.vectordb.VectorDBProviderFactory import VectorDBProviderFactory
from stores.vectordb.VectorDBEnums import VectorDBEnum
from helpers.config import get_settings

settings = get_settings()

class NLPController:

    def __init__(self, db):
        self.db = db
        llm_factory = LLMProviderFactory(settings)
        self.embed_provider = llm_factory.create(LLMEnum.OLLAMA)
        self.llm_provider = llm_factory.create(LLMEnum.GROQ)
        vectordb_factory = VectorDBProviderFactory(db)
        self.vectordb_provider = vectordb_factory.create(VectorDBEnum.PGVECTOR)

    async def answer_question(self, question: str, project_id: int, top_k: int = 5):
        # soruyu embed et
        question_embedding = self.embed_provider.embed_text(question)

        # ilgili chunk'ları bul
        chunks = await self.vectordb_provider.search(
            collection_name="chunks",
            query_vector=question_embedding,
            top_k=top_k
        )

        if not chunks:
            return {"answer": "İlgili bilgi bulunamadı.", "chunks": []}

        # chunk'ları birleştir
        context = "\n\n".join([chunk.text for chunk in chunks])

        # LLM'e gönder
        prompt = f"""Aşağıdaki bilgilere dayanarak soruyu cevapla.

Bilgiler:
{context}

Soru: {question}

Cevap:"""

        answer = self.llm_provider.generate_text(prompt)

        return {
            "answer": answer,
            "chunks": [{"text": chunk.text, "id": chunk.id} for chunk in chunks]
        }