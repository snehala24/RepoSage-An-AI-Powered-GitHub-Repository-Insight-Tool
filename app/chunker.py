import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_files_from_repo(repo_path, allowed_extensions=None):
    if allowed_extensions is None:
        allowed_extensions = ['.py', '.md', '.txt', '.js', '.json', '.java', '.cpp', '.yaml', '.yml']

    all_files = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in allowed_extensions):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read().strip()
                        if content:
                            all_files.append({
                                "file_path": full_path,
                                "content": content
                            })
                except Exception as e:
                    print(f"❌ Error reading {full_path}: {e}")

    print(f"✅ Loaded {len(all_files)} text/code files.")
    return all_files


def chunk_files(file_data, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )

    all_chunks = []

    for file in file_data:
        chunks = splitter.split_text(file['content'])
        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "file_path": file["file_path"],
                "chunk_id": i,
                "content": chunk
            })

    print(f"✅ Chunked into {len(all_chunks)} pieces.")
    return all_chunks
