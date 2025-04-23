import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.spatial import ConvexHull
from itertools import combinations

st.title("Linear Programming with Graphical Solution")

# Sidebar inputs
st.sidebar.header("Objective Function")
objective = st.sidebar.radio("Optimization Direction", ["Maximize", "Minimize"])
c_x = st.sidebar.number_input("Coefficient of x", value=3.0)
c_y = st.sidebar.number_input("Coefficient of y", value=5.0)

st.sidebar.header("Constraints")
constraints = []
num_constraints = st.sidebar.number_input("Number of Constraints", 1, 5, 2)

for i in range(num_constraints):
    st.sidebar.subheader(f"Constraint {i+1}")
    a = st.sidebar.number_input(f"x coefficient {i+1}", value=2.0 if i==0 else 1.0)
    b = st.sidebar.number_input(f"y coefficient {i+1}", value=1.0 if i==0 else 2.0)
    sign = st.sidebar.selectbox(f"Inequality {i+1}", ["<=", ">=", "="], key=f"sign{i}")
    c = st.sidebar.number_input(f"RHS {i+1}", value=100.0 if i==0 else 80.0)
    constraints.append({'a': a, 'b': b, 'sign': sign, 'c': c})

non_negative = st.sidebar.checkbox("Include non-negativity constraints", True)
if non_negative:
    constraints.extend([{'a': 1, 'b': 0, 'sign': '>=', 'c': 0},
                        {'a': 0, 'b': 1, 'sign': '>=', 'c': 0}])

if st.sidebar.button("Solve"):
    vertices = []
    for con1, con2 in combinations(constraints, 2):
        a1, b1, c1 = con1['a'], con1['b'], con1['c']
        a2, b2, c2 = con2['a'], con2['b'], con2['c']
        det = a1*b2 - a2*b1
        if det == 0: continue
        
        x = (c1*b2 - c2*b1) / det
        y = (a1*c2 - a2*c1) / det
        
        valid = True
        for con in constraints:
            a, b, s, c = con['a'], con['b'], con['sign'], con['c']
            lhs = a*x + b*y
            if (s == '<=' and lhs > c + 1e-6) or (s == '>=' and lhs < c - 1e-6) or (s == '=' and abs(lhs - c) > 1e-6):
                valid = False
                break
        if valid:
            vertices.append((x, y))
    
    if not vertices:
        st.error("No feasible solution")
    else:
        points = np.array(vertices)
        hull = ConvexHull(points)
        polygon = points[hull.vertices]
        polygon = np.vstack([polygon, polygon[0]])
        
        x_min, x_max = np.min(polygon[:,0])-1, np.max(polygon[:,0])+1
        y_min, y_max = np.min(polygon[:,1])-1, np.max(polygon[:,1])+1
        
        best_val = None
        best_point = None
        for x, y in vertices:
            z = c_x*x + c_y*y
            if (objective == "Maximize" and (best_val is None or z > best_val)) or \
               (objective == "Minimize" and (best_val is None or z < best_val)):
                best_val = z
                best_point = (x, y)
        
        # Plotting
        fig = go.Figure()
        
        # Feasible region
        fig.add_trace(go.Scatter(x=polygon[:,0], y=polygon[:,1], 
                                fill="toself", fillcolor="rgba(0,255,0,0.2)",
                                line=dict(color="green"), name="Feasible Region"))
        
        # Constraints
        x_vals = np.linspace(x_min, x_max, 200)
        for con in constraints:
            a, b, s, c = con['a'], con['b'], con['sign'], con['c']
            if b == 0:
                if a != 0:
                    x_const = c/a
                    fig.add_trace(go.Scatter(x=[x_const, x_const], y=[y_min, y_max], 
                                            line=dict(dash="dash"), name=f"{a}x {s} {c}"))
            else:
                y_vals = (c - a*x_vals)/b
                valid = (y_vals >= y_min) & (y_vals <= y_max)
                fig.add_trace(go.Scatter(x=x_vals[valid], y=y_vals[valid], 
                                        line=dict(dash="dash"), name=f"{a}x + {b}y {s} {c}"))
        
        # Vertices
        fig.add_trace(go.Scatter(x=[v[0] for v in vertices], y=[v[1] for v in vertices],
                                mode="markers", name="Vertices", marker=dict(color="red")))
        
        # Optimal solution
        if best_point:
            fig.add_trace(go.Scatter(x=[best_point[0]], y=[best_point[1]],
                                    mode="markers", name="Optimal Solution",
                                    marker=dict(color="blue", size=12)))
        
        fig.update_layout(title="Linear Programming Solution",
                         xaxis=dict(range=[x_min, x_max]), 
                         yaxis=dict(range=[y_min, y_max]),
                         xaxis_title="x", yaxis_title="y")
        
        st.plotly_chart(fig)
        st.write(f"Optimal Value (Z) = {best_val:.2f} at (x, y) = ({best_point[0]:.2f}, {best_point[1]:.2f})")
