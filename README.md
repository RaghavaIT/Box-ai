📖 Box-ai

This project provides a Python pipeline to ingest documents from Box into Interlinked AI’s Knowledge Base.
It extracts text from Box files (PDF, DOCX, TXT), cleans them, and pushes them into Interlinked using its Knowledge APIs.
## 📂 Project Structure

box.AI/
│── .env                  # BOX + Interlinked API keys
│── requirements.txt      # dependencies
│── config.py             # loads env variables
│── box_client.py         # Box API connector
│── scraper.py            # extract text from Box files
│── interlinked_client.py # send data to Interlinked Knowledge API
│── ingestion.py          # orchestrates pipeline
│
└── tests/
    ├── test_box_client.py
    ├── test_scraper.py
    ├── test_ingestion.py


⚙️ Setup
1. Clone the repo
git clone https://github.com/RaghavaIT/Box-ai.git
cd Box-ai

2. Create virtual environment
python -m venv .venv
# Activate
source .venv/bin/activate     # Mac/Linux
.venv\Scripts\activate        # Windows

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables

Create a .env file in the root directory:

BOX_CLIENT_ID=your_box_client_id
BOX_CLIENT_SECRET=your_box_client_secret
BOX_ACCESS_TOKEN=your_box_access_token

INTERLINKED_API_KEY=your_interlinked_api_key

▶️ Usage
Ingest all files from Box root folder
python ingestion.py

Ingest from a specific Box folder

Update the ingestion.py file:

if __name__ == "__main__":
    ingest_box_folder("123456789")  # replace with Box folder ID

🧪 Testing

Run unit tests:

pytest tests/

🔑 Key Components

box_client.py → Connects to Box API and fetches files.

scraper.py → Extracts and cleans text from PDF/DOCX/TXT.

interlinked_client.py → Pushes text into Interlinked Knowledge Base (AI.learn).

ingestion.py → Orchestrates Box → Scraper → Interlinked.

📌 Notes

Currently supports PDF, DOCX, TXT. Extend scraper.py for other formats.

Box API requires client_id, client_secret, and access_token → Get from Box Developer Console
.

Interlinked API requires an API key (provided by your team).

📊 Architecture Flow
flowchart TD
    A[Box Storage] --> B[Box Client]
    B --> C[Scraper]
    C --> D[Interlinked Client]
    D --> E[Interlinked Knowledge Base]
    E --> F[LLM / Q&A Service]

    ⚠️ **Important Note**

This project is intended for **local development and testing only**.  
The `.env` file currently stores API keys and tokens in plain text.  

🚫 Do **NOT** use this setup directly in a production environment.  

✅ For production:
- Store secrets in a secure service like **Azure Key Vault**, **AWS Secrets Manager**, or **Vault by HashiCorp**.
- Update `config.py` to fetch secrets securely instead of reading from `.env`.
Sample code for production ready
import os
from dotenv import load_dotenv

# If running locally for dev/testing, still load .env
load_dotenv()

# For production, fetch secrets from Azure Key Vault
config.py
-----
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class Config:
    # Load from ENV first (safe for local dev)
    BOX_CLIENT_ID = os.getenv("BOX_CLIENT_ID")
    BOX_CLIENT_SECRET = os.getenv("BOX_CLIENT_SECRET")
    BOX_ACCESS_TOKEN = os.getenv("BOX_ACCESS_TOKEN")
    INTERLINKED_API_KEY = os.getenv("INTERLINKED_API_KEY")

    @classmethod
    def load_from_keyvault(cls, vault_url: str):
        """
        Load secrets securely from Azure Key Vault
        vault_url: Example -> "https://my-keyvault.vault.azure.net/"
        """
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=vault_url, credential=credential)

        cls.BOX_CLIENT_ID = client.get_secret("Box-Client-Id").value
        cls.BOX_CLIENT_SECRET = client.get_secret("Box-Client-Secret").value
        cls.BOX_ACCESS_TOKEN = client.get_secret("Box-Access-Token").value
        cls.INTERLINKED_API_KEY = client.get_secret("Interlinked-Api-Key").value

        print("✅ Secrets loaded securely from Azure Key Vault")




