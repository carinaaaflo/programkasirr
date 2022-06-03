import streamlit as st

st.title("Kasir Chilless Cafe")
st.write("-------------------------- Selamat Datang Di Chilless Cafe --------------------------")

nama = st.text_input("Masukkan Nama Anda")
menu = {
    "Chicken Ball":                23000,
    "French Fries" :               15000,
    "Vanila Latte" :               18000,
    "Rose Tea" :                   15000,
    "Dumpling" :                   12000,
    "Ice Cream" :                  10000,
    "Pecel Buaya Darat" :         200000,
    "Nasi Goreng Cacing Kremi" :  150000,  
}
st.write("                      Chilless Cafe                      ")
st.write("====================== Daftar Menu ======================")
for i in menu:
    st.write("Daftar Menu : ", i, "\t Harga : ", menu[i])
st.wite("pembelian diatas Rp 100.000,- mendapat diskon 10%")
st.write("=========================================================")
beli = st.text_input("Pilih Menu : ")
jumlah = st.number_input("Jumlah Pesanan :")
bayar = jumlah * menu[beli]

if bayar > 100000:
    diskon = bayar*10/100
    total = bayar - diskon
else:
    total = bayar

st.write("====================== Detail Pembayaran ======================")
st.write("Menu yang dipesan        : ",beli)
st.write("Jumlah yang dipesan      : ",jumlah)
st.write("Total Biaya              : ",bayar)
st.write("Total yang harus dibayar :",total)
