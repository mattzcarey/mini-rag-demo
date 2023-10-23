from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import BedrockChat, ChatOpenAI

from demo.constants.settings import SETTINGS
from demo.llm.retriever import configure_retriever

"""
Configure your LLM Chain to use for this personal assistant.
"""
def get_qa_chain(uploaded_files, memory, model_provider):
    # Configure a LLM to use:
    if model_provider == "OpenAI":
        llm = ChatOpenAI(
            openai_api_key=SETTINGS.openai_api_key.get_secret_value(),
            model=SETTINGS.openai_model,  # type: ignore
            temperature=SETTINGS.temperature,
            streaming=True,
        )
    elif model_provider == "Amazon Bedrock":
        llm = BedrockChat(
            region_name=SETTINGS.aws_region,
            model_id=SETTINGS.bedrock_model_id,
            streaming=True,
        ) # type: ignore
    else:
        raise ValueError(f"Unknown LLM provider: {model_provider}")

    # Configure the retriever
    retriever = configure_retriever(uploaded_files, model_provider)

    # ConversationalRetrievalChain
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm, retriever=retriever, memory=memory, verbose=True,
    )

    return qa_chain
