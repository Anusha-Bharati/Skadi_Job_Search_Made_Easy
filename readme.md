• Ingestion Layer: Multi-account distributed extraction via the Google API Client. Implements Server-Side Filtering via Query Pruning to reduce network bandwidth and I/O overhead.

• Transformation & Processing Layer: A Two-Tiered Classification Architecture. Tier 1 uses a high-recall local regex Sifting Matrix to shed irrelevant processing volumes. Tier 2 uses a zero-RAM-footprint Semantic Token Classifier via the Gemini API, enforcing a strict JSON output schema.

• Storage / Persistence Layer: A decoupled, file-based Data Lakehouse State (job_pipeline_dw.json) acting as a stateful snapshot that manages transaction updates and tracks dynamic applicant lifecycle states.

• Presentation Layer: A reactive web app utilizing Streamlit for real-time reporting, parsing data down to granular dimensions (Company, Title, Dynamic Stage, and Salary).
