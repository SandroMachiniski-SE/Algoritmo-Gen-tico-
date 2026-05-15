import random
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Definição dos itens
ITEMS = [
    {"name": "Saco de dormir", "weight": 15, "score": 15},
    {"name": "Corda", "weight": 3, "score": 7},
    {"name": "Canivete", "weight": 2, "score": 10},
    {"name": "Tocha", "weight": 5, "score": 5},
    {"name": "Garrafa", "weight": 9, "score": 8},
    {"name": "Comida", "weight": 20, "score": 17}
]

MAX_WEIGHT = 30

class Individual:
    def __init__(self, chromosome=None):
        if chromosome is None:
            self.chromosome = [random.randint(0, 1) for _ in range(len(ITEMS))]
        else:
            self.chromosome = list(chromosome)
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        total_weight = sum(ITEMS[i]["weight"] * self.chromosome[i] for i in range(len(ITEMS)))
        total_score = sum(ITEMS[i]["score"] * self.chromosome[i] for i in range(len(ITEMS)))

        # Penalizar se exceder o peso máximo
        if total_weight > MAX_WEIGHT:
            return 0

        return total_score

    def get_details(self):
        total_weight = sum(ITEMS[i]["weight"] * self.chromosome[i] for i in range(len(ITEMS)))
        total_score = sum(ITEMS[i]["score"] * self.chromosome[i] for i in range(len(ITEMS)))
        selected_items = [ITEMS[i]["name"] for i in range(len(ITEMS)) if self.chromosome[i] == 1]

        return {
            "chromosome": self.chromosome,
            "weight": total_weight,
            "score": total_score,
            "items": selected_items,
            "fitness": self.fitness
        }

class GeneticAlgorithm:
    def __init__(self, population_size=50, generations=100, mutation_rate=0.1):
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.best_fitness_history = []
        self.avg_fitness_history = []
        self.population = [Individual() for _ in range(population_size)]

    def selection(self):
        # Seleção por torneio
        tournament_size = min(5, len(self.population))
        selected = []
        for _ in range(self.population_size):
            tournament = random.sample(self.population, tournament_size)
            winner = max(tournament, key=lambda x: x.fitness)
            selected.append(winner)
        return selected

    def crossover(self, parent1, parent2):
        if len(ITEMS) > 1:
            point = random.randint(1, len(ITEMS) - 1)
        else:
            point = 1
        child_chromosome = parent1.chromosome[:point] + parent2.chromosome[point:]
        return Individual(child_chromosome)

    def mutate(self, individual):
        for i in range(len(individual.chromosome)):
            if random.random() < self.mutation_rate:
                individual.chromosome[i] = 1 - individual.chromosome[i]
        individual.fitness = individual.calculate_fitness()

    def evolve(self):
        for generation in range(self.generations):
            # Seleção
            selected = self.selection()

            # Crossover e mutação
            new_population = []
            for _ in range(self.population_size):
                parent1, parent2 = random.sample(selected, 2)
                child = self.crossover(parent1, parent2)
                self.mutate(child)
                new_population.append(child)

            # Elitismo: manter o melhor indivíduo
            best = max(self.population, key=lambda x: x.fitness)
            new_population[0] = Individual(best.chromosome)

            self.population = new_population

            # Registrar histórico
            fitness_values = [ind.fitness for ind in self.population]
            self.best_fitness_history.append(max(fitness_values))
            self.avg_fitness_history.append(sum(fitness_values) / len(fitness_values))

        return self.get_best_solution()

    def get_best_solution(self):
        best = max(self.population, key=lambda x: x.fitness)
        return best.get_details()

@app.route('/api/items', methods=['GET'])
def get_items():
    try:
        return jsonify(ITEMS)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/solve', methods=['POST'])
def solve():
    try:
        data = request.json
        population_size = int(data.get('population_size', 50))
        generations = int(data.get('generations', 100))
        mutation_rate = float(data.get('mutation_rate', 0.1))

        # Validar parâmetros
        if population_size < 10:
            population_size = 10
        if generations < 10:
            generations = 10
        if mutation_rate < 0.01:
            mutation_rate = 0.01
        if mutation_rate > 0.5:
            mutation_rate = 0.5

        ga = GeneticAlgorithm(population_size, generations, mutation_rate)
        best_solution = ga.evolve()

        return jsonify({
            "best_solution": best_solution,
            "best_fitness_history": ga.best_fitness_history,
            "avg_fitness_history": ga.avg_fitness_history
        })
    except Exception as e:
        print(f"Erro no servidor: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    print("🚀 Servidor rodando em http://localhost:5000")
    print("📡 CORS habilitado para localhost")
    app.run(debug=True, port=5000, host='0.0.0.0')