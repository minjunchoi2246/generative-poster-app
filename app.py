# app.py
# 🎨 Generative Abstract Poster in Streamlit

import streamlit as st
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# --- Functions ---

def random_palette(k=5, seed=None):
    """Return k random pastel-like colors."""
    if seed is not None:
        random.seed(seed)
    return [(random.random(), random.random(), random.random()) for _ in range(k)]

def blob(center=(0.5, 0.5), r=0.3, points=200, wobble=0.15):
    """Generate a wobbly closed shape."""
    angles = np.linspace(0, 2*math.pi, points)
    radii = r * (1 + wobble*(np.random.rand(points)-0.5))
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

def generate_poster(seed, n_layers, wobble_min, wobble_max, radius_min, radius_max):
    """Generate the poster figure."""
    random.seed(seed)
    np.random.seed(seed)
    
    fig, ax = plt.subplots(figsize=(7, 10))
    ax.axis('off')
    ax.set_facecolor((0.98, 0.98, 0.97))

    palette = random_palette(6, seed)
    for i in range(n_layers):
        cx, cy = random.random(), random.random()
        rr = random.uniform(radius_min, radius_max)
        x, y = blob(center=(cx, cy), r=rr, wobble=random.uniform(wobble_min, wobble_max))
        color = random.choice(palette)
        alpha = random.uniform(0.25, 0.6)
        ax.fill(x, y, color=color, alpha=alpha, edgecolor=(0, 0, 0, 0))

    ax.text(0.05, 0.95, "Generative Poster", fontsize=18, weight='bold', transform=ax.transAxes)
    ax.text(0.05, 0.91, "Week 2 • Arts & Advanced Big Data", fontsize=11, transform=ax.transAxes)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return fig


# --- Streamlit App UI ---

st.title("🎨 Generative Abstract Poster")
st.write("Experiment with parameters to create unique generative art!")

# Controls
seed = st.number_input("Seed (for reproducibility)", value=0, min_value=0, max_value=9999, step=1)
n_layers = st.slider("Number of layers", 1, 20, 8)
wobble_min = st.slider("Min wobble", 0.0, 0.5, 0.05)
wobble_max = st.slider("Max wobble", 0.0, 0.5, 0.25)
radius_min = st.slider("Min radius", 0.05, 0.5, 0.15)
radius_max = st.slider("Max radius", 0.1, 0.6, 0.45)

if st.button("🎲 Generate Poster"):
    fig = generate_poster(seed, n_layers, wobble_min, wobble_max, radius_min, radius_max)
    st.pyplot(fig)
else:
    st.info("Click **Generate Poster** to create your artwork.")

