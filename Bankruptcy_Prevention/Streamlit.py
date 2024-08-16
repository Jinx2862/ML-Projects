#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Sized
import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)


def predict_bankruptcy(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk):
     prediction=classifier.predict([[industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk]])
     print(prediction)
     return prediction





def main():
    
    st.title("BANKRUPTCY DETECTOR")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:black;text-align:center;">This is a Website which Predicts whether the Company is Bankrupt or Not. </h2>
    </div>
    """
    

    st.markdown(html_temp,unsafe_allow_html=True)
    
    
    industrial_risk = st.number_input(label="Industrial_Risk",format="%.1f")
    management_risk = st.number_input(label="Management_Risk",format="%.1f")
    financial_flexibility = st.number_input(label="Financial_Flexibility",format="%.1f")
    credibility = st.number_input(label="Credibility",format="%.1f")
    competitiveness = st.number_input(label="Competitiveness",format="%.1f")
    operating_risk = st.number_input(label="Operating_Risk",format="%.1f")
    result=""
    if st.button("Predict"):
        result=predict_bankruptcy(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk)
    result1=''
    if(result==0):
        result1='Bankrupt'
    elif(result==1):
        result1='Non Bankrupt'
    
    st.success('The output is {}'.format(result1))

if __name__=='__main__':
    main()
