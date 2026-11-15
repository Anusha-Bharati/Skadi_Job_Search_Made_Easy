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