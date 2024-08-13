import streamlit as st
import pandas as pd
from scipy.stats import hmean
from scipy.stats.mstats import gmean

# Function to calculate means
def calculate_means(sets):
    df = pd.DataFrame(columns=['Values', 'Geometric Mean', 'Arithmetic Mean', 'Harmonic Mean'])
    
    for values_input in sets:
        # Split the input string by spaces or commas
        values = [float(x) for x in values_input.replace(',', ' ').split() if x.strip()]
        filtered_values = [x for x in values if x > 0]

        if len(filtered_values) > 0:
            geometric_mean = gmean(filtered_values)
            arithmetic_mean = sum(filtered_values) / len(filtered_values)
            harmonic_mean = hmean(filtered_values)
            
            new_row = pd.DataFrame({
                'Values': [str(filtered_values)],
                'Geometric Mean': [geometric_mean],
                'Arithmetic Mean': [arithmetic_mean],
                'Harmonic Mean': [harmonic_mean]
            })
            df = pd.concat([df, new_row], ignore_index=True)

    return df

# Streamlit UI
st.title("Mean Calculator")

# Input: Number of sets
num_sets = st.number_input("How many sets of values do you want to input?", min_value=1, max_value=100, value=1)

# Dynamic input for each set of values
sets = []
for i in range(num_sets):
    values_input = st.text_input(f"Enter values for set {i + 1} (separated by spaces or commas):")
    sets.append(values_input)

# Calculate means when the button is clicked
if st.button("Calculate Means"):
    df = calculate_means(sets)
    
    if not df.empty:
        st.write("Results:")
        st.dataframe(df)
    else:
        st.warning("Please enter valid numbers for all sets.")
