import os 
import logging
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
from langchain_chroma import Chroma

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("Ingestion_Pipeline")
logger.info("Initializing HuggingFace Embeddings Model...")
embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

pdfpath = r"C:\Users\UTKARSH\Desktop\AI_AGENT_Office_policy_project\Policy_PDF.pdf"
persist_db_directory = "./chroma_policy_db"

logger.info(f"Opening and reading PDF file from: {pdfpath}")
try:
    documents = PdfReader(pdfpath)
    raw_text =""

    for page in documents.pages:
        page_text = page.extract_text()
        if page_text:
            raw_text += page_text + "\n"
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_text(raw_text)
    logger.info(f"Successfully extracted text from {len(documents.pages)} PDF pages.")
except Exception as e:
    logger.error(f"Failed to read PDF: {str(e)}")
    raise

logger.info("Splitting text into logical chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_text(raw_text)
logger.info(f"Generated {len(texts)} text chunks for Vector Database storage.")

vector_store = Chroma.from_texts(
        texts=texts,
        embedding=embeddings_model,
       persist_directory=persist_db_directory
    )
logger.info("Successfully saved all document chunks to Chroma Database!")