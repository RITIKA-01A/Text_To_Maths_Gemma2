import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain,LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool ,initialize_agent
from dotenv import load_dotenv
from langchain.callbacks import StreamlitCallbackHandler

## Set up the streamlit app
st.set_page_config(page_title="Text to Math Problem Solver And Data Search Assistant",page_icon = "")
st.title("Text To Math Problem Solver Using Google Gemma 2")

groq_api_key = st.sidebar.text_input("Enter the api key",type="password")

if not groq_api_key:
    st.info("Please add the groq api key to continue")
    st.stop()


llm = ChatGroq(groq_api_key=groq_api_key,model_name = "Gemma2-9b-It") 


## Initialise the tools
wikipedia_wrapper=WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name='Wikipedia',
    func = wikipedia_wrapper.run,
    description="A tool for searching the internet to find the various information on the topics mentioned"

)

## Initialise the math tool
math_chain=LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name="calculator",
    func=math_chain.run,
    description="A tool for answering math related question.Only input mathematical expression needs to be provided"
)


prompt="""
You are a agent tasked for solving users mathematical questions.Logically arrive at the solution and  give a detailed explanation
and display it point wise for the question below.
Question : {question}
Answer : 
"""
template = PromptTemplate(
    template = prompt,
    input_variables=['question']
)

## Combining all the tools into chain
chain = LLMChain(llm = llm,prompt=template)

reasoning_tool = Tool(
    name='Reasoning tool',
    func=chain.run,
    description = "A Tool for answering logic_based and reasoning questions."
)

# Initialise the agents

assitant_agent = initialize_agent(
    tools=[wikipedia_tool,calculator,reasoning_tool],
    llm = llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)


if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {'role':"assistant" ,"content":"Hi,I am MATH chatbot who can aswer all your maths question"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])


## function to generate the response
def generate_response(question):
    response=assitant_agent.invoke({'input':question})
    return response


## Starting the instruction
question = st.text_area("Enter your question : ")
if st.button("find my answer"):
    if question:
        with st.spinner("Generating the response ..."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)


            st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response=assitant_agent.run(st.session_state.messages,callbacks=[st_cb])


            st.session_state.messages.append({"role":"assistant",'content':response})
            st.write("### Response")
            st.success(response)

    else:
        st.write("Please enter the question")
