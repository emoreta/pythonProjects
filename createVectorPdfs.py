import chromadb
from sentence_transformers import SentenceTransformer
from langchain.document_loaders import PyPDFLoader
import os

# Ruta donde se encuentra la base de datos persistente
db_path = "./chroma_db_pdf_3"

# Crear cliente Chroma con la base de datos persistente
client = chromadb.PersistentClient(path=db_path)

# Nombre de la colección
collection_name = "document_collection_pdfs"

# Crear o acceder a la colección
collection = client.get_or_create_collection(name=collection_name)

# Lista de archivos PDF a cargar
pdf_files = ["Amigo - Juan Iván Cueva.pdf","Acción Democrática Nacional - Daniel Noboa Azín.pdf","Avanza - Luis Tillería.pdf"
             ]  # Agrega más rutas si tienes múltiples PDFs

# Inicializar modelo de embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')  # Puedes elegir otro modelo preentrenado

# Procesar cada archivo PDF
for pdf_file in pdf_files:
    # Cargar y leer el contenido del PDF
    loader = PyPDFLoader(pdf_file)
    pages = loader.load_and_split()  # Dividir en páginas o fragmentos si es necesario
    print(f"*******Paginas:{pages}")
    # Procesar cada página o fragmento
    for i, page in enumerate(pages):
        document_text = page.page_content
        #print(document_text)

        # Calcular embedding para el texto del fragmento
        document_embedding = model.encode([document_text])[0]

        # Metadata asociada al fragmento
        metadata = {"source": pdf_file, "page": i + 1}

        # Generar un ID único para cada fragmento
        doc_id = f"{os.path.basename(pdf_file)}_page_{i + 1}"
        #print(f"DOC ID {doc_id} ")

        # Insertar el fragmento en la colección
        collection.add(
            documents=[document_text],  # El contenido del fragmento
            embeddings=[document_embedding],  # El embedding del fragmento
            metadatas=[metadata],  # Metadata del fragmento
            ids=[doc_id],  # ID único para el fragmento
        )

        #print(f"Fragmento de página {i + 1} cargado en Chroma: {pdf_file}")

# Confirmar que todos los documentos han sido procesados
print(f"Todos los PDFs han sido cargados en Chroma.")
collectionList = client.get_collection(name="document_collection_pdfs")
print(collectionList.peek())


