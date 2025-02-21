import chromadb
from together import Together
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

# Inicializar el cliente de Together
api_key = "6d63b30d07cd19e252baf2dfafad9d5880440d6e9889a8a4497f3a08aef6d15c"
client_together = Together(api_key=api_key)

# Inicializar cliente Chroma con la base de datos persistente
db_path = "./chroma_db_pdf_amigo"  # La ruta donde tienes tu base de datos Chroma persistente
client_chroma = chromadb.PersistentClient(path=db_path)

# Nombre de la colección donde tienes tus documentos guardados
collection_name = "document_collection_pdfs"
collection = client_chroma.get_or_create_collection(name=collection_name)
#print(collection)

# Inicializar embeddings con HuggingFace
model_name = "all-MiniLM-L6-v2"
hf_embeddings = HuggingFaceEmbeddings(model_name=model_name)

# Inicializar el vectorstore de Chroma
vectorstore = Chroma(client=client_chroma, collection_name=collection_name, embedding_function=hf_embeddings)
#print(vectorstore)
# Función para recuperar documentos relevantes
def retrieve_documents(query, retriever, k=3):
    return retriever.similarity_search(query, k=k)

# Función para generar respuesta utilizando el modelo de AI
def generate_response(query, retrieved_docs):
    print(retrieved_docs)
    # Combinar los documentos recuperados en un solo contexto
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])
    #print(context)
    prompt = f"Contexto:\n{context}\n\nPregunta: {query}\nRespuesta:"

    # Llamada al modelo para generar la respuesta usando el cliente de Together
    response = client_together.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1.2,
        #stop=["\n", "\n\n"],
        stop=["<|eot_id|>", "<|eom_id|>"],
        stream=False,
    )

    # Concatenar la respuesta generada
    result = ""
    if response and hasattr(response, "choices") and response.choices:
        return response.choices[0].message.content
    else:
        print("La respuesta de Together AI no contiene datos válidos:", response)
        return "Hubo un problema al generar la respuesta."
    return result

# Realizar consulta
query = "que propone Juan Ivan Cueva?"
retrieved_documents = retrieve_documents(query, vectorstore, k=3)
#print("Documentos recuperados:", retrieved_documents)
# Generar respuesta con los documentos recuperados
answer = generate_response(query, retrieved_documents)

# Imprimir la respuesta generada
print("Respuesta generada:", answer)
