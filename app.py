import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.outh2.credentials import Credentials
import streamlit as st

SCOPES = ['https://googleapis.com']
TOKENS= ["token_account1.json", "token_account2.json"]
DB_PATH = "job_pipeline_dw.json"

KEYWORDS = ["apply", "application", "received", "thank you", "submitted", "unsuccessful", 
            "assessment", "test", "interview", "moving forward", "regret", "salary", "offer"]


st.set_page_config(page_title="Job tracker", layout="wide")
st.title("Secure serverless pipeline for Job tracking")
st.write("An autonomous ETL tracking local inbox and extracting keywords specific unstructured emails and converting it into semantic analysis dashboard")

## Setup environment keys without hardcoding
with st.sidebar:
    st.header("Check your jobs status")
    api_key_input = st.text_input("GEMINI API Key", type="password", value=os.environ.get("GEMINI_API_KEY" ""))

## Setup date inputs
    st.subheader("Filter by Dates")
    date_from = st.date_input("Date From", datetime(2026, 30,10))
    date_to = st.date_input("Date To", datetime.today())

##Run pipeline button
    run_pipeline = st.button("Let's get cracking!")

##Check the database if the db path exists
if os.path.exists(DB_PATH):
    with open(DB_PATH,"r") as f:
        master_store = json.load(f)
else:
    master_store = {} 

##Authentication loop

def authentication_endpoint(token_path):
    if os.path.exists(token_path):
        return Credentials.from_authorized_user_file(token_path, SCOPES)
    if not os.path.exists(token_path):
        st.error("Missing credentials")
        st.stop()

    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port = 0) 

#SAve credentials for next run

    with open(token_path,"w") as token:
        token.write(creds.to_json())
    return creds

#Run AI layer - with semantic inference

def run_semantic_inference(payload, API_Key):
    if not API_Key:
        return {}

#Connect gemini now
    genai.configure(api_key = API_Key)
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
    
    prompt = f"""
    Analyze this email preview payload. Classify it strictly as one of these: 'confirmation', 'rejection', 'assessment'. If none, classify as 'noise'.
    Extract the clean company name, exact job role title, and any mentioned salary/compensation details.
    Return ONLY a raw, valid JSON object matching this schema precisely without markdown wrappers:
    {{"category": "confirmation/rejection/assessment/noise", "company": "String", "role": "String", "salary": "String or Not Mentioned"}}
    
    Payload: {payload}
    """
    try:
        response = model.generate_content(prompt)
        clean_json_str = re.sub(r'```json\s*|```', '', response.text).strip()
        return json.loads(clean_json_str)
    except:
        return {"category": "noise", "company": "Unknown", "role": "Unknown", "salary": "Not Mentioned"}

#Pipeline

if run_pipeline:
    if not api_key_input:
        st.warning("Gemini API key not defined")
        st.stop()

    formatted_start = start_dt.strftime("%Y/%m/%m")
    formatted_end = end_dt.strftime("%Y/%m/%m")

    progress_bar = st.progress(0)
    st.info("Loading the details... Initialising connection endpoints")

#Process multiple email inputs sequentially

    for token_index, token_path in enumerate(TOKENS):
        creds = authentication_endpoint(token_path)
        gmail_service = build('gmail','v1', credentials= creds)

        server_query = f"after:{start_dt.strftime('%Y/%m/%d')} before:{end_dt.strftime('%Y/%m/%d')}"
        message_stream = gmail_service.users().messages().list(userId='me', q=server_query).execute()
        messages = message_stream.get('messages', [])

        for current_index, message in enumerate(messages):
            meta = gmail_service.users().messages().get(userId='me', id=msg['id'], format = 'metadata', metaHeaders = ['Subject']).execute()
            body_preview = f"Subject: {meta.get('snippet', '')}"

        #First filter to remove other emails except the job related
            if not any(kw in body_preview.lower() for kw in KEYWORDS):
                continue
            
        #Second filter 
            analysis = run_semantic_inference(body_preview, api_key_input)
            category = analysis.get("category")
            company = analysis.get("company", "Unknown").strip()


def generate_account_token(token_name):
    print(f"\n--- Authenticating: {token_name} ---")

    flow = InstalledAppFlow.from_client_secrets_file('credentials.json',SCOPES)
    creds= flow.run_local_server(port=0)

    with open(token_name='w') as token_file:
        token_file.write(creds.to_json())
    print(f"\n--- Success: {token_name} created. ---")

for account_token in TOKENS:
    if not os.path.exists(account_token):
        generate_account_token(account_token)

##AI context and semantic structure


##Pipeline orchestration

## Semantic logic for analysis

## Get the email meta data and body preview

## FILTER 1: quick scan body preview keywords through the KEYWORDS dict

# FILTER 2: Get rest of the data like company, role, salary

# Describe the primary key using the Subject line of the email

# Check the email is present in the master store json if it is we UPSERT else its a new application.

## Ghosted logic

## After all the mutated data is in the master_store dict we dump into the json 

## Data visualization layer