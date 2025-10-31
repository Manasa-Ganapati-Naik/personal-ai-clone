# Data Collection Plan

## Data types
- SMS text (export), email archives (MBOX), chat logs (Slack/WhatsApp export)

## Minimum volume
- Aim for 10k-50k tokens for initial personalization; if not available, use adapter tuning + synthetic augmentation.

## Anonymization
- Remove PII (names, phone numbers, emails) using regex patterns (see cleaning script).
- Replace with placeholders: <NAME>, <EMAIL>, <PHONE>.

## Storage
- Store raw uploads locally in encrypted folder: /data/raw (AES-256).
- Preprocessed data in /data/processed (restricted access).

## Retention and deletion
- Data will be deleted on request within 14 days.

## Consent
- Collect signed consent form before processing.
