from interlinked import AI
from config import INTERLINKED_API_KEY

def upload_to_interlinked(text: str, source_id: str, metadata: dict = None):
    """
    Push content into Interlinked Knowledge Base
    """
    if not text.strip():
        print(f"⚠️ Skipped empty content for {source_id}")
        return

    AI.learn(
        from_=text,
        knowledge_source_id=source_id,
        metadata=metadata or {"source": "box"}
    )
    print(f"✅ Uploaded {source_id} to Interlinked")
