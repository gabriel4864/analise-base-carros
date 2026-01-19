# Importando a biblioteca pandas para realização do tratamento do dataset
import pandas as pd

# Lendo a base de dados
df = pd.read_excel("car_base.xlsx")

# Excluindo colunas não necessárias 
df = df.drop(["Engine_Size", "Mileage", "Doors", "Owner_Count" ], axis= 1)

# Armazenando o valor do dolar para calculos com valores do dataset
valor_dolar = 5

# Padronizando os títulos das colunas
df.columns = (
    df.columns
      .str.strip()
      .str.capitalize()
      .str.replace("_", " ")
)

# Arrumando os tipos das colunas
df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Convertendo valores dos carros de dolar para real
df["Price"] = df["Price"] * valor_dolar
# Colocando a coluna de preço em padrão de milhar
df["Price"] = df["Price"].map(lambda x: f"{x:,.0f}".replace(",", "."))

# Salvando base atualizada
df.to_excel("car_base_tratada.xlsx", index=False)

