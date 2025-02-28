import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image
import plotly.express as px
from datetime import datetime

# Initialize session state for login and secret mode
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'secret_mode' not in st.session_state:
    st.session_state.secret_mode = False

# Configure page
st.set_page_config(
    page_title="🚀 Streamlit Interactive Learning",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------
# Secret Insights (Unlocked Content)
# ---------------------
def show_secret_insights():
    st.header("🔍 Secret Insights")
    st.info("Congratulations! You've unlocked secret insights to further deepen your learning experience.")
    
    # Allow the user to set a duration for each lesson segment (in seconds)
    lesson_duration = st.number_input("Lesson Duration (seconds)", value=600, min_value=2)
    
    # Option to auto-advance lessons or navigate manually
    auto_advance = st.checkbox("Auto Advance Lesson", value=False)
    
    # Define a list of lessons (designed to guide you through the learning process)
    lessons = [
        {
            "title": "Welcome to Learning!",
            "content": "Welcome to the interactive learning platform! Over the next hour, you'll discover advanced insights into Streamlit features, data visualization, and interactive widgets."
        },
        {
            "title": "Overview of Learning Features",
            "content": """
            **Tips:**
            - **Data Visualization:** Line, Bar, Area, and Scatter charts.
            - **Interactive Widgets:** Text input, number input, checkboxes, color picker, date input, file uploader.
            - **Layout & Media:** Tabs for charts, data, and media.
            - **Advanced Features:** Multi-select data analysis and statistical summaries.
            - **Secret Insights:** Unlock additional content and deeper learning tips.
            """
        },
        {
            "title": "Data Visualization Tips",
            "content": "Learn how different chart types (using Plotly and Matplotlib) can help you uncover patterns in your data."
        },
        {
            "title": "Interactive Widgets in Action",
            "content": "Experiment with various inputs like text, number, and checkboxes. For instance, share your favorite widget to get personalized tips."
        },
        {
            "title": "Advanced Data Analysis",
            "content": "Discover how multi-select options and statistical summaries can provide deeper insights into your datasets."
        },
        {
            "title": "Wrap-Up & Reflection",
            "content": "Reflect on what you've learned and consider revisiting any section for a deeper understanding. Keep exploring and happy learning!"
        }
    ]
    
    # Initialize lesson index if not present
    if 'current_lesson' not in st.session_state:
        st.session_state.current_lesson = 0

    # Display the current lesson
    lesson = lessons[st.session_state.current_lesson]
    st.subheader(lesson["title"])
    st.write(lesson["content"])
    
    # Add an interactive element on the "Interactive Widgets in Action" lesson
    if lesson["title"] == "Interactive Widgets in Action":
        answer = st.text_input("What is your favorite widget?")
        if answer:
            st.write(f"Great choice: {answer}!")
    
    # If auto-advance is enabled, show a countdown timer for the lesson
    if auto_advance:
        progress_bar = st.progress(0)
        for i in range(lesson_duration):
            progress_bar.progress((i + 1) / lesson_duration)
            time.sleep(1)
        st.success("Time's up for this lesson!")
    
    # Button to go to the next lesson (manual or after auto-advance)
    if st.button("Next Lesson"):
        if st.session_state.current_lesson < len(lessons) - 1:
            st.session_state.current_lesson += 1
            st.rerun()
        else:
            st.success("You've completed the secret insights!")

# ---------------------
# Cheat Sheet
# ---------------------
def show_cheatsheet():
    st.header("📚 Streamlit Full Cheat Sheet")
    
    st.markdown("""
    ## **1. Display Elements**
    - `st.title("Title Text")` → Large header text
    - `st.header("Header Text")` → Section header
    - `st.subheader("Subheader Text")` → Subsection header
    - `st.text("Simple text display")` → Displays plain text
    - `st.markdown("**Bold**, *Italic*, `Code`")` → Supports Markdown syntax
    - `st.code("print('Hello, world!')", language='python')` → Displays formatted code block
    - `st.latex("E = mc^2")` → Renders LaTeX equations
    
    ## **2. Data Display**
    - `st.dataframe(df)` → Interactive DataFrame with sorting & filtering
    - `st.table(df)` → Static table for small datasets
    - `st.metric(label, value, delta)` → Shows KPI-style metric values
    - `st.json(data)` → Displays JSON data in a formatted way
    - `st.write("Hello", 123, df)` → Generic function to display various data types
    
    ## **3. User Input Widgets**
    - `st.button("Click Me")` → Simple button
    - `st.text_input("Enter text")` → Text box
    - `st.number_input("Pick a number", min_value=0, max_value=100)` → Number selector
    - `st.text_area("Enter long text")` → Multi-line text input
    - `st.checkbox("Check me")` → Checkbox (Boolean)
    - `st.radio("Pick one", ["Option 1", "Option 2"])` → Radio button selection
    - `st.selectbox("Choose", ["A", "B", "C"])` → Dropdown single selection
    - `st.multiselect("Choose multiple", ["A", "B", "C"])` → Dropdown multi-selection
    - `st.slider("Choose a number", 0, 100)` → Slider for numerical selection
    - `st.date_input("Pick a date")` → Date picker
    - `st.time_input("Pick a time")` → Time picker
    - `st.file_uploader("Upload a file")` → File upload component
    - `st.color_picker("Pick a color")` → Color selection tool
    
    ## **4. Control Flow & State Management**
    - `st.form("my_form")` → Groups multiple input widgets
    - `st.form_submit_button("Submit")` → Submit button for forms
    - `st.experimental_rerun()` → Reruns the app
    - `st.session_state.variable_name = value` → Stores session variables
    
    ## **5. Layout & Organization**
    - `st.sidebar.header("Sidebar")` → Creates a sidebar
    - `st.sidebar.button("Sidebar Button")` → Button inside sidebar
    - `st.columns(2)` → Splits layout into columns
    - `st.expander("Expand for details")` → Collapsible section
    - `st.container()` → Grouping elements dynamically
    - `st.empty()` → Placeholder for dynamic elements
    
    ## **6. Media & Visualization**
    - `st.image("image.png")` → Displays images
    - `st.audio("audio.mp3")` → Plays audio files
    - `st.video("video.mp4")` → Embeds videos
    - `st.pyplot(fig)` → Displays Matplotlib figures
    - `st.altair_chart(chart)` → Shows Altair charts
    - `st.plotly_chart(fig)` → Displays Plotly graphs
    - `st.bokeh_chart(fig)` → Renders Bokeh visualizations
    - `st.deck_gl_chart(viewport, layers)` → 3D map visualizations
    - `st.graphviz_chart(graph_code)` → Graphviz network diagrams
    
    ## **7. Advanced & Experimental Features**
    - `st.toast("Notification message")` → Shows toast notifications
    - `st.progress(50)` → Progress bar
    - `st.spinner("Loading...")` → Displays loading spinner
    - `st.cache_data()` → Caches function results for performance
    - `st.cache_resource()` → Caches resources like models or databases
    - `st.exception(e)` → Displays error messages
    
    ## **8. Secrets & Authentication**
    - `st.secrets["API_KEY"]` → Access secret variables
    - `st.experimental_user` → Gets user information (if authentication is enabled)
    
    ## **9. Theming & Configuration**
    - `st.set_page_config(page_title="My App", layout="wide")` → Configures page layout
    - `st.get_option("theme.base")` → Retrieves theme settings
    
    ---
    
    🎯 **Use this cheat sheet as a reference for all Streamlit functionalities!**
    """)


# ---------------------
# Magic Section
# ---------------------
def show_new_features():
    st.header("🔮 Magic")
    st.write("Explore the additional functionalities recently added to enhance your learning experience!")
    
    st.subheader("Real-Time Clock")
    st.write("Current time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    st.subheader("Quick Poll")
    poll_option = st.radio("Which new feature do you like the most?",
                           ["Secret Insights", "Enhanced Widgets", "Cheat Sheet", "Real-Time Clock"])
    st.write("You selected:", poll_option)

# ---------------------
# Existing Sections
# ---------------------
def show_home():
    st.header("Welcome to Streamlit! 👋")
    st.write("This interactive platform is designed to help you learn various Streamlit features in a hands-on way.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("👈 Use the sidebar to navigate between learning modules")
    with col2:
        st.success("✨ Dive into interactive lessons and explore streamlit!")

def show_visualization():
    st.header("📊 Data Visualization")
    
    # Generate sample data
    dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
    data = pd.DataFrame({
        'Date': dates,
        'Sales': np.random.randint(100, 1000, size=30),
        'Traffic': np.random.randint(500, 2000, size=30)
    })
    
    # Interactive chart selection
    chart_type = st.selectbox(
        "Select Chart Type",
        ["Line Chart", "Bar Chart", "Area Chart", "Scatter Plot"]
    )
    
    if chart_type == "Line Chart":
        st.line_chart(data.set_index('Date'))
    elif chart_type == "Bar Chart":
        st.bar_chart(data.set_index('Date'))
    elif chart_type == "Area Chart":
        st.area_chart(data.set_index('Date'))
    elif chart_type == "Scatter Plot":
        fig = px.scatter(data, x='Sales', y='Traffic', title='Sales vs Traffic')
        st.plotly_chart(fig)

def show_widgets():
    st.header("🎮 Interactive Widgets")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Basic Inputs")
        name = st.text_input("Enter your name")
        age = st.number_input("Enter your age", 0, 120, 25)
        is_happy = st.checkbox("I am happy!")
        
        if name and age:
            st.write(f"Hello {name}! You are {age} years old.")
        if is_happy:
            st.write("😊 Glad you're feeling good!")
    
    with col2:
        st.subheader("Advanced Inputs")
        color = st.color_picker("Pick a color")
        date = st.date_input("Select a date")
        files = st.file_uploader("Upload files", accept_multiple_files=True)
        
        st.write(f"Selected color: {color}")
        st.write(f"Selected date: {date}")

def show_layout():
    st.header("📱 Layout & Media")
    
    # Tabs example
    tab1, tab2, tab3 = st.tabs(["📈 Charts", "🗃 Data", "🖼 Media"])
    
    with tab1:
        st.write("Sample chart")
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
        st.line_chart(chart_data)
    
    with tab2:
        
            col1, col2, col3 = st.columns([1, 2, 1])  # Adjust column width

            with col2:
                st.write("Sample data")
                st.dataframe(pd.DataFrame({
                    'Name': ['John', 'Anna', 'Peter'],
                    'Age': [28, 24, 32],
                    'City': ['New York', 'Paris', 'London']
                }))
    
    with tab3:
        
        col1, col2, col3 = st.columns([1, 2, 1])  # Adjust column width

        with col2:
            image = Image.open("premium_photo-1694819488591-a43907d1c5cc.jpeg")
            resized_image = image.resize((500, 600))
            st.image(resized_image, caption="A cute dog")

def show_advanced_features():
    st.header("🔧 Advanced Features")
    
    st.subheader("Interactive Data Analysis")
    data = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])
    
    selected_columns = st.multiselect(
        "Select columns to analyze",
        data.columns.tolist(),
        default=data.columns[0:2].tolist()
    )
    
    if selected_columns:
        st.line_chart(data[selected_columns])
        st.subheader("Statistical Summary")
        st.write(data[selected_columns].describe())

# ---------------------
# Main Navigation
# ---------------------
def main():
    st.title("🚀 Streamlit Interactive Learning")
    st.markdown("Welcome to this interactive platform! Learn about various Streamlit features through hands-on modules and unlock secret insights along the way.")
    
    # Sidebar navigation: add extra options for secret mode users
    st.sidebar.header("📍 Navigation")
    nav_options = ["🏠 Home", "📊 Data Visualization", "🎮 Interactive Widgets", "📱 Layout & Media", "🔧 Advanced Features"]
    
    # Display extra navigation options for secret mode
    if st.session_state.secret_mode:
        nav_options += ["🔍 Secret Insights", "📚 Cheat Sheet", "🔮 Magic"]
    
    section = st.sidebar.radio("Go to:", nav_options)
    
    # Add Logout button to the sidebar
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.secret_mode = False
        # Reset any other session states if needed
        if 'current_lesson' in st.session_state:
            del st.session_state.current_lesson
        st.rerun()
    
    if section == "🏠 Home":
        show_home()
    elif section == "📊 Data Visualization":
        show_visualization()
    elif section == "🎮 Interactive Widgets":
        show_widgets()
    elif section == "📱 Layout & Media":
        show_layout()
    elif section == "🔧 Advanced Features":
        show_advanced_features()
    elif section == "🔍 Secret Insights":
        show_secret_insights()
    elif section == "📚 Cheat Sheet":
        show_cheatsheet()
    elif section == "🔮 Magic":
        show_new_features()

# ---------------------
# Login Section
# ---------------------
if not st.session_state.logged_in:
    login_container = st.empty()
    with login_container.container():
        st.title("👤 Login")
        st.markdown("Enter your credentials to start your interactive learning journey.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            # Regular learning login
            if username == "default" and password == "default123":
                st.session_state.logged_in = True
                st.sidebar.success("Welcome, Learner!")
                st.rerun()
            # Secret mode login (unlock extra insights)
            elif username == "secret" and password == "secret123":
                st.session_state.logged_in = True
                st.session_state.secret_mode = True
                st.sidebar.success("Secrets Unlocked! Enjoy your extra insights!")
                st.rerun()
            else:
                st.sidebar.error("Invalid credentials! Please try again.")
else:
    main()