import pandas as pd
import numpy as np

# Criando dados aleatórios para simular exames de 1000 pacientes
np.random.seed(42)
num_pacientes = 1000

dados = {
    "id": np.arange(1, num_pacientes + 1),
    "idade": np.random.randint(18, 80, num_pacientes),
    "imc": np.random.uniform(18, 35, num_pacientes),
    "glicose": np.random.randint(70, 200, num_pacientes),
    "colesterol": np.random.randint(150, 300, num_pacientes),
    "pressao": np.random.randint(60, 140, num_pacientes),
    "condicao_medica": np.random.choice([0, 1], num_pacientes, p=[0.7, 0.3])  # 30% dos pacientes têm a condição
}

# Criando um DataFrame e salvando como CSV
df = pd.DataFrame(dados)
df.to_csv("dados_pacientes.csv", index=False)

print("Arquivo CSV criado com sucesso! 🎯")