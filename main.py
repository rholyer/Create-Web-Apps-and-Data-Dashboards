import streamlit as st

data = {
  'Series_1':[1,3,4,5,7],
  'Series_2':[10,30,40,100,250],
}

df = pandas.DataFrame(data)

st.title('Streamlit App')
st.subheader('Introducing Streamlit in Automate Everything with Python')
st.write('''Look at you go! \n
Coding like a pro!
{{{df}}}
''')
st.write(df)