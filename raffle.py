import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np

# Predefined list of random names
participants = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack"]

def draw_spinner(participants):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.clear()
    ax.axis('equal')

    num_participants = len(participants)
    if num_participants == 0:
        st.write("No participants found.")
        return

    # Create a pie chart
    wedges, _ = ax.pie([1] * num_participants, startangle=90, counterclock=False)

    # Add labels inside the wedges
    for i, wedge in enumerate(wedges):
        ang = (wedge.theta2 - wedge.theta1) / 2 + wedge.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        ax.text(x * 0.7, y * 0.7, participants[i], horizontalalignment='center', verticalalignment='center')

    # Spin the wheel
    rotation = random.randint(0, 360)
    wedges, _ = ax.pie([1] * num_participants, startangle=rotation, counterclock=False)

    # Draw the arrow
    ax.annotate('', xy=(0, 1), xytext=(0, 0),
                arrowprops=dict(facecolor='red', shrink=0.05))

    st.pyplot(fig)

    # Determine the winner
    winner_index = (rotation // (360 // num_participants)) % num_participants
    return participants[winner_index]

st.title("Book Giveaway Raffle")

if st.button("Spin the Wheel"):
    if participants:
        winner = draw_spinner(participants)
        st.write(f"Congratulations, {winner}!")
    else:
        st.write("No participants to draw from.")