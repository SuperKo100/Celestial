import streamlit as st
import graphviz

if "login" not in st.session_state:
	st.session_state.login = False
if "username" not in st.session_state:
	st.session_state.username = ""
if "password" not in st.session_state:
	st.session_state.password = ""
if "team" not in st.session_state:
	st.session_state.team = ""

def appLogin():
	username = st.text_input("Username")
	password = st.text_input("Password")

def appRisk():
	with st.sidebar:
		st.write("risk tool1")
		st.write("risk tool2")
		st.write("risk tool3")

def appCompliance():
	with st.sidebar:
		st.write("compliance tool1")
		st.write("compliance tool2")

def main():
	with st.sidebar:
		st.write(f"Login: {st.session_state.login}")
		st.write(f"Username: {st.session_state.username}")
		st.write(f"Password: {st.session_state.password}")
		st.write(f" Team: {st.session_state.team}")
		st.divider()
		st.write("general tool1")
		st.write("general tool2")
		st.divider()
	appLogin()
	
	# Create a graphlib graph object
	graph = graphviz.Digraph()
	graph.edge("run", "intr")
	graph.edge("intr", "runbl")
	graph.edge("runbl", "run")
	graph.edge("run", "kernel")
	graph.edge("kernel", "zombie")
	graph.edge("kernel", "sleep")
	graph.edge("kernel", "runmem")
	graph.edge("sleep", "swap")
	graph.edge("swap", "runswap")
	graph.edge("runswap", "new")
	graph.edge("runswap", "runmem")
	graph.edge("new", "runmem")
	graph.edge("sleep", "runmem")

	st.graphviz_chart(graph)



if __name__ == "__main__":
	main()
