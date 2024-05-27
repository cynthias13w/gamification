import streamlit as st
from text import *

def main():
    # Set title of your app
    st.title("📦 Nebenan Challenge")

    # Add some text to the app
    st.write("Recommendations for each badge's criteria:")

    # Add a sidebar
    st.sidebar.title("Sidebar")

    # Add some widgets
    st.sidebar.header("Settings")
    name = st.sidebar.text_input("Enter your name", "John Doe")
    age = st.sidebar.number_input("Enter your age", min_value=0, max_value=120, value=30)
    color = st.sidebar.color_picker("Pick a color", "#00ff00")

    # Show the entered information
    st.write(f"Your name is: {name}")
    st.write(f"Your age is: {age}")
    st.write(f"Selected color: {color}")

def page_home():
    st.title("Nebenan Challenge")
    st.markdown("## My recommendations for each badge's criteria:")
    st.write(predictions)

def page_about():
    st.title("Challenge")
    st.markdown(challenge)

def page_home():
    st.title("Nebenan Challenge")
    st.markdown("## My recommendations for each badge's criteria:")
    st.write(predictions)


def page_methodology():
    st.write('xx')

def page_suggestions():
    st.write('xx')



def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["🥳 Results", "My methodology", "Challenge", "Suggestions"])

    if selection == "🥳 Results":
        page_home()
    elif selection == "Challenge":
        page_about()
    elif selection == "Methodology":
        page_methodology()
    elif selection == "Suggestions":
        page_suggestions()

if __name__ == "__main__":
    main()
