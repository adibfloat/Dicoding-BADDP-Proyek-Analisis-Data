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
