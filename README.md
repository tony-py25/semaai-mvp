# SemaAI MVP

A mobile-friendly Flask MVP for a Kiswahili-first AI assistant.

## Run locally
pip install -r requirements.txt
python app.py

Then open http://127.0.0.1:5000

## Deploy
The included Procfile is suitable for services that run:
gunicorn app:app

## Next step
Replace the demo logic in `/api/chat` with a real AI model/API. Keep API keys server-side as environment variables.
