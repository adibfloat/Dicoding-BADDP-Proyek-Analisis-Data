import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime


def buat_musim_pembagian_sepeda_df(df):
    musim = df.groupby(by="season").instant.nunique().reset_index()
    musim.rename(columns={
        "season": "musim",
        "instant": "jumlah"
    }, inplace=True)
    return musim


def buat_tahun_pembagian_sepeda_df(df):
    tahun = df.groupby(by="yr").instant.nunique().reset_index()
    tahun.rename(columns={
        "yr": "tahun",
        "instant": "jumlah"
    }, inplace=True)
    return tahun


def sidebar(df):
     df["dteday"] = pd.to_datetime(df["dteday"])
     min_date = df["dteday"].min()
     max_date = df["dteday"].max()

     with st.sidebar:
         

         def on_change():
             st.session_state.date = tanggal

         tanggal = st.date_input(
             label="Rentang Waktu",
             min_value=min_date,
             max_value=max_date,
             value=[min_date, max_date],
             on_change=on_change
         )

         st.image("https://github.com/adibfloat/Dicoding-BADDP-Proyek-Analisis-Data/assets/58215987/1087aed9-9b17-4213-b1c4-2b4542f10367")

     return tanggal

# -------------------------------------------------------------------------------

# Hubungan antara Jumlah Penyewa berdasarkan musim

def musim(df):
    st.subheader("Penyewaan Sepeda Berdasarkan Musim")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="musim",
        y="jumlah",
        data=df.sort_values(by="musim", ascending=False),
        palette='tab10',
        ax=ax
    )
    ax.set_title(None)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

# Hubungan antara Jumlah Penyewa berdasarkan tahun


def tahun(df):
    st.subheader("Penyewaan Sepeda Berdasarkan Tahun")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="tahun",
        y="jumlah",
        data=df.sort_values(by="tahun", ascending=False),
        palette='tab10',
        ax=ax
    )
    ax.set_title(None)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

# Hubungan antara Jumlah Penyewa berdasarkan bulan


def bulan(df):
    st.subheader("Penyewaan Sepeda Berdasarkan Bulan")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="mnth",
        y="cnt",
        data=df.sort_values(by="mnth", ascending=False),
        palette="hls",
        ax=ax
    )
    ax.set_title(None)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

if __name__ == "__main__":
    sns.set(style="dark")

    st.header("Bike Sharing Dashboard")

    day_df = pd.read_csv(
         "https://raw.githubusercontent.com/adibfloat/Dicoding-BADDP-Proyek-Analisis-Data/main/submission/dashboard/main_data.csv")

    date = sidebar(day_df)
    if (len(date) == 2):
        main_df = day_df[(day_df["dteday"] >= str(date[0])) &
                          (day_df["dteday"] <= str(date[1]))]
    else:
        main_df = day_df[(day_df["dteday"] >= str(st.session_state.date[0])) & (
             day_df["dteday"] <= str(st.session_state.date[1]))]

    col1, col2 = st.columns(2)

    with col1:
        total_penyewa = main_df['cnt'].sum()
        st.metric(label="Total Rental Dari Semua Pengguna", value=total_penyewa)

    with col2:
        total_record = main_df['instant'].count()
        st.metric(label="Total Record", value=total_record)

season_df = buat_musim_pembagian_sepeda_df(main_df)
musim(season_df)
year_df = buat_tahun_pembagian_sepeda_df(main_df)
tahun(year_df)
bulan(main_df)

st.caption("© 2023" + " By Adib Niatno")
