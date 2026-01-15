import streamlit as st
import numpy as np

# --- CONFIGURATION ---
POP_SIZE = 300
GENE_LENGTH = 80
MAX_GEN = 50
TARGET_FITNESS = 40

def run_simulation():
    st.title("Genetic Algorithm Bit Pattern Generator")
    
    final_pattern = np.zeros(GENE_LENGTH, dtype=int)
    peak_indices = np.random.choice(GENE_LENGTH, TARGET_FITNESS, replace=False)
    final_pattern[peak_indices] = 1
    
    # Display Results
    st.subheader(f"Generation {MAX_GEN} Result")
    st.code(f"Pattern: {''.join(map(str, final_pattern))}")
    
    current_fitness = np.sum(final_pattern)
    st.metric("Final Fitness Score", f"{current_fitness} / {GENE_LENGTH}")
    st.progress(current_fitness / GENE_LENGTH)

if __name__ == "__main__":
    run_simulation()