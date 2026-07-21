# LangChain Chatbot Examples

A collection of LangChain examples demonstrating various chatbot implementations and prompt engineering techniques using Google's Gemini AI model.

## 📋 Overview

This project showcases different approaches to building AI chatbots and applications using LangChain framework with Google Gemini AI. From basic chatbots to streaming responses and specialized travel planning assistants, these examples demonstrate progressive concepts in AI application development.

## 🚀 Features

- **Basic Chatbots**: Simple conversational AI with message history
- **Streaming Responses**: Real-time token-by-token response generation
- **Prompt Templates**: Reusable and customizable prompt engineering
- **Prompt Chaining**: Sequential processing for complex workflows
- **Web Interface**: Streamlit-based interactive chatbot UI
- **Specialized AI Agents**: Custom travel planning and weather assistants
- **Tool Integration**: External API integration with function calling
- **Few-Shot Learning**: Example-based prompt engineering for ticket triage
- **Semantic Selection**: Vector-based example selection for improved accuracy
- **Conditional Chains**: Dynamic routing based on sentiment analysis
- **Multi-Stage Code Review**: Comprehensive AI-powered code analysis and recommendations

## 📦 Requirements

```
langchain
langchain-google-genai
langchain-chroma
python-dotenv
streamlit
requests
pydantic
```

## 🔧 Setup

1. **Clone or download this repository**

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install langchain langchain-google-genai langchain-chroma python-dotenv streamlit requests pydantic
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   WEATHER_API_KEY=your_openweathermap_api_key_here  # Required for 10_weather_agent.py
   ```

## 📚 Project Files

### 1. `1_main.py` - Basic Chatbot with Message Objects
A fundamental chatbot implementation using LangChain's message objects (HumanMessage, AIMessage) for proper conversation tracking.

**Features:**
- Conversation history management
- Type-safe message handling
- Command-line interface

**Run:**
```bash
python 1_main.py
```

### 2. `2_chatbot.py` - Simple String-Based Chatbot
A simpler chatbot storing conversation as plain strings.

**Features:**
- Lightweight conversation history
- Basic input/output loop

**Run:**
```bash
python 2_chatbot.py
```

### 3. `3_msg.py` - Personality-Enhanced Chatbot
Chatbot with a system message defining its personality and behavior.

**Features:**
- System message for AI personality
- Humorous and professional tone
- Emoji support in responses

**Run:**
```bash
python 3_msg.py
```

### 4. `4_stream.py` - Streaming Response Chatbot
Real-time streaming chatbot that displays responses token-by-token as they're generated.

**Features:**
- Streaming API integration
- Real-time response display
- Enhanced user experience

**Run:**
```bash
python 4_stream.py
```

### 5. `5_PrompTemplate.py` - Prompt Chaining Demo
Demonstrates advanced prompt chaining by generating an article and creating quiz questions from it.

**Features:**
- PromptTemplate usage
- Chain creation (article → quiz)
- Output parsing
- Sequential processing

**Run:**
```bash
python 5_PrompTemplate.py
```

### 6. `6_generate_prompt.py` - Travel Planner Prompt Generator
Creates and saves a reusable prompt template for travel planning.

**Features:**
- Complex prompt template creation
- Template serialization to JSON
- Multi-variable input handling

**Run:**
```bash
python 6_generate_prompt.py
```

**Generates:** `travel_planner_prompt.json`

### 7. `7_travel_planner.py` - Travel Planning Assistant
Uses the saved prompt template to generate personalized travel itineraries.

**Features:**
- Loads prompt from JSON file
- Streaming responses
- Personalized travel recommendations
- Budget-aware planning

**Run:**
```bash
python 7_travel_planner.py
```

**Includes:**
- Activities and attractions
- Local food suggestions
- Transportation tips
- Cultural guidelines
- Packing checklist
- Unique experiences

### 8. `8_streamlit-chabot.py` - Web-Based Chatbot UI
A beautiful web interface for the chatbot using Streamlit.

**Features:**
- Modern chat interface
- Session state management
- Message history display
- User-friendly UI

**Run:**
```bash
streamlit run 8_streamlit-chabot.py
```

Then open your browser to the provided local URL (typically `http://localhost:8501`)

### 9. `travel_planner_prompt.json`
Serialized prompt template for travel planning with all input variables and formatting.

### 10. `10_weather_agent.py` - Weather Agent with Tool Integration
An AI agent that fetches real-time weather data using OpenWeatherMap API and tools.

**Features:**
- Tool integration with `@tool` decorator
- Real-time API calls to OpenWeatherMap
- Agent-based architecture
- Humorous weather responses with emojis

**Run:**
```bash
python 10_weather_agent.py
```

**Requirements:** Obtain a free API key from [OpenWeatherMap](https://openweathermap.org/api) and add it to your `.env` file.

### 11. `11_FewshotPromptTemplate.py` - Few-Shot Learning for Ticket Triage
Demonstrates few-shot prompting for ticket classification using example-based learning.

**Features:**
- FewShotPromptTemplate implementation
- Ticket triage automation
- Multi-category classification (billing, bug, feature-request)
- Priority assignment (P1-P4)
- Team routing

**Run:**
```bash
python 11_FewshotPromptTemplate.py
```

**Use Case:** Automate customer support ticket categorization and routing.

### 12. `12_FewshotPromptTemplateSelector.py` - Semantic Example Selection
Advanced few-shot learning with semantic similarity-based example selection.

**Features:**
- SemanticSimilarityExampleSelector
- Chroma vector database
- Google embeddings (gemini-embedding-001)
- Dynamic example selection (k=2 most relevant)
- More accurate classification using semantic matching

**Run:**
```bash
python 12_FewshotPromptTemplateSelector.py
```

**Advantage:** Automatically selects the most relevant examples based on input similarity.

### 13. `13_Conditional_chain.py` - Conditional Chains with Sentiment Analysis
Demonstrates conditional routing using RunnableBranch based on sentiment analysis.

**Features:**
- Pydantic output parsing for structured data
- Sentiment classification (positive/negative)
- Conditional chain branching with RunnableBranch
- Auto-generates thank you or apology emails
- Extracts structured feedback (highlights, lowlights, ratings)

**Run:**
```bash
python 13_Conditional_chain.py
```

**Use Case:** Automated feedback processing and response generation for training programs.

### 14. `14_code_review_assistant.py` - AI Code Review Assistant (Streamlit App)
A comprehensive multi-stage AI-powered code review application that analyzes source code and generates detailed review reports.

**Features:**
- **Multi-Chain Architecture:**
  - Analysis Chain: Identifies bugs, performance, security, readability, and best practice issues
  - Classification Chain: Determines primary issue type using Pydantic structured output
  - Branch Chain: Routes to specialized review prompts based on classification
  - Sequential Chain: Combines analysis and recommendations into final report
- **Structured Output Parsing:**
  - Pydantic models for CodeIssue and CodeAnalysis
  - Severity levels (critical, high, medium, low)
  - Line-by-line issue tracking
  - Quality score (1-10)
- **Specialized Review Types:**
  - Bug detection and fix recommendations
  - Performance optimization suggestions
  - Security vulnerability assessment
  - Readability improvements
  - Best practices guidance
- **Interactive Streamlit UI:**
  - Code input area with syntax highlighting
  - Multi-stage process visualization
  - Expandable sections for each review stage
  - Download final report as Markdown
  - Side-by-side code and results layout

**Run:**
```bash
streamlit run 14_code_review_assistant.py
```

**Supported Languages:** Python, JavaScript, Java, C++, C#, Go, Ruby, PHP, TypeScript, and more

**Use Case:** Automated code quality assessment, security audits, code review automation, and developer education.

### Code Review Module
The `code_review/` folder contains reusable components:

- **`CodeReviewAssistant.py`**: Standalone module for programmatic code review
  ```python
  from code_review.CodeReviewAssistant import CodeReviewAssistant
  
  assistant = CodeReviewAssistant()
  result = assistant.review_code(your_code)
  print(result["final_report"])
  ```

- **`sample_codes.py`**: Collection of test code samples with various issues
  - Buggy code examples
  - Performance problems
  - Security vulnerabilities
  - Readability issues
  - Best practice violations
  - Good code examples
  - Multi-language samples (Python, JavaScript, Java)

## 🎯 Usage Examples

### Basic Chat
```bash
python 3_msg.py
```
```
You: What is artificial intelligence?
AI: [Response with humor and emojis]
```

### Generate Travel Plan
```bash
python 7_travel_planner.py
```
Modify the script parameters for your destination and preferences.

### Launch Web Interface
```bash
streamlit run 8_streamlit-chabot.py
```

## 🛠️ Key Concepts Demonstrated

1. **LangChain Framework**: Core functionality and abstractions
2. **Google Gemini Integration**: Using `ChatGoogleGenerativeAI`
3. **Message Types**: HumanMessage, AIMessage, SystemMessage
4. **Prompt Engineering**: Templates and variable injection
5. **Chain Creation**: Sequential processing workflows
6. **Streaming**: Real-time response generation
7. **State Management**: Conversation history tracking
8. **UI Development**: Streamlit integration
9. **Tool Integration**: Function calling and external API integration
10. **Agent Architecture**: Building autonomous AI agents with tools
11. **Few-Shot Learning**: Example-based prompting and classification
12. **Vector Databases**: Chroma for semantic similarity search
13. **Embeddings**: Google Gemini embeddings for semantic matching
14. **Output Parsing**: Pydantic models for structured data extraction
15. **Conditional Routing**: RunnableBranch for dynamic workflow control17. **Multi-Stage Chains**: Complex sequential and branching chains for code review
18. **Structured Analysis**: Pydantic-based code issue detection and classification
## 📖 Learning Path

Follow this sequence for progressive learning:

**Phase 1: Basics**
1. Start with `2_chatbot.py` (simplest)
2. Upgrade to `1_main.py` (proper message objects)
3. Add personality with `3_msg.py`
4. Enable streaming in `4_stream.py`

**Phase 2: Prompt Engineering**
5. Learn chaining with `5_PrompTemplate.py`
6. Create templates with `6_generate_prompt.py`
7. Build specialized agents with `7_travel_planner.py`

**Phase 3: Advanced Features**
8. Deploy with UI using `8_streamlit-chabot.py`
9. Explore tool integration with `10_weather_agent.py`
10. Learn few-shot prompting with `11_FewshotPromptTemplate.py`
11. Advanced selection with `12_FewshotPromptTemplateSelector.py`
12. Master conditional routing with `13_Conditional_chain.py`

**Phase 4: Complex Multi-Chain Applications**
13. Build comprehensive AI app with `14_code_review_assistant.py`
    - Multi-stage chain orchestration
    - Specialized routing and branching
    - Structured output with Pydantic
    - Production-ready Streamlit UI

## ⚙️ Configuration

All examples use the Google Gemini 3.1 Flash Lite model for fast, cost-effective responses. You can modify the model in each file:

```python
model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
```

Other available models:
- `gemini-pro`
- `gemini-1.5-pro`
- `gemini-1.5-flash`

## 🔐 Environment Variables

Required in `.env` file:
```
GOOGLE_API_KEY=your_api_key_here
WEATHER_API_KEY=your_openweathermap_api_key_here  # Optional, only for 10_weather_agent.py
```

**API Key Sources:**
- Google API Key: [Google AI Studio](https://makersuite.google.com/app/apikey)
- Weather API Key: [OpenWeatherMap](https://openweathermap.org/api) (Free tier available)

## 🐛 Troubleshooting

**ModuleNotFoundError**: Ensure all dependencies are installed
```bash
pip install -r requirements.txt
```

**API Key Error**: Check your `.env` file and API key validity

**Streamlit Issues**: Make sure streamlit is installed
```bash
pip install streamlit
```

## 🤝 Contributing

Feel free to fork, modify, and expand these examples for your learning or projects.

## 📝 License

This project is provided as-is for educational purposes.

## 🔗 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Google Gemini API](https://ai.google.dev/)
- [Streamlit Docs](https://docs.streamlit.io/)

---

**Happy Coding! 🚀**