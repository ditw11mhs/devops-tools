import streamlit as st

from api import logic, utils
from api.logic.json import json2env, json_anonymizer


def main():
    st.header("JSON tools")
    st.subheader("Notes: no file is saved to server")
    file = st.file_uploader("Upload your json file here")
    str_content = st.text_area("Paste your json file content file here")

    c1, c2, _ = st.columns([1, 1, 2])
    to_env_btn = c1.button("Convert to env")
    anonym_btn = c2.button("Anonymize")

    if file and str_content:
        st.error("You can use only one input method at a time")
    elif not file and not str_content:
        st.info("Please upload a file or paste the file content in the textarea above")
    else:
        if to_env_btn:
            utils.apply_func(
                file=file,
                str_content=str_content,
                func=json2env,
                captions="Converted to env",
                language="bash",
            )

        if anonym_btn:
            utils.apply_func(
                file=file,
                str_content=str_content,
                func=json_anonymizer,
                captions="Anonymized JSON",
                language="json",
            )


if __name__ == "__main__":
    main()
