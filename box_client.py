from boxsdk import OAuth2, Client
from config import BOX_CLIENT_ID, BOX_CLIENT_SECRET, BOX_ACCESS_TOKEN

def get_box_client():
    """
    Authenticate and return Box client
    """
    oauth = OAuth2(
        client_id=BOX_CLIENT_ID,
        client_secret=BOX_CLIENT_SECRET,
        access_token=BOX_ACCESS_TOKEN
    )
    return Client(oauth)

def fetch_files(folder_id="0"):
    """
    Fetch all items in a Box folder (default root folder)
    """
    client = get_box_client()
    folder = client.folder(folder_id=folder_id).get()
    items = folder.get_items(limit=100)
    return items
