import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title("🧠 Smart Analytics Tool")

file = st.file_uploader(
    "Upload CSV",
    type="csv"
)

if file:

    df = pd.read_csv(file)

    st.subheader(
        "Dataset Preview"
    )

    st.dataframe(
        df.head()
    )

    st.subheader(
        "Missing Values"
    )

    st.write(
        df.isnull().sum()
    )

    st.subheader(
        "Statistical Summary"
    )

    st.write(
        df.describe()
    )

    numeric = df.select_dtypes(
        include=np.number
    ).columns

    if len(numeric) > 0:

        x = st.selectbox(
            "Select X",
            numeric
        )

        fig1 = px.histogram(
            df,
            x=x
        )

        st.plotly_chart(
            fig1
        )

        y = st.selectbox(
            "Select Y",
            numeric
        )

        fig2 = px.scatter(
            df,
            x=x,
            y=y
        )

        st.plotly_chart(
            fig2
        )

        fig3 = px.box(
            df,
            y=x
        )

        st.plotly_chart(
            fig3
        )

else:

    st.info(
        "Upload dataset"
    )