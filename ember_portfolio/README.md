# Sri Lochana — Retro Pixel Portfolio

A responsive student portfolio with a retro pixel-art / pastel aesthetic.

## Tech stack
- HTML, CSS and JavaScript
- Python Flask backend
- SQLite contact-message storage

## Run locally (Windows)
Open this folder in VS Code and run these commands in its terminal:

```powershell
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Then visit http://127.0.0.1:5000.

If `py -3.12` is not available, use `py --list` to see installed Python versions and select a version 3.10 or newer.

## Backend
The contact form validates the submitted fields and stores messages in SQLite using parameterized SQL. Submit a test message locally to verify it. The `/health` endpoint returns a simple status response.

## Deployment
The project includes `render.yaml` for a Render web service and persistent disk. Review Render's current pricing and persistent-disk requirements before deployment. Set a secure `SECRET_KEY`; never commit credentials.

## Personalisation before submission
- Confirm the wording of your degree and college details.
- Add only real certificates and achievements.
- Add verified social links and a reviewed resume if you want them displayed.
- Add or replace project links after publishing them.
- The insider-threat project is described as dataset preparation, not a trained model.
- The supplied pixel-art images were provided as design references for this portfolio.
