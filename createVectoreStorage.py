import chromadb
from sentence_transformers import SentenceTransformer
import os

# Ruta donde se encuentra la base de datos persistente
db_path = "./chroma_db1"

# Crear cliente Chroma con la base de datos persistente
client = chromadb.PersistentClient(path=db_path)

# Nombre de la colección
collection_name = "document_collection_elecciones1"

# Crear o acceder a la colección
collection = client.get_or_create_collection(name=collection_name)

# Ruta del archivo .txt que quieres cargar
file_path = "C:/ProjectPython/TranscribeToText/dataElecciones/textoObtenidoPagina.txt"

# Leer el archivo .txt
with open(file_path, 'r', encoding='utf-8') as file:
    document_text = file.read()

# Calcular embeddings para el texto del documento utilizando SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')  # Puedes elegir otro modelo preentrenado
document_embedding = model.encode([document_text])[0]  # Devuelve un solo embedding

# Metadata asociada al documento (puedes agregar más campos según sea necesario)
metadata = {"source": "file.txt", "author": "Autor desconocido"}

# Insertar el documento con su embedding y metadata en la colección
collection.add(
    documents=[document_text],  # El contenido del documento
    embeddings=[document_embedding],  # El embedding del documento
    metadatas=[metadata],  # Metadata del documento
    ids=["doc_1"],  # ID único para el documento
)

# Confirmar que el documento se ha agregado
print(f"Documento cargado en Chroma: {file_path}")
