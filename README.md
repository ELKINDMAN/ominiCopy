# ominiCopy

A simple FastAPI-based REST API for managing marketing campaigns.

## Features
- CRUD operations for campaigns (Create, Read, Update, Delete)
- Campaign fields: `campaign_id`, `name`, `due_date`, `created_at`
- In-memory data storage (no database required)
- API endpoints:
  - `GET /api/v1/` — Health check
  - `GET /api/v1/campaigns` — List all campaigns
  - `GET /api/v1/campaigns/{id}` — Get campaign by ID
  - `POST /api/v1/campaigns` — Create a new campaign
  - `PUT /api/v1/campaigns/{id}` — Update a campaign
  - `DELETE /api/v1/campaigns/{id}` — Delete a campaign

## Getting Started

### Requirements
- Python 3.12+
- See `requirements.txt` for dependencies

### Installation
1. Clone the repository:
   ```powershell
   git clone <repo-url>
   cd ominiCopy
   ```
2. (Optional) Create and activate a virtual environment:
   ```powershell
   python -m venv omini
   .\omini\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

### Running the API
Start the FastAPI server using Uvicorn:
```powershell
uvicorn main:app --reload --port 8000
```
Visit [http://localhost:8000/api/v1](http://localhost:8000/api/v1) in your browser or use tools like Postman to interact with the API.

## Example Campaign Object
```json
{
  "campaign_id": 1,
  "name": "Welcome to Store",
  "due_date": "2025-09-17T12:00:00",
  "created_at": "2025-09-17T10:00:00"
}
```

## License
MIT

## Development
In progress...

```author
Elkanah Kindness .M
```
