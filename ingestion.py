from box_connector.box_client import fetch_files
from box_connector.scraper import extract_text_from_file
from box_connector.interlinked_client import upload_to_interlinked

def ingest_box_folder(folder_id="0"):
    """
    Orchestrates Box → Scraper → Interlinked ingestion
    """
    items = fetch_files(folder_id)

    for item in items:
        if item.type == "file":
            # NOTE: in real-world, you'd download file to local before parsing
            file_path = item.name
            print(f"📂 Processing {file_path}...")

            text = extract_text_from_file(file_path)
            upload_to_interlinked(
                text,
                source_id=item.id,
                metadata={"filename": item.name}
            )

if __name__ == "__main__":
    ingest_box_folder("0")
