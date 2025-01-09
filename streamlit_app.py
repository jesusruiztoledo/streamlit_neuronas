import streamlit as st

st.image("neurona.jpg", width=300)
st.title("¡Hola neurona!")

# Opciones de la pestaña
tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

# Primera pestaña: Una entrada
with tab1:
    st.header("Una neurona con una entrada y su peso")

    # Peso w
    w = st.slider("Peso w", min_value=0.0, max_value=5.0, value=0.0, step=0.1, key="peso_w")

    # Entrada x
    x = st.number_input("Entrada x", min_value=0.0, value=0.0, step=0.1, key="entrada_x")

    # Botón para calcular la salida
    if st.button("Calcular la salida", key="boton_1"):
        # Calcular la salida de la neurona
        y = w * x
        st.write(f"La salida de la neurona es: {y:.2f}")

# Segunda pestaña: Dos entradas
with tab2:
    st.header("Dos entradas")

    # Ordenar los elementos en dos columnas
    col1, col2 = st.columns(2)

    with col1:
        # Pesos w0 y w1
        w0 = st.slider("Peso w₀", min_value=0.0, max_value=5.0, value=0.0, step=0.1, key="peso_w0")
        x0 = st.number_input("Entrada x₀", min_value=0.0, value=0.0, step=0.1, key="entrada_x0")

    with col2:
        # Entradas x0 y x1
        w1 = st.slider("Peso w₁", min_value=0.0, max_value=5.0, value=0.0, step=0.1, key="peso_w1")
        x1 = st.number_input("Entrada x₁", min_value=0.0, value=0.0, step=0.1, key="entrada_x1")

    # Botón para calcular la salida
    if st.button("Calcular la salida", key="boton_2"):
        # Calcular la salida de la neurona
        y = w0 * x0 + w1 * x1
        st.write(f"La salida de la neurona es: {y:.2f}")

# Tercera pestaña: Tres entradas y sesgo
with tab3:
    st.header("Tres entradas y sesgo")

    # Ordenar los elementos en tres columnas
    col1, col2, col3 = st.columns(3)

    with col1:
        w0 = st.slider("Peso w₀", min_value=0.0, max_value=5.0, value=0.0, step=0.1, key="peso_w0_tab3")
        x0 = st.number_input("Entrada x₀", value=0.0, step=0.1, key="entrada_x0_tab3")

    with col2:
        w1 = st.slider("Peso w₁", min_value=0.0, max_value=5.0, value=0.0, step=0.1, key="peso_w1_tab3")
        x1 = st.number_input("Entrada x₁", value=0.0, step=0.1, key="entrada_x1_tab3")
    
    with col3:
        w2 = st.slider("Peso w₂", min_value=0.0, max_value=5.0, value=0.0, step=0.1, key="peso_w2_tab3")
        x2 = st.number_input("Entrada x₂", value=0.0, step=0.1, key="entrada_x2_tab3")

    # Valor del sesgo
    b = st.number_input("Introduzca el valor del sesgo", min_value=-5.0, value=0.0, step=0.1, key="sesgo")

    # Botón para calcular la salida
    if st.button("Calcular la salida", key="boton_3"):
        # Calcular la salida de la neurona
        y = w0 * x0 + w1 * x1 + w2 * x2 + b
        st.write(f"La salida de la neurona es: {y:.2f}")

