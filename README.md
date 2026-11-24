# WorkLoop

A job-seeker-first web application connecting skilled blue-collar workers (carpenters, housemaids, plumbers, electricians, cooks, drivers) with local daily-wage, 10–15 day gig, and monthly job postings.

## Features
- **Job Postings Feed**: Browse open jobs by role and duration, view start dates and pay details, and send requests with one tap.
- **Voice Search & Voice Forms**: Multilingual voice input (English, Hindi, Kannada, Tamil) for searching jobs, registering worker profiles, and posting jobs.
- **WhatsApp Alerts**: Interactive button-based daily job alerts that let workers view details and open matching jobs directly in the app.
- **Employer Portal & Match Chat**: Employers post jobs, review applicant ratings and past work, accept a match, and negotiate final pay via chat or call.

## Project Structure
- `index.html` — Standalone responsive web app
- `lambda_handlers.py` — AWS Lambda API handlers (jobs, requests, ratings & work history)
- `whatsapp_webhook.js` — WhatsApp Business Cloud API interactive button webhook
- `voice_assistant.js` — ElevenLabs multilingual voice integration helper
- `template.yaml` — AWS SAM template (DynamoDB tables & encrypted S3 bucket)

## Run Locally
Open `index.html` directly in any browser.
