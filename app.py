import streamlit as st
from services import process_uploaded_file

st.title("Obtendo um arquivo")

arquivo = st.file_uploader(
    "Escolha um arquivo", type=["py", "csv", "xlsx", "json"]
)

if arquivo:
    content_type, data = process_uploaded_file(arquivo)

    match content_type:
        case "dataframe":
            st.dataframe(data)

        case "code":
            st.code(data, language="python")

        case "json":
            st.json(data)

        case "video":
            st.video(data)

        case "audio":
            st.audio(data)

        case _:
            st.error("Formato de arquivo não suportado.")