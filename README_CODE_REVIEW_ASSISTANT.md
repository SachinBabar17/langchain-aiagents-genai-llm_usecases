# AI Code Review Assistant

A sophisticated AI-powered code review system built with LangChain, Google Gemini, and Streamlit. This application provides comprehensive code analysis with specialized reviews based on issue types.

## Features

### Multi-Stage Analysis Pipeline

1. **Initial Code Analysis**
   - Automatic programming language detection
   - Structured issue identification with line numbers
   - Severity classification (critical, high, medium, low)
   - Overall quality scoring (1-10 scale)

2. **Specialized Reviews**
   - **Bug Detection**: Identifies logical errors and provides fix recommendations
   - **Performance Optimization**: Suggests algorithmic improvements and bottleneck fixes
   - **Security Audit**: Detects vulnerabilities with OWASP/CWE references
   - **Readability Enhancement**: Improves code structure and naming conventions
   - **Best Practices**: Ensures adherence to coding standards

3. **Comprehensive Reporting**
   - Executive summary
   - Prioritized action items
   - Code examples and recommendations
   - Quality metrics and explanations

## Requirements

### Dependencies

```
streamlit
langchain-google-genai
langchain-core
python-dotenv
pydantic
```

### Environment Setup

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

## Installation

1. Clone or download the project:
```bash
cd c:\Users\yys2kor\Desktop\langchain
```

2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

3. Install required packages:
```bash
pip install streamlit langchain-google-genai langchain-core python-dotenv pydantic
```

4. Set up your Google API key:
   - Get a Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a `.env` file with your API key

## Usage

### Running the Application

```bash
streamlit run 15_code_review_assiast.py
```

The application will open in your default browser at `http://localhost:8501`

### How to Use

1. **Select Programming Language**: Choose from Python, JavaScript, Java, C++, C#, Go, Rust, TypeScript, Ruby, PHP, Swift, Kotlin, or Other

2. **Paste Your Code**: Enter the code you want to review in the text area

3. **Optional Settings**:
   - Toggle "Show stages" to see detailed analysis at each step

4. **Start Review**: Click the "Start Code Review" button

5. **Review Results**:
   - View quick metrics (Language, Quality Score, Primary Issue)
   - Expand sections to see detailed analysis
   - Read the comprehensive final report with actionable recommendations

## Architecture

### Chain Pipeline

```
User Input → Analysis Chain → Branch Chain → Final Report Chain
                    ↓              ↓               ↓
            CodeAnalysis    Specialized      Final Report
            (Structured)      Review         (Markdown)
```

### Components

#### 1. Analysis Chain
- **Input**: Code + Language
- **Process**: Uses Pydantic parser for structured output
- **Output**: `CodeAnalysis` object with issues, severity, and primary issue type

#### 2. Branch Chain (RunnableBranch)
Routes to specialized reviewers based on `primary_issue_type`:
- `bug` → Bug Review Chain
- `performance` → Performance Review Chain
- `security` → Security Review Chain
- `readability` → Readability Review Chain
- `best_practice` → Best Practice Review Chain
- `default` → General Review Chain

#### 3. Final Report Chain
- **Input**: Analysis + Specialized Review
- **Process**: Synthesizes information into structured report
- **Output**: Professional code review document

### Data Models

```python
CodeIssue:
  - line_number: int
  - issue_type: str
  - severity: Literal['critical', 'high', 'medium', 'low']
  - description: str

CodeAnalysis:
  - language: str
  - primary_issue_type: Literal['bug', 'performance', 'security', 'readability', 'best_practice', 'none']
  - issues: List[CodeIssue]
  - overall_quality_score: int (1-10)
```

## Configuration

### LLM Model

The application uses Google's Gemini model. To change the model:

```python
llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
# Change to: model="gemini-1.5-pro" or other available models
```

### Supported Languages

Currently supports:
- Python, JavaScript, Java, C++, C#
- Go, Rust, TypeScript, Ruby, PHP
- Swift, Kotlin, and Others

### UI Customization

Modify Streamlit settings in the `main()` function:

```python
st.set_page_config(
    page_title="AI Code Review Assistant",
    page_icon="🔍",
    layout="wide"
)
```

## Example Use Cases

### 1. Bug Detection
Submit code with potential bugs to get:
- Exact line numbers of issues
- Bug explanation and impact analysis
- Fix recommendations with examples
- Testing strategies

### 2. Security Audit
Review code for vulnerabilities:
- SQL injection risks
- XSS vulnerabilities
- Authentication issues
- Secure coding recommendations

### 3. Performance Review
Optimize your code:
- Identify bottlenecks
- Algorithm improvements
- Data structure suggestions
- Estimated performance gains

### 4. Code Refactoring
Improve readability:
- Better naming conventions
- Structure improvements
- Documentation suggestions
- Before/after examples

## Troubleshooting

### Common Issues

1. **API Key Error**
   ```
   Error: GOOGLE_API_KEY not found
   Solution: Ensure .env file exists with valid API key
   ```

2. **Module Import Error**
   ```
   Error: No module named 'langchain_google_genai'
   Solution: pip install langchain-google-genai
   ```

3. **Streamlit Port Already in Use**
   ```
   Solution: streamlit run 15_code_review_assiast.py --server.port 8502
   ```

## Best Practices

1. **Code Size**: Keep code submissions under 500 lines for optimal analysis
2. **Context**: Include relevant imports and function definitions
3. **Language Selection**: Select the correct language for accurate analysis
4. **Iterative Review**: Review code in chunks for complex projects

## Advanced Features

### Stage-by-Stage View

Enable "Show stages" to see:
- Initial analysis with all detected issues
- Specialized review details
- Progressive report generation

### Quality Metrics

The system evaluates:
- Code correctness (bugs, logic errors)
- Performance efficiency
- Security posture
- Maintainability
- Standards compliance

## Future Enhancements

- [ ] Support for multiple file analysis
- [ ] Integration with Git repositories
- [ ] Custom rule configuration
- [ ] Historical review tracking
- [ ] Team collaboration features
- [ ] Export reports (PDF, HTML)

## Technical Details

- **Framework**: Streamlit for UI
- **LLM**: Google Gemini (gemini-3.1-flash-lite)
- **Orchestration**: LangChain LCEL (LangChain Expression Language)
- **Output Parsing**: Pydantic for structured data
- **Branching Logic**: RunnableBranch for conditional routing

## License

This project is provided as-is for educational and development purposes.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments in `15_code_review_assiast.py`
3. Verify all dependencies are installed correctly

---

**Note**: This application requires an active internet connection and a valid Google Gemini API key to function.
