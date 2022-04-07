import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit 超入門')

st.write('プログレスバー')
'Start!!'

button = st.button('このボタンを押すとスタート')

latest_iteration = st.empty()
bar = st.progress(0)

if button:
    for i in range(100):
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

'Done!'

left_column, right_column = st.columns(2)
button = left_column.button('ここを押すと右カラムに表示')

if button:
    right_column.write('ここは右カラム')

expander_1 = st.expander('問い合わせ１')
ex = expander_1.button('1')
expander_1.write('2')
expander_2 = st.expander('問い合わせ2')
expander_2.write('3')

if ex:
    st.write('ボタンが押されました')
