# backend/processor.py
from io import BytesIO
import pandas as pd

# ここでpdfplumberやPyPDF2などを使って独自実装する
def pdf_to_records(file_like) -> list[dict]:
    # --- ダミー実装：実際はPDFから抽出したデータを返す ---
    # file_like は st.file_uploader のUploadedFileやBytesIOが入る想定
    # 例: return [{"page": 1, "text": "..."}, ...]
    return [{"col1": "a", "col2": 1}, {"col1": "b", "col2": 2}]

def process_pdf_to_csv(file_like) -> tuple[pd.DataFrame, bytes]:
    records = pdf_to_records(file_like)
    df = pd.DataFrame(records)
    buf = BytesIO()
    df.to_csv(buf, index=False)
    return df, buf.getvalue()