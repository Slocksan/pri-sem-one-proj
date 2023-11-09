import streamlit as st
import pandas as pd
import numpy as np

st.title('Сложнейшие задание')

df = pd.read_csv("data.csv", delimiter=',')

sex = st.radio(label="Пол пассажиров", options=["Женщины", "Мужчины"])

st.write("Доля выживших пассажиров")

countOfSurvivedWoman = df[(df.Sex == "female") & (df.Survived == 1)].shape[0]
countOfSurvivedMan = df[(df.Sex == "male") & (df.Survived == 1)].shape[0]

if (sex == "Женщины"):
    survivedWomanRatio = round(countOfSurvivedWoman / (countOfSurvivedWoman + countOfSurvivedMan) * 100, 2)
    st.write(f"{survivedWomanRatio} %")
else:
    survivedManRatio = round(countOfSurvivedMan / (countOfSurvivedWoman + countOfSurvivedMan) * 100, 3)
    st.write(f"{survivedManRatio} %")