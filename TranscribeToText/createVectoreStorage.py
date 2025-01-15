import os
import chromadb
print(os.environ.get('REQUESTS_CA_BUNDLE'))
# Función para leer los documentos desde una carpeta
def read_documents_from_folder(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath) and filename.endswith(".txt"):  # Filtra archivos .txt
            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()
                documents.append(text)
    return documents

# Leer documentos desde la carpeta 'data'
documents = read_documents_from_folder('data')

# Crear cliente Chroma (sin configuración adicional)
client = chromadb.Client()

# Crear una colección (almacén de vectores)
collection = client.create_collection("document_collection2", persist_directory="./chroma_db")

# Inserción de documentos en Chroma
for doc_id, doc_text in enumerate(documents):
    collection.add(
        documents=[doc_text],        # El contenido de texto del documento
        metadatas=[{"source": f"doc_{doc_id}"}],  # Metadata del documento
        ids=[f"doc_{doc_id}"],  # ID único para cada documento
    )

# Realizar una consulta
query = "¿Cuál es el tema principal?"
query_result = collection.query(query_texts=[query], n_results=1)

# Mostrar los resultados
print("Consulta:", query)
print("Resultados encontrados:", query_result)
