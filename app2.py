# app.py
# 🎨 Generative Abstract Poster — Streamlit Version

import streamlit as st
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Functions
# -----------------------------

def random_palette(k=5):
    """Return k random pastel-like colors."""
    return [(random.random(), random.random(), random.random()) for _ in range(k)]

def blob(center=(0.5, 0.5), r=1.0, points=200, wobble=0.05):
    """Generate a wobbly closed shape."""
    angles = np.linspace(0, 2*math.pi, points)
    radii = r * (1 + wobble*(np.random.rand(points)-0.5))
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

def generate_poster(n_layers=100, palette_size=100, wobble=100, seed=None):
    """Generate the generative poster figure."""
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

    fig, ax = plt.subplots(figsize=(7, 10))
    ax.axis('off')
    ax.set_facecolor((0.98, 0.98, 0.97))

    palette = random_palette(palette_size)
    for i in range(n_layers):
        cx, cy = random.random(), random.random()
        rr = random.uniform(0.15, 0.45)
        x, y = blob(center=(cx, cy), r=rr, wobble=random.uniform(wobble, wobble))
        color = random.choice(palette)
        alpha = random.uniform(0.25, 0.6)
        ax.fill(x, y, color=color, alpha=alpha, edgecolor=(0,0,0,0))

    ax.text(0.05, 0.95, "Generative Poster", fontsize=18, weight='bold', transform=ax.transAxes)
    ax.text(0.05, 0.91, "Week 3 • Arts & Advanced Big Data", fontsize=11, transform=ax.transAxes)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return fig

# -----------------------------
# Streamlit UI
# -----------------------------

st.title("🎨 Generative Abstract Poster")
st.caption("Week 3 • Arts & Advanced Big Data")

# Sidebar Controls
st.sidebar.header("Poster Parameters")
n_layers = st.sidebar.slider("Number of layers", 10, 200, 100)
palette_size = st.sidebar.slider("Palette size", 5, 150, 100)
wobble = st.sidebar.slider("Wobble intensity", 0.0, 200.0, 100.0)
seed = st.sidebar.number_input("Random seed (optional)", value=0, min_value=0, step=1)

# Generate Poster
if st.button("🎲 Generate Poster"):
    fig = generate_poster(n_layers=n_layers, palette_size=palette_size, wobble=wobble, seed=seed)
    st.pyplot(fig)

    # Save button
    import io
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=300)
    st.download_button(
        label="💾 Download Poster as PNG",
        data=buf.getvalue(),
        file_name="poster1.png",
        mime="image/png"
    )
else:
    st.info("Adjust parameters and click **Generate Poster** to create your art.")

