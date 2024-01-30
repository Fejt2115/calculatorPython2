import streamlit as st
import pandas as pd

def main():
    st.title("Porównywarka cen")

    # Prześlij plik Excel
    df = pd.read_excel(
        io="calc.xlsx",
        engine="openpyxl",
        sheet_name="Kalkulator"
    )


    # Wybierz komórkę do wstawienia wartości
    st.header("Wstawianie wartości do komórki")
    cell_value = st.text_input("Wartość do wstawienia:", "")
    if st.button("Wstaw"):
        insert_value(df, cell_value)

    # Wybierz komórkę z formułą
    st.header("Obliczanie formuły")
    formula_cell = st.text_input("Komórka z formułą (np. A1):", "")
    if st.button("Oblicz"):
        result = calculate_formula(df, formula_cell)
        st.success(f"Wynik obliczeń: {result}")

def read_excel_file(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file, engine='openpyxl')
        return df
    except Exception as e:
        st.error(f"Błąd przy odczycie pliku Excel: {e}")
        return None

def insert_value(df, cell_value):
    try:
        df.iloc[0, 0] = cell_value
        st.success(f"Wartość {cell_value} została wstawiona do komórki A1.")
    except Exception as e:
        st.error(f"Błąd przy wstawianiu wartości: {e}")

def calculate_formula(df, formula_cell):
    try:
        result = df[formula_cell].values[0]
        return result
    except Exception as e:
        st.error(f"Błąd przy obliczaniu formuły: {e}")
        return None

if __name__ == "__main__":
    main()