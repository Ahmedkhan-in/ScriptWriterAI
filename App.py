import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

st.title("Scripting Assistant")

model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

purpose = st.selectbox(
    'Select the purpose of the script', 
    ['YouTube vlog', 'motivational speech ',
     'product ad', 'presentation', 'storytelling', 'explainer video'])


audience = st.multiselect(
    'Select the target audience', 
    ['children', 'teenagers', 'adults', 'seniors', 'professionals', 
     'general public', 'Students', 'Professors'])


ToneNStyle = st.selectbox(
    'Select the tone and style',    
    ['formal', 'informal', 'humorous', 'serious', 'enthusiastic', 
     'persuasive', 'educational', 'narrative', 'Whatever suites best based on the purpose and audience'])

length = st.selectbox(
    'Select the length of the script', 
    ['short (1-2 minutes)', 'medium (3-5 minutes)', 'long (6-10 minutes)'])

Topic = st.text_input('Enter the topic or theme of the script or transcript here')

main_points = st.text_area('Enter the main points or key messages to be included in the script here')

Example = st.text_area('Provide any examples or references for style or content (optional)')

Context = st.text_area('Provide any additional context or background information (optional)')

if st.button('Generate Script'):
    prompt_template = """You are a professional scriptwriter. 
    Create a {length} script for a {purpose} targeting {audience} with a {ToneNStyle} tone and style. 
    The topic is "{Topic}". 
    Include the following main points: {main_points}. 
    {Example_section}
    {Context_section}
    Ensure the script is engaging and well-structured."""
    
    Example_section = f"Here are some examples or references for style or content: {Example}." if Example else ""
    Context_section = f"Additional context or background information: {Context}." if Context else ""
    
    prompt = PromptTemplate(
        input_variables=["length", "purpose", "audience", "ToneNStyle", "Topic", "main_points", "Example_section", "Context_section"],
        template=prompt_template
    ).format(
        length=length,
        purpose=purpose,
        audience=", ".join(audience) if audience else "general public",
        ToneNStyle=ToneNStyle,
        Topic=Topic,
        main_points=main_points,
        Example_section=Example_section,
        Context_section=Context_section
    )
    
    result = model.invoke(prompt)
    st.write(result.content)# This code creates a Streamlit UI for generating scripts based on user-defined parameters using the Google Gemini Pro model.