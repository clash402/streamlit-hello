import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


# Day 5: st.write()
st.header("Day 5: st.write()")

st.subheader("_This_ is a :blue[subheader]")
st.subheader("This is a subheader with a dividers", divider=True)


# st.write() is a general-purpose command that can write a wide variety of data types to your app.
st.markdown("*Streamlit* is **really** ***cool*** :sunglasses:")
st.markdown(
    """
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text."""
)

# You can write plain text, Markdown, images, dataframes, and even interactive charts.
st.write(1234)
st.write({"name": "John", "age": 30})

st.caption("This is a string that explains something above.")

st.code("print('Hello!')", language="python")


# You can also write dataframes and interactive charts.
df1 = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
st.write(df1)
st.write("Table Header", df1, "Table Footer")


# You can also write interactive charts.
df2 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
chart = (
    alt.Chart(df2)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.write(chart)
