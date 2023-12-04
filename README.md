![screenshot dashboard](https://github.com/adibfloat/Dicoding-BADDP-Proyek-Analisis-Data/assets/58215987/62c78cab-c2ff-4206-8f52-79c4a4eb9cf7)
Link streamlit cloud: https://vuphyvmtvxkxwhcxqygayx.streamlit.app/
# Cara Menjalankan Dashboard pada personal Env
1. Salin Repositori
```sh
git clone https://github.com/adibfloat/Dicoding-BADDP-Proyek-Analisis-Data.git
```
2. Setup environment
```sh
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
```
3. Pindah direktori ke Dicoding-BADDP-Proyek-Analisis-Data\submission\dashboard
```sh
cd 'Dicoding-BADDP-Proyek-Analisis-Data\submission\dashboard'
```
4. Run streamlit
```sh
streamlit run dashboard.py
```
