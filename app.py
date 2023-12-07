from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

# Probabilistic functions for the Bayesian network
def bernoulli(p):
    """Return 1 with probability p, else 0."""
    return 1 if np.random.uniform() < p else 0

def probability_type2Diabetes(obesity, age_over_45, family_history, physical_inactivity, unhealthy_diet, ethnicity_risk, history_gestational_diabetes, pcos):
    """Return the probability of Type 2 Diabetes given the risk factors."""
    # Hypothetical weights based on risk factors
    weights = {
        'obesity': 0.3,
        'age_over_45': 0.15,
        'family_history': 0.25,
        'physical_inactivity': 0.2,
        'unhealthy_diet': 0.2,
        'ethnicity_risk': 0.1,
        'history_gestational_diabetes': 0.2,
        'pcos': 0.15
    }

    # Calculate cumulative probability
    probability = 0.05  # Base probability
    if obesity: probability += weights['obesity']
    if age_over_45: probability += weights['age_over_45']
    if family_history: probability += weights['family_history']
    if physical_inactivity: probability += weights['physical_inactivity']
    if unhealthy_diet: probability += weights['unhealthy_diet']
    if ethnicity_risk: probability += weights['ethnicity_risk']
    if history_gestational_diabetes: probability += weights['history_gestational_diabetes']
    if pcos: probability += weights['pcos']

    # Ensuring probability doesn't exceed 1
    return min(probability, 1.0)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form
        obesity = int(data.get('obesity', 0))
        age_over_45 = int(data.get('age_over_45', 0))
        family_history = int(data.get('family_history', 0))
        physical_inactivity = int(data.get('physical_inactivity', 0))
        unhealthy_diet = int(data.get('unhealthy_diet', 0))
        ethnicity_risk = int(data.get('ethnicity_risk', 0))
        history_gestational_diabetes = int(data.get('history_gestational_diabetes', 0))
        pcos = int(data.get('pcos', 0))

        prob_type2Diabetes = probability_type2Diabetes(obesity, age_over_45, family_history, physical_inactivity, unhealthy_diet, ethnicity_risk, history_gestational_diabetes, pcos)
        return render_template('result.html', probability=prob_type2Diabetes)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
