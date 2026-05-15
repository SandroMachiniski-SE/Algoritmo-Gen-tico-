# Algoritmo-Gen-tico-
Aplicação com frontend e algoritmo genético para resolver o problema clássico da mochila (Knapsack Problem).

# Knapsack Problem - Algoritmo Genético

## 📋 Descrição

Aplicação completa que implementa um Algoritmo Genético para resolver o problema clássico da Mochila (Knapsack Problem). O projeto inclui um backend em Python com Flask e um frontend interativo em HTML/CSS/JavaScript.

## 🎯 Objetivo

Encontrar a melhor combinação de itens para carregar em uma mochila com capacidade máxima de 30 kg, maximizando a pontuação de sobrevivência sem exceder o limite de peso.

## 🏗️ Estrutura do Projeto

knapsack-ga/ ├── backend/ │ └── app.py # Servidor Flask com algoritmo genético ├── frontend/ │ └── index.html # Interface web completa ├── README.md # Este arquivo └── requirements.txt # Dependências Python

## 🚀 Como Executar

### Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone ou extraia o projeto**

2. **Instale as dependências**

pip install -r requirements.txt

### Executar o Backend

python backend/app.py


O servidor estará rodando em `http://localhost:5000`

### Executar o Frontend

Abra o arquivo `frontend/index.html` no seu navegador ou sirva-o com um servidor web:

# Usando Python 3
python -m http.server 8000 --directory frontend

Acesse `http://localhost:8000` no navegador.

## 🧬 Funcionamento do Algoritmo Genético

### 1. **Representação Genética**
- Cada solução é um cromossomo binário de 6 bits
- Exemplo: `101010` representa [Saco, Corda, Canivete, Tocha, Garrafa, Comida]
- `1` = item incluído, `0` = item não incluído

### 2. **População Inicial**
- Gerada aleatoriamente com indivíduos binários
- Tamanho configurável (padrão: 50)

### 3. **Função de Fitness**
- Maximiza a pontuação de sobrevivência
- Penaliza (retorna 0) soluções que excedem 30 kg
- Fórmula: `fitness = score_total se peso_total <= 30 kg, senão 0`

### 4. **Seleção**
- Implementa seleção por torneio
- Seleciona os melhores indivíduos para reprodução

### 5. **Crossover**
- Ponto de corte aleatório
- Combina material genético de dois pais

### 6. **Mutação**
- Inverte bits aleatoriamente
- Taxa configurável (padrão: 10%)

### 7. **Elitismo**
- Preserva o melhor indivíduo da geração anterior
- Garante que a melhor solução não seja perdida

### 8. **Evolução**
- Executa por número configurável de gerações
- Registra histórico de fitness para visualização

## 📊 Interface do Usuário

### Painel de Itens
- Lista todos os 6 itens disponíveis
- Exibe peso e pontuação de cada item

### Configurações
- **Tamanho da População**: Quantidade de indivíduos (10-500)
- **Número de Gerações**: Iterações do algoritmo (10-1000)
- **Taxa de Mutação**: Probabilidade de mudança (0.01-0.5)

### Resultados
- **Cromossomo**: Representação binária da solução
- **Peso Total**: Peso dos itens selecionados
- **Pontuação Total**: Pontos de sobrevivência
- **Itens Selecionados**: Lista visual dos itens escolhidos
- **Gráfico de Evolução**: Mostra melhor fitness e fitness médio por geração

## 📦 Itens Disponíveis

| Item | Peso (kg) | Pontuação |
|------|-----------|-----------|
| Saco de dormir | 15 | 15 |
| Corda | 3 | 7 |
| Canivete | 2 | 10 |
| Tocha | 5 | 5 |
| Garrafa | 9 | 8 |
| Comida | 20 | 17 |

## 🔧 Dependências
Flask==2.3.0 Flask-CORS==4.0.0

Instale com:
pip install -r requirements.txt

## 💡 Exemplos de Uso

### Configuração Rápida
- População: 50
- Gerações: 100
- Taxa de Mutação: 0.1

### Configuração Agressiva
- População: 200
- Gerações: 500
- Taxa de Mutação: 0.15

Maiores valores podem encontrar soluções melhores, mas levam mais tempo.

## 📈 Interpretando os Resultados

- **Cromossomo**: Leia da esquerda para direita (posição 0 = Saco de dormir, etc.)
- **Gráfico**: A linha verde (melhor) deve convergir para um valor estável
- **Fitness**: Quanto maior, melhor (máximo teórico é 57 pontos)

## 🎓 Conceitos Implementados

✅ Representação genética binária  
✅ População inicial aleatória  
✅ Cálculo de fitness com penalização  
✅ Seleção por torneio  
✅ Crossover de ponto único  
✅ Mutação por inversão de bits  
✅ Elitismo  
✅ Evolução por gerações  
✅ Visualização de resultados  
✅ Interface web interativa  

## 📝 Notas

- O algoritmo é não-determinístico, resultados podem variar entre execuções
- Aumentar gerações geralmente melhora a solução
- A população deve ser pelo menos 10 para bom funcionamento
- Taxa de mutação muito alta pode prejudicar convergência

## 👨‍💻 Autor

Desenvolvido como atividade de Algoritmos Genéticos

---

**Boa sorte na sobrevivência! 🏕️**

pip install -r requirements.txt

Flask==2.3.0
Flask-CORS==4.0.0

