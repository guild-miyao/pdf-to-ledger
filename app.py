# streamlit_app.py
import streamlit as st
from io import BytesIO
import pandas as pd
from backend.processor import process_pdf_to_csv

st.set_page_config(page_title="PDF → CSV Converter", page_icon="📄", layout="centered")

st.title("📄 PDF → CSV 変換")

uploaded = st.file_uploader("PDFをアップロード", type=["pdf"])

# 変換ボタンを明示
convert_clicked = st.button("変換する", type="primary", disabled=uploaded is None)

if convert_clicked and uploaded is not None:
    with st.spinner("変換中..."):
        try:
            # StreamlitのUploadedFileはfile-likeなので、そのまま渡してOK
            df, csv_bytes = process_pdf_to_csv(uploaded)

            st.success("変換が完了しました！")
            # 先頭プレビュー
            if not df.empty:
                st.write("プレビュー（先頭）")
                st.dataframe(df.head(50), use_container_width=True)
            else:
                st.info("抽出結果が空でした。PDFの内容をご確認ください。")

            st.download_button(
                label="CSVをダウンロード",
                data=csv_bytes,
                file_name="converted.csv",
                mime="text/csv",
            )
        except Exception as e:
            st.error(f"変換に失敗しました: {e}")

with st.expander("注意点"):
    st.markdown(
        "- 大きいPDFや複雑なレイアウトは処理に時間がかかる場合があります。\n"
        "- アップロードしたファイルは処理のために一時的にメモリ上で扱います。\n"
        ""
    )
