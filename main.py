import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from langchains import Chain
from CreatePortfolioDatabase import Portfolio
from utils import clean_text

def create_streamlit_app(chain_x, portfolio):
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-45852?from=job%20search%20funnel")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.CreateDatabase()
            jobs=chain_x.extract_job_description(data)
            print(jobs)
            for job in jobs:
                links=portfolio.get_links(job)
                email=chain_x.write_cold_mail(jobs,links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")

if __name__ == "__main__":
    chain_x=Chain("llama-3.3-70b-versatile")
    portfolio_file_path="resource/my_portfolio.csv"
    portfolio=Portfolio(portfolio_file_path)
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain_x, portfolio)
