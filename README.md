# Box-ai
This project provides a Python pipeline to ingest documents from Box into Interlinked AI’s Knowledge Base. It extracts text from Box files (PDF, DOCX, TXT), cleans them, and pushes them into Interlinked using its Knowledge APIs.
📂 Project Structure
box_connector/
│── .env                      # BOX + Interlinked API keys
│── requirements.txt          # dependencies
│── config.py                 # loads env variables
│── box_client.py             # Box API connector
│── scraper.py                # extract text from Box files
│── interlinked_client.py     # send data to Interlinked Knowledge API
│── ingestion.py              # orchestrates pipeline
│
└── tests/
    ├── test_box_client.py
    ├── test_scraper.py
    ├── test_ingestion.py

    ⚙️ Setup
1. Clone the repo
git clone https://github.com/RaghavaIT/Box-ai.git
cd box-connector

2. Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables

Create a .env file:

BOX_CLIENT_ID=your_box_client_id
BOX_CLIENT_SECRET=your_box_client_secret
BOX_ACCESS_TOKEN=your_box_access_token

INTERLINKED_API_KEY=your_interlinked_api_key

▶️ Usage
Ingest all files from Box root folder
python ingestion.py

Ingest from specific folder

Update in ingestion.py:

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

Box API requires client_id, client_secret, access_token. Get these from Box Developer Console
.

Interlinked API requires an API key (provided by your team).

++++++
# Setup env
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

pip install -r requirements.txt

# Run ingestion
python ingestion.py

# Run tests
pytest tests/
++++