import streamlit as st



def greatest(a,b,c):

    return (max(a,b,c))

def main():
    
    
    st.title('Choosing the maximum of 3 numbers')
    st.text("This is a small app to input the maximum of 3 numbers. Input all your numbers below.")
   
    number1 = st.number_input('Input Number One')
    number2= st.number_input("Input Number Two")
    number3=st.number_input("Input Number Three")
    st.empty()
    st.markdown(f"The greatest number is **{greatest(number1,number2,number3)}** ")

if __name__ == "__main__":
  main()