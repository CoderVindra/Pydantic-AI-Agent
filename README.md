# 🌤️ AI Weather Agent

An **AI-powered weather assistant** that uses an LLM agent to fetch real-time weather data for any city using the OpenWeather API.

---

## 🚀 Features

- 🤖 AI Agent powered by Groq (LLaMA 3.1)
- 🌍 Real-time weather data using OpenWeather API
- 🛠️ Tool calling with Pydantic AI
- 🎯 Clean and interactive UI using Streamlit
- 📦 Structured output using Pydantic models

---

## 🧠 How It Works

1. User asks a question (e.g., *"What's the weather in Mumbai?"*)
2. AI agent understands the intent
3. Agent calls the `get_weather_forecast` tool
4. Tool fetches data from OpenWeather API
5. AI formats and returns a user-friendly response

---

## 🖥️ UI Overview

- Input box for user query  
- Button to fetch weather  
- AI-generated response display  
- Loading spinner & error handling  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pydantic AI  
- Groq (LLaMA 3.1)  
- OpenWeather API  
- Requests  

---

## 📂 Project Structure

```
Pydantic-AI-Agent/
│
├── app.py                # Streamlit UI
├── ai_agent_utility.py   # AI agent + tool logic
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/CoderVindra/Pydantic-AI-Agent.git
cd Pydantic-AI-Agent
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
API_KEY=your_openweather_api_key
```

### 5. Run the application
```bash
streamlit run app.py
```

---

## 💡 Example Query

```
What's the weather in Delhi?
```

### ✅ Example Response

```
The current weather in Delhi is Clear sky with a temperature of 32°C.
```

---

## 🔐 Environment Variables

| Variable        | Description                  |
|----------------|------------------------------|
| GROQ_API_KEY   | API key for Groq LLM         |
| API_KEY        | OpenWeather API key          |

---

## ⭐ Support

If you found this project helpful, please give it a ⭐ on GitHub!

---

## 👨‍💻 Author

**Ravindra Pawar**
