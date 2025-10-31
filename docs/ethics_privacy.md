# Ethics & Privacy Plan

## Principles
- **Informed consent**: Obtain explicit, documented consent before collecting or using personal data.
- **Data minimization**: Collect only the data strictly necessary for personalization.
- **Right to erasure**: Allow users to request deletion of their raw and processed data.
- **Data security**: Protect data at rest and in transit with modern cryptography.
- **Transparency**: Inform users how their data will be used and give clear contact information.

## Measures
- **Consent before ingestion**: Require signed consent form (see data_plan/consent_form.txt) prior to processing any user data.
- **Anonymization**: Apply PII removal (emails, phones, names) and placeholder substitution before model training (see data_plan/cleaning_snippets.py).
- **Encryption at rest**: Store raw uploads in an encrypted directory (AES-256 recommended).
- **Encryption in transit**: Use TLS for any networked uploads or API calls.
- **Access control**: Limit access to encrypted keys/credentials (developer and supervisor keys only).
- **Logging & audit trail**: Record access to raw and processed data with timestamp and actor for accountability.

## Risk mitigations
- **Human-in-the-loop**: Require human review before any message is sent or used in public demonstrations.
- **Output watermarking/labeling**: Mark AI-generated text in demos (e.g., “[AI-generated]”) so recipients know content is synthesized.
- **No public deployment without explicit consent**: Do not push the personalized clone into public channels or services without informed approval.
- **Bias monitoring**: Periodically review outputs for harmful or biased content; maintain a mitigation plan.
- **Minimum viable logging**: Log enough to audit but avoid storing sensitive content in logs.

## Legal & Compliance Notes (GDPR basics)
- **Lawful basis**: Obtain explicit consent (Article 6) for processing personal data for model adaption and demos.
- **Data subject rights**: Support access, rectification, erasure, restriction of processing, and portability.
- **Data Protection by Design**: Prefer approaches that minimize data transfer (e.g., adapters, on-device or federated learning).

## Optional Technical Notes
- **AES encryption**: Use a vetted library (e.g., `cryptography` in Python) for AES-256 encryption of stored files. Do not write your own crypto.
- **Key management**: Store keys in environment variables or a secrets manager, not in source control. Use `python-dotenv` for local development only.
- **Secrets**: Keep a `.env.example` in repo (no secrets), and ensure `.env` is in `.gitignore`.
