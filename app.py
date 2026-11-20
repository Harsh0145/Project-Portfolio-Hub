import streamlit as st

st.set_page_config(page_title="Harsh | Project Portfolio", page_icon="◈", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');
:root { --ink:#17251f; --muted:#65756d; --paper:#f5f6f2; --green:#315e49; --line:#dce4dc; }
html, body, [class*="css"] { font-family:'DM Sans',sans-serif; color:var(--ink); }
.stApp { background:var(--paper); }
.block-container { max-width:1120px; padding-top:3rem; }
.eyebrow { color:var(--green); font-size:.75rem; letter-spacing:.14em; font-weight:700; text-transform:uppercase; }
h1,h2,h3 { font-family:'Manrope',sans-serif; letter-spacing:-.04em; }
.project { background:white; border:1px solid var(--line); border-radius:16px; padding:26px; min-height:275px; }
.project-label { color:var(--green); font-size:.72rem; letter-spacing:.11em; font-weight:700; text-transform:uppercase; }
.project-title { font:700 1.45rem 'Manrope',sans-serif; margin:.55rem 0 .75rem; }
.project-copy { color:var(--muted); line-height:1.6; min-height:80px; }
footer { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="eyebrow">HARSH 0145 · PROJECT PORTFOLIO</div>', unsafe_allow_html=True)
st.title("Data projects, ready to explore")
st.write("Two interactive projects covering experimentation, causal inference, customer lifetime value, and churn.")
st.divider()

left, right = st.columns(2, gap="large")
with left:
    st.markdown("""
    <section class="project">
      <div class="project-label">Project 01</div>
      <div class="project-title">Experimentation &amp; Causal Inference Platform</div>
      <div class="project-copy">Plan A/B tests, analyze experiment results, and explore causal methods when randomization is unavailable. Includes a CSV upload demo.</div>
    </section>
    """, unsafe_allow_html=True)
    st.write("")
    a, b = st.columns(2)
    a.link_button("Open live demo", "https://zvp22qb4mn3uu7j4ilsle6.streamlit.app/", use_container_width=True)
    b.link_button("View GitHub repo", "https://github.com/Harsh0145/Experimentation-Causal-Inference-platform", use_container_width=True)
with right:
    st.markdown("""
    <section class="project">
      <div class="project-label">Project 02</div>
      <div class="project-title">Customer Lifetime Value &amp; Churn Intelligence</div>
      <div class="project-copy">Explore customer lifetime value and churn intelligence through an interactive Streamlit application.</div>
    </section>
    """, unsafe_allow_html=True)
    st.write("")
    a, b = st.columns(2)
    a.link_button("Open live demo", "https://customer-lifetime-value-churn-intelligence-kw6zdgdzjigfrevjxo2.streamlit.app/", use_container_width=True)
    b.link_button("View GitHub repo", "https://github.com/Harsh0145/Customer-Lifetime-Value-Churn-Intelligence", use_container_width=True)

st.divider()
st.caption("Built by Harsh0145 · Each project has its own public repository and live application.")
