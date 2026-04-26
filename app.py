import streamlit as st
import random

# 🎨 DARK THEME
st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
}
h1, h2, h3, h4, h5, h6, p, div {
    color: #ffffff;
}
.stButton>button {
    background-color: #1f77b4;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 0.5em 1em;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #3399ff;
    box-shadow: 0px 0px 10px #3399ff;
}
</style>
""", unsafe_allow_html=True)

# 🏟️ PAGE CONFIG
st.set_page_config(page_title="Find My Peep", layout="centered")

st.title("🧑‍🤝‍🧑 Find My Peep")
st.subheader("Real-time Crowd-Aware Navigation System")
st.caption("🚀 AI-powered crowd-aware navigation system")

st.success("🟢 System Active: Tracking users & analyzing crowd")

# 🎲 INITIAL POSITIONS
if "user" not in st.session_state:
    st.session_state.user = {"x": random.randint(10, 90), "y": random.randint(10, 90)}
    st.session_state.friend = {"x": random.randint(10, 90), "y": random.randint(10, 90)}

user = st.session_state.user
friend = st.session_state.friend

# 📍 LOCATIONS
st.subheader("📍 Locations")
st.write(f"👦 Srinath: ({user['x']}, {user['y']})")
st.write(f"👧 Bunny: ({friend['x']}, {friend['y']})")

# 📏 DISTANCE
distance = abs(user["x"] - friend["x"]) + abs(user["y"] - friend["y"])
st.write(f"📏 Distance between you: {distance} units")

if distance < 20:
    st.success("🎉 You are very close! No need for a meeting point.")

# 🔘 BUTTONS
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🔍 Find Friend"):
        st.success("Path calculated! Move towards your friend.")

with col2:
    if st.button("✨ Suggest Meeting Point"):
        meet_x = (user["x"] + friend["x"]) // 2
        meet_y = (user["y"] + friend["y"]) // 2

        st.session_state.meet = {"x": meet_x, "y": meet_y}

        st.success(f"📍 Best Meeting Point: ({meet_x}, {meet_y})")
        st.info("💡 Move towards the meeting point to avoid congestion and reduce walking time.")

with col3:
    if st.button("🏃 Move Users"):
        st.session_state.user["x"] += random.randint(-5, 5)
        st.session_state.user["y"] += random.randint(-5, 5)
        st.session_state.friend["x"] += random.randint(-5, 5)
        st.session_state.friend["y"] += random.randint(-5, 5)
        st.rerun()

with col4:
    if st.button("🔄 Reset"):
        st.session_state.user = {"x": random.randint(10, 90), "y": random.randint(10, 90)}
        st.session_state.friend = {"x": random.randint(10, 90), "y": random.randint(10, 90)}
        if "meet" in st.session_state:
            del st.session_state.meet
        st.rerun()

# 🗺️ MAP
st.subheader("🗺️ Stadium Map (Demo)")

map_grid = [["⬜" for _ in range(10)] for _ in range(10)]

# 🚧 Crowded zones
crowded_zone = [(4,4), (4,5), (5,4), (5,5)]
for (cx, cy) in crowded_zone:
    map_grid[cy][cx] = "🚧"

# Positions
ux, uy = user["x"] // 10, user["y"] // 10
fx, fy = friend["x"] // 10, friend["y"] // 10

map_grid[uy][ux] = "👦"
map_grid[fy][fx] = "👧"

# 🤝 Meeting point
if "meet" in st.session_state:
    meet = st.session_state.meet
    mx = meet["x"] // 10
    my = meet["y"] // 10

    if (mx, my) in crowded_zone:
        mx, my = 3, 3

    if 0 <= my < 10 and 0 <= mx < 10:
        map_grid[my][mx] = "🤝"

# Display map
for row in map_grid:
    st.markdown(f"<div style='font-size:26px'>{' '.join(row)}</div>", unsafe_allow_html=True)

# 🧭 LEGEND
st.markdown("### 🧭 Legend")
st.write("👦 You | 👧 Friend | 🚧 Crowded Area | 🤝 Meeting Point")