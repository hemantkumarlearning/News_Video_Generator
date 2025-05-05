from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 


def generate_script_with_llama(headline):
    prompt_template = PromptTemplate(
        input_variables=["headline"],
        template="""
        You are a professional scriptwriter for short, engaging news videos.

        Write a 6-line video script about the headline below. The first line should be:

        "Here is today’s top news:"

        Then follow with 5 informative and conversational lines explaining the news, without mentioning this is a script or giving any extra explanation.

        Headline: {headline}
        
        Script:
        """
    )

    # I am using Llama model through groq bcz it is very fast and smooth.
    llm = ChatGroq(temperature=0, groq_api_key="GROQ-API-KEY", model_name='llama-3.3-70b-versatile') 
    chain = LLMChain(prompt=prompt_template, llm=llm)
    
    response = chain.run(headline)
    return response.strip().split('\n')

