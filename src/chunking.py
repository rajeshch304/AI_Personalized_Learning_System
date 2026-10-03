'''def chunking(text,chunksize=1000,overlap=100):
    chunks=[]
    start=0
    while start < len(text):
        end=start+chunksize
        chunks.append(text[start:end])
        start=end-overlap
    return chunks'''
def chunking(text, chunksize=1000, overlap=100):
    """
    Splits text into overlapping chunks safely.
    
    Args:
        text (str): input text
        chunksize (int): size of each chunk
        overlap (int): overlap between chunks
    
    Returns:
        list: list of text chunks
    """

    if overlap >= chunksize:
        raise ValueError("overlap must be smaller than chunksize")

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunksize
        chunk = text[start:end]
        chunks.append(chunk)

        # move forward with overlap
        start = start + (chunksize - overlap)

    return chunks
    