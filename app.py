import streamlit as st

st.title('Data Dashboard')
st.write('Week 9: Interactive Dashboard')

import csv
values = []
with open('student.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        values.append(float(row[2]))

if st.button('Load Data'):
    st.write(values)

if st.button('Show Chart'):
    st.bar_chart(values)

threshold = st.slider('Select threshold', 0, 100)
count = 0

for v in values:
    if v > threshold:
        count += 1

st.write('Values above threshold:', count)

if st.button('Analyse Data'):
    total = 0

    for v in values:
       total += v
    
    average = total / len(values)
    
    st.write('Average:', average)
    st.bar_chart(values)
