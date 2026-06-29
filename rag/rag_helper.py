from llm import retrieval_llm
from rag.retriever import retrieve_text


def get_retrieval(question: str):

    decision = retrieval_llm.invoke(
        f"""
Question:
{question}

You are a retrieval routing agent.

Your ONLY job is to decide whether the local vector database should be queried.

If the user is asking ANYTHING about:

- their CV
- their resume
- uploaded files
- uploaded documents
- local PDFs
- "this paper"
- "my paper"
- "my notes"
- "my report"
- "my thesis"
- "my project"
- "documents" folder
- anything the user previously uploaded

then ALWAYS set

use_rag = true

Examples

User:
What projects are on my CV?

use_rag=true

User:
Summarize my uploaded paper.

use_rag=true

User:
What skills do I have?

use_rag=true

User:
According to my resume what companies fit me?

use_rag=true

Only return use_rag=false if the answer does not depend on local documents.

Return

use_rag
retrieval_query
confidence
reason
"""
    )

    if not decision.use_rag:
        return "",decision

    return retrieve_text(decision.retrieval_query),decision