# client_email_generator
Cold email generator for services company using groq, langchain and streamlit. It allows users to input the URL of a company's careers page. The tool then extracts job listings from that page and generates personalized cold emails. These emails include relevant portfolio links sourced from a vector database, based on the specific job descriptions. 

**Imagine a scenario:**

- Nike needs a Director Supply Chain AIML Engineer and is spending time and resources in the hiring process, on boarding, training etc
- ABC is a AI & Software Consulting company and can provide a dedicated AIML engineer to Nike. So, the business development executive XYZ from ABC is going to reach out to Nike via a cold email.

# Email Example
Subject: Expert AI & Software Consulting Services for Nike's Supply Chain AIML Engineering

Dear Hiring Manager,

I came across the job posting for Director Supply Chain AIML Engineer at Nike, and I am excited to introduce ABC, a leading AI & Software Consulting company. With our expertise in developing productionized code in software or data engineering, machine learning, and related fields, we are confident that we can support Nike in delivering scalable machine learning and artificial intelligence solutions.

Our team at ABC has a strong background in machine learning, data science, software engineering, and leadership, aligning perfectly with the requirements of the role. We have experience working with various technologies such as Scikitlearn, Dask, Tensorflow, Kubeflow, Spark, and EMR, which are essential for building and deploying AI and ML models.

We have a proven track record of empowering numerous enterprises with tailored solutions, fostering scalability, process optimization, cost reduction, and heightened overall efficiency. Our portfolio includes successful projects in machine learning and Python, which can be viewed at https://example.com/ml-python-portfolio. Additionally, our expertise in devops, as showcased at https://example.com/devops-portfolio, can help Nike streamline its AI and ML workflows.

At ABC, we understand the importance of agile frameworks, ETL, ML, and analytics in driving business growth. Our team is well-versed in these areas and can help Nike develop and implement AI and ML solutions that meet its specific needs.

I would be delighted to discuss how ABC can support Nike in achieving its goals. Please feel free to contact me to schedule a call to explore further.

Best regards,

XYZ

Business Development Executive

ABC

## Architecture Diagram
![img.png](imgs/architecture.png)

## Set-up
1. To get started we first need to get an API_KEY from here: https://console.groq.com/keys. Inside `.env` update the value of `GROQ_API_KEY` with the API_KEY you created. 


2. To get started, first install the dependencies using:
    ```commandline
     pip install -r requirements.txt
    ```
   
3. Run the streamlit app:
   ```commandline
   streamlit run main.py
   ```
   

Copyright (C) Codebasics Inc. All rights reserved.

**Additional Terms:**
This software is licensed under the MIT License. However, commercial use of this software is strictly prohibited without prior written permission from the author. Attribution must be given in all copies or substantial portions of the software.
