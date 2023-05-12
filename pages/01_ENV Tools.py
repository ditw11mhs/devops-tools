import streamlit as st

from api import utils
from api.logic.env import env2json


def main():
    st.header("ENV Tools")
    st.subheader("Notes: no file is saved to server")
    file = st.file_uploader("Upload your json file here")
    str_content = st.text_area("Paste your json file content file here")

    to_json_btn = st.button("Convert to json")

    if file and str_content:
        st.error("You can use only one input method at a time")
    elif not file and not str_content:
        st.info("Please upload a file or paste the file content in the textarea above")
    else:
        if to_json_btn:
            utils.apply_func(
                file=file,
                str_content=str_content,
                func=env2json,
                captions="Converted to env",
                language="bash",
            )


if __name__ == "__main__":
    main()
