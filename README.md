# Harsh 0145 — Project Portfolio Hub

A single public landing page for two deployed Streamlit projects. Use this hub when a submission portal accepts one repository URL and one deployment URL.

## Projects

1. **Experimentation & Causal Inference Platform**
   - [Live demo](https://zvp22qb4mn3uu7j4ilsle6.streamlit.app/)
   - [GitHub repository](https://github.com/Harsh0145/Experimentation-Causal-Inference-platform)
2. **Customer Lifetime Value & Churn Intelligence**
   - [Live demo](https://customer-lifetime-value-churn-intelligence-kw6zdgdzjigfrevjxo2.streamlit.app/)
   - [GitHub repository](https://github.com/Harsh0145/Customer-Lifetime-Value-Churn-Intelligence)

## Run locally

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

## Deploy

Deploy `app.py` from this repository on Streamlit Community Cloud. The app only needs Streamlit and has no secrets or external data requirements.
