# 🦜 LangChain: Chat with SQL DB

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-f37b51?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)

An interactive conversational AI application built with Streamlit and LangChain that allows users to chat seamlessly with SQL databases using natural language. The application leverages the powerful `llama-3.3-70b-versatile` LLM model via the **Groq API** to translate plain English questions into accurate SQL queries, execute them, and return conversational answers.

## ✨ Features

- **Natural Language to SQL**: Ask questions in plain English and get answers directly from your database.
- **Support for Multiple Databases**:
  - Out-of-the-box support for a local **SQLite** database (`student.db`).
  - Seamless connection to remote **MySQL** databases.
- **Conversational Memory**: The agent remembers the context of the conversation during your session.
- **High-Performance LLM**: Uses ChatGroq (`llama-3.3-70b-versatile`) for extremely fast and accurate query generation.
- **Zero-Shot ReAct Agent**: Intelligently reasons about the database schema and structure before querying.
- **Real-time Streaming**: Watch the agent's thought process and final answer stream in real-time.



### Prerequisites

Ensure you have Python 3.8+ installed. You will also need a **Groq API Key**. You can get one for free at [console.groq.com](https://console.groq.com/).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RohanJha2410/SQL-Chatbot.git
   cd "SQL-Chatbot"
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Rebuild the local SQLite database:**
   The repository comes with a pre-populated `student.db`. If you want to recreate it or see how it's built, run:
   ```bash
   python sqlite.py
   ```

### Running the Application

Launch the Streamlit app by running the following command in your terminal:

```bash
streamlit run app.py
```

## 💡 How to Use

1. Open the application in your browser (usually `http://localhost:8501`).
2. **Sidebar Configuration**:
   - Enter your **GROQ API Key**.
   - Choose your target database:
     - **SQLite 3 Database (Student.db)**: Uses the local dummy database included in the project.
     - **Connect to your SQL database**: Prompts you to enter your MySQL Host, User, Password, and Database Name.
3. **Chat Area**:
   - Once configured, use the chat input at the bottom to ask questions.
   - Example questions for the local Student DB:
     - *"How many students are in the Data Science class?"*
     - *"Who scored the highest marks and what section are they in?"*
     - *"List all students in the DEVOPS class."*

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) - The web framework used for the UI.
- [LangChain](https://python.langchain.com/) - Framework for developing applications powered by language models.
- [ChatGroq](https://groq.com/) - High-speed LLM inference.
- [SQLAlchemy](https://www.sqlalchemy.org/) - Database toolkit and Object Relational Mapper for Python.

## 📁 Project Structure

- `app.py`: The main Streamlit application script containing the UI and LangChain agent logic.
- `sqlite.py`: A utility script to initialize and populate the local `student.db` SQLite database.
- `student.db`: The local SQLite database containing dummy student records.
- `requirements.txt`: List of Python dependencies required to run the project.

## 📝 License

This project is licensed under the MIT License.
