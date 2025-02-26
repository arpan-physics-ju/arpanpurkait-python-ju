# @Writter - Arpan Purkait
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.title("SciPlot : Scientific function plotting tool.")
st.subheader("Plot a Mathematical Function with us !")
function = st.text_input("Entre a function of x (e.g. sin(x)")
x_min,x_max = st.slider("Select X range:", -100.0,100.0,(-10.0,10.0))

if function:
    try:
        x = np.linspace(x_min,x_max,400)
        y = eval(function,{"__builtins__":None},{"x":x,"sin":np.sin,"cos":np.cos,"tan":np.tan,"log":np.log,"sqrt":np.sqrt,"exp":np.exp,"pi":np.pi,"e":np.e})

        fig,ax = plt.subplots()
        ax.plot(x,y,label=function)
        ax.axhline(0,color="black",linewidth=0.5)
        ax.axvline(0,color="black",linewidth=0.5)
        ax.grid(True,linestyle="--",linewidth=0.4)
        ax.legend()
        st.pyplot(fig)
    except:
        st.error("Invalid function")

st.write("**Supports:** sin, cos, tan, log, sqrt, exp, pi, e, +, -, *, /, ^")
st.write("**Developer:** Arpan Purkait")
