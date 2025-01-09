
# ¡Hola Neurona!

Esta es una aplicación interactiva creada con Streamlit que permite explorar el funcionamiento básico de una neurona artificial. Podrás experimentar con diferentes entradas, pesos y sesgos para calcular la salida de la neurona.

## Funcionalidades

La aplicación está organizada en tres pestañas que representan diferentes configuraciones de una neurona:

### 1. Una entrada
- Configura un único peso (`w`) y una entrada (`x`).
- Calcula la salida de la neurona como \( y = w \cdot x \).

### 2. Dos entradas
- Configura dos pesos (`w₀`, `w₁`) y dos entradas (`x₀`, `x₁`).
- Calcula la salida de la neurona como \( y = w₀ \cdot x₀ + w₁ \cdot x₁ \).

### 3. Tres entradas y sesgo
- Configura tres pesos (`w₀`, `w₁`, `w₂`), tres entradas (`x₀`, `x₁`, `x₂`) y un sesgo (`b`).
- Calcula la salida de la neurona como \( y = w₀ \cdot x₀ + w₁ \cdot x₁ + w₂ \cdot x₂ + b \).

## Requisitos

- Python 3.7 o superior.
- Streamlit 1.0 o superior.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd tu-repositorio
   ```
3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
4. Asegúrate de que la imagen `neurona.jpg` se encuentre en el directorio `images/`.

## Ejecución

1. Ejecuta la aplicación con el siguiente comando:
   ```bash
   streamlit run app.py
   ```
2. Abre el enlace generado en tu navegador para interactuar con la aplicación.

## Personalización

Puedes personalizar los valores predeterminados y los rangos de los sliders o inputs editando los parámetros en el archivo `app.py`. Por ejemplo:

- Cambiar el rango de un slider:
  ```python
  w = st.slider("Peso w", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
  ```

- Modificar el sesgo:
  ```python
  b = st.number_input("Introduzca el valor del sesgo", min_value=-10.0, max_value=10.0, step=0.1, value=0.0)
  ```
