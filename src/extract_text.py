import fitz
#pdf_path="../data/The_Verdict_book.pdf"
import os
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
pdf_path=os.path.join(BASE_DIR,"data","FullStack_DataScience_RAG_Notes.pdf")
doc=fitz.open(pdf_path)
text=""
for page in doc:
    text+=page.get_text()+"\n"
print(text)
print(len(text))
