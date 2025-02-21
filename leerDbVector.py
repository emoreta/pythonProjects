import chromadb
from sentence_transformers import SentenceTransformer

# Ruta donde se encuentra la base de datos persistente
db_path = "./chroma_db_pdf"

# Crear cliente Chroma con la base de datos persistente
client = chromadb.PersistentClient(path=db_path)

# Nombre de la colección
collection_name = "document_collection_pdfs"

# Crear o acceder a la colección
collection = client.get_or_create_collection(name=collection_name)

# Inicializar el modelo para generar embeddings de la consulta
model = SentenceTransformer('all-MiniLM-L6-v2')  # Puedes elegir otro modelo preentrenado

# Texto de la consulta
query = "¿Sobre qué trata el documento?"

# Calcular el embedding para la consulta (para comparar con los documentos)
query_embedding = model.encode([query])[0]

# Realizar la consulta
query_result = collection.query(
    query_embeddings=[query_embedding],
    n_results=15  # Número de resultados a recuperar
)

# Mostrar los resultados
print("Consulta:", query)
print("Resultados encontrados:")
for i, result in enumerate(query_result['documents']):
    print(f"Resultado {i + 1}:")
    print(f"Texto del documento: {result}")
    print(f"Metadata: {query_result['metadatas'][i]}")
    print(f"ID: {query_result['ids'][i]}")
    print("-" * 30)
