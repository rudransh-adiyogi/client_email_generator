import os
from langchain_groq import ChatGroq ###llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()
### get the api key from .env file
#"llama-3.1-70b-versatile"
print(os.getenv("GROQ_API_KEY"))
class Chain:
    def __init__(self,model_name):
        groq_api_key=os.getenv("GROQ_API_KEY")
        self.model_name=model_name
        self.groq_llm = ChatGroq(groq_api_key=groq_api_key,temperature=0,model_name=self.model_name)
        
    def extract_job_description(self,cleaned_text):
        prompt_extract = PromptTemplate.from_template(
        """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the career's page of a website.
        Your job is to extract the job postings and return them in JSON format containing the 
        following keys: `role`, `experience`, `skills` and `description`.
        Only return the valid JSON.
        ### VALID JSON (NO PREAMBLE):    
        """)
        chain_extract = prompt_extract | self.groq_llm ### chain
        res = chain_extract.invoke(input={'page_data':cleaned_text})
        try:
            json_parser = JsonOutputParser()
            json_res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return json_res if isinstance(json_res, list) else [json_res]
    def write_cold_mail(self,job_description,link_list):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are XYZ, a business development executive at ABC. ABC is an AI & Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools. 
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
            process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a cold email to the client regarding the job mentioned above describing the capability of ABC 
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase ABC's portfolio: {link_list}
            Remember you are XYZ, BDE at ABC. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_create_mail= prompt_email|self.groq_llm
        res_mail = chain_create_mail.invoke(input={'job_description':job_description,'link_list':link_list})
        return res_mail.content



