import streamlit as st
import pandas as pd

st.set_page_config(page_title="SDG Progress Dashboard", layout="centered")

# Dummy data for a few SDGs
data = {
    "Goal": [
        "No Poverty",
        "Zero Hunger",
        "Good Health & Well-being",
        "Quality Education",
        "Climate Action",
    ],
    "Progress (%)": [65, 50, 72, 80, 40],
    "Description": [
        "End poverty in all its forms everywhere.",
        "End hunger, achieve food security and improved nutrition.",
        "Ensure healthy lives and promote well-being for all.",
        "Ensure inclusive and equitable quality education.",
        "Take urgent action to combat climate change and its impacts.",
    ],
}

df = pd.DataFrame(data)

st.title("🌍 SDG Progress Dashboard")
st.markdown("A simple dashboard to visualize Sustainable Development Goals progress.")

# Dropdown to select goal
selected_goal = st.selectbox("Select an SDG Goal:", df["Goal"])

# Show details
goal_info = df[df["Goal"] == selected_goal].iloc[0]
st.subheader(f"📌 {goal_info['Goal']}")
st.write(goal_info["Description"])

progress = int(goal_info["Progress (%)"])
st.progress(progress / 100)

st.write(f"✅ Current progress: **{progress}%**")

# Show all goals in table
st.subheader("Overview of All Goals")
st.dataframe(df)
