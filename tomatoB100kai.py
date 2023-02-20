import streamlit as st
import pandas as pd
import base64
import csv
import os
import random

st.title('トマト100個の官能評価')
st.header('多量の２点識別の組合せから順序を導き出す官能評価')
st.subheader('')
st.write('①品質が良いと思う方の選択肢(左or右)を選んでください')
st.write('②選択肢を押し間違えても変更はできませんが,多量のデータから判断するため押し間違えは気にしないでください')
st.write('③選択肢を選んだら「画像更新」を押して,次の評価を行ってください')
st.write('④選択肢の下に表示される「結果ダウンロード」を押すと今までの評価結果がcsvファイルで見られます')
st.subheader('')


from PIL import Image

df = pd.read_csv('tomato-result.csv',encoding='cp932')
    
st.subheader("「良い」方を選んでください")
col1, col2, col3, col4, col5, col6= st.columns(6)
with col2:            
    if st.button("画像更新", key=1):
        lst_image = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg', '20.jpg', '21.jpg', '22.jpg', '23.jpg', '24.jpg', '25.jpg', '26.jpg', '27.jpg', '28.jpg', '29.jpg', '30.jpg', '31.jpg', '32.jpg', '33.jpg', '34.jpg', '35.jpg', '36.jpg', '37.jpg', '38.jpg', '39.jpg', '40.jpg', '41.jpg', '42.jpg', '43.jpg', '44.jpg', '45.jpg', '46.jpg', '47.jpg', '48.jpg', '49.jpg', '50.jpg', '51.jpg', '52.jpg', '53.jpg', '54.jpg', '55.jpg', '56.jpg', '57.jpg', '58.jpg', '59.jpg', '60.jpg', '61.jpg', '62.jpg', '63.jpg', '64.jpg', '65.jpg', '66.jpg', '67.jpg', '68.jpg', '69.jpg', '70.jpg', '71.jpg', '72.jpg', '73.jpg', '74.jpg', '75.jpg', '76.jpg', '77.jpg', '78.jpg', '79.jpg', '80.jpg', '81.jpg', '82.jpg', '83.jpg', '84.jpg', '85.jpg', '86.jpg', '87.jpg', '88.jpg', '89.jpg', '90.jpg', '91.jpg', '92.jpg', '93.jpg', '94.jpg', '95.jpg', '96.jpg', '97.jpg', '98.jpg', '99.jpg', '100.jpg']
        data1 = random.choice(lst_image)
        lst_image.remove(data1)
        data2 = random.choice(lst_image)
        
if 'hoge' not in st.session_state:
    st.session_state.hoge = 0        
        
try:        
    if 'key' not in st.session_state:
        st.session_state.key = data1
    if 'key2' not in st.session_state:
        st.session_state.key2 = data2
        
    col1, col2, col3= st.columns(3)
    
    with col1:
        container = st.container()
        st.image(st.session_state.key, use_column_width=True)
        with container:
            if st.button("左", key=2):
                with col3:
                    st.write(st.session_state.key,'>',st.session_state.key2)
                df = pd.read_csv('tomato-result.csv',encoding='cp932')
                df.at[ 1000000]  = [st.session_state.key ,st.session_state.key2 ,1 ,0] 
                csv = df.to_csv("tomato-result.csv", index=False )
                st.session_state.hoge += 1

    with col2:
        container = st.container()
        st.image(st.session_state.key2, use_column_width=True)
        with container:
            if st.button("右", key=3):
                with col3:
                    st.write(st.session_state.key,'<',st.session_state.key2)
                df = pd.read_csv('tomato-result.csv',encoding='cp932')
                df.at[ 1000000]  = [st.session_state.key2 ,st.session_state.key ,1 ,0] 
                df.to_csv("tomato-result.csv", index=False )
                st.session_state.hoge += 1
                
    if st.session_state.hoge > 0:
        del st.session_state.key
        del st.session_state.key2
        del st.session_state.hoge
                    
except NameError:
    st.subheader('↑画像更新ボタンを押してください')  
                            
st.subheader('')
st.subheader('')
st.download_button(label='結果ダウンロード', data=df.to_csv(), file_name='tomato-result_.csv')

