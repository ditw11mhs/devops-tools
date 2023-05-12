import plotly.graph_objects as go
import streamlit as st


def apply_func(file, str_content, func, captions="Output", language="bash"):
    if file:
        out = func(file=file)
    else:
        out = func(str_content=str_content)

    st.subheader(captions)
    st.code(out, language=language)
    return out


def add_one_line(fig, df, x, y, name):
    fig.add_trace(
        go.Scattergl(
            x=df[x],
            y=df[y],
            name=name,
            mode="lines",
        )
    )


def add_one_scatter(fig, df, x, y, name):
    fig.add_trace(
        go.Scattergl(
            x=df[x],
            y=df[y],
            name=name,
            mode="markers",
        )
    )


def add_line(fig, df, x, y, names):
    if len(y) != len(names):
        raise Exception("Length y != Length name")

    for col, name in zip(y, names):
        add_one_line(fig, df, x, col, name)


def add_scatter(fig, df, x, y, names):
    if len(y) != len(names):
        raise Exception("Length y != Length name")

    for col, name in zip(y, names):
        add_one_scatter(fig, df, x, col, name)
