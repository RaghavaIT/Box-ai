from box_connector.ingestion import ingest_box_folder

def test_ingestion():
    try:
        ingest_box_folder("0")
        assert True
    except Exception as e:
        assert False, f"Ingestion failed: {e}"
