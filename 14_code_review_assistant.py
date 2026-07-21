import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.runnables import RunnableBranch
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal, List

load_dotenv()

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")


# Define structured output models
class CodeIssue(BaseModel):
    """Structured representation of code issues found"""
    line_number: int = Field(description="Line number where the issue occurs")
    issue_type: str = Field(description="Type of issue: bug, performance, security, readability, or best_practice")
    severity: Literal['critical', 'high', 'medium', 'low'] = Field(description="Severity level of the issue")
    description: str = Field(description="Description of the issue")


class CodeAnalysis(BaseModel):
    """Structured code analysis result"""
    language: str = Field(description="Programming language detected")
    primary_issue_type: Literal['bug', 'performance', 'security', 'readability', 'best_practice', 'none'] = Field(
        description="The most critical type of issue found in the code"
    )
    issues: List[CodeIssue] = Field(description="List of issues found in the code")
    overall_quality_score: int = Field(description="Overall code quality score from 1-10", ge=1, le=10)


# Step 1: Analysis Chain - Analyzes code and identifies issues
analysis_parser = PydanticOutputParser(pydantic_object=CodeAnalysis)

analysis_prompt = PromptTemplate(
    template="""You are an expert code reviewer. Analyze the following code and identify potential issues.

Code to analyze:
```
{code}
```

Focus on:
- Bugs and logical errors
- Performance issues
- Security vulnerabilities
- Code readability and maintainability
- Coding best practices

Provide a detailed analysis with specific line numbers, issue types, severity levels, and descriptions.
{format_instructions}
""",
    input_variables=["code"],
    partial_variables={"format_instructions": analysis_parser.get_format_instructions()}
)

analysis_chain = analysis_prompt | llm | analysis_parser


# Step 2: Specialized Review Chains based on issue type
bug_review_prompt = PromptTemplate(
    template="""You are a bug detection specialist. The code has been identified as having BUG issues.

Code:
```
{code}
```

Analysis Result:
{analysis}

Provide detailed recommendations to fix the bugs:
1. Explain each bug and its potential impact
2. Provide code examples showing how to fix each bug
3. Suggest testing strategies to prevent similar bugs
4. Rate the bug severity and recommend priority

Format your response as a structured bug fix guide.
""",
    input_variables=["code", "analysis"]
)

performance_review_prompt = PromptTemplate(
    template="""You are a performance optimization expert. The code has been identified as having PERFORMANCE issues.

Code:
```
{code}
```

Analysis Result:
{analysis}

Provide detailed recommendations to improve performance:
1. Identify performance bottlenecks with explanations
2. Suggest optimized code alternatives
3. Recommend algorithm or data structure improvements
4. Estimate potential performance gains
5. Discuss trade-offs between optimization and readability

Format your response as a performance optimization guide.
""",
    input_variables=["code", "analysis"]
)

security_review_prompt = PromptTemplate(
    template="""You are a security expert. The code has been identified as having SECURITY issues.

Code:
```
{code}
```

Analysis Result:
{analysis}

Provide detailed security recommendations:
1. Explain each security vulnerability and its risk level
2. Provide secure code examples
3. Suggest security best practices
4. Recommend security testing approaches
5. Reference relevant security standards (OWASP, CWE, etc.)

Format your response as a security audit report.
""",
    input_variables=["code", "analysis"]
)

readability_review_prompt = PromptTemplate(
    template="""You are a code readability and maintainability expert. The code has been identified as having READABILITY issues.

Code:
```
{code}
```

Analysis Result:
{analysis}

Provide detailed recommendations to improve readability:
1. Suggest better naming conventions
2. Recommend code structure improvements
3. Provide refactoring suggestions
4. Suggest documentation improvements
5. Show before/after examples

Format your response as a code readability improvement guide.
""",
    input_variables=["code", "analysis"]
)

best_practice_review_prompt = PromptTemplate(
    template="""You are a coding standards and best practices expert. The code has been identified as having BEST PRACTICE issues.

Code:
```
{code}
```

Analysis Result:
{analysis}

Provide detailed recommendations to follow best practices:
1. Identify violations of coding standards
2. Suggest language-specific best practices
3. Recommend design pattern improvements
4. Provide code examples following best practices
5. Reference style guides and standards

Format your response as a best practices review.
""",
    input_variables=["code", "analysis"]
)

general_review_prompt = PromptTemplate(
    template="""You are a code review expert. The code has been analyzed and needs a general review.

Code:
```
{code}
```

Analysis Result:
{analysis}

Provide a comprehensive code review:
1. Summarize findings
2. Provide general recommendations
3. Suggest improvements across all categories
4. Highlight positive aspects of the code
5. Provide an action plan for improvements

Format your response as a general code review report.
""",
    input_variables=["code", "analysis"]
)


# Step 3: Branch Chain - Routes to specialized review based on primary issue type
def create_review_branch():
    """Creates a branching chain based on issue type"""
    return RunnableBranch(
        (lambda x: x["primary_issue_type"] == "bug", 
         bug_review_prompt | llm | StrOutputParser()),
        (lambda x: x["primary_issue_type"] == "performance", 
         performance_review_prompt | llm | StrOutputParser()),
        (lambda x: x["primary_issue_type"] == "security", 
         security_review_prompt | llm | StrOutputParser()),
        (lambda x: x["primary_issue_type"] == "readability", 
         readability_review_prompt | llm | StrOutputParser()),
        (lambda x: x["primary_issue_type"] == "best_practice", 
         best_practice_review_prompt | llm | StrOutputParser()),
        general_review_prompt | llm | StrOutputParser()  # Default branch
    )


# Step 4: Final Report Chain
final_report_prompt = PromptTemplate(
    template="""Create a comprehensive code review report.

ANALYSIS:
{analysis}

SPECIALIZED REVIEW:
{specialized_review}

Generate a final structured report with:
1. Executive Summary
2. Code Quality Score and Explanation
3. Critical Issues (prioritized)
4. Detailed Findings
5. Recommendations (with examples)
6. Action Items (prioritized list)
7. Conclusion

Format the report professionally with clear sections and actionable items.
""",
    input_variables=["analysis", "specialized_review"]
)

final_report_chain = final_report_prompt | llm | StrOutputParser()


# Streamlit UI
def main():
    st.set_page_config(page_title="AI Code Review Assistant", page_icon="🔍", layout="wide")
    
    st.title("🔍 AI Code Review Assistant")
    st.markdown("""
    Submit your code for AI-powered comprehensive review. The system analyzes your code for bugs, performance issues, 
    security vulnerabilities, readability problems, and best practice violations.
    """)
    
    # Simple settings in main area
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown("### 📝 Enter Your Code")
    with col2:
        show_stages = st.checkbox("Show stages", value=True)
    
    # Code input area
    code_input = st.text_area(
        "Paste your code here:",
        height=350,
        placeholder="Paste your Python, JavaScript, Java, or other code here for review...",
        label_visibility="collapsed"
    )
    
    # Analyze button
    analyze_button = st.button("🚀 Start Code Review", type="primary", use_container_width=True)
    
    st.markdown("---")
    
    # Results area
    results_container = st.container()
    
    # Process code review
    if analyze_button and code_input.strip():
        with results_container:
            try:
                # Stage 1: Analysis
                with st.spinner("🔍 Analyzing code..."):
                    analysis_result = analysis_chain.invoke({"code": code_input})
                
                # Display quick summary
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Language", analysis_result.language)
                with col2:
                    st.metric("Quality Score", f"{analysis_result.overall_quality_score}/10")
                with col3:
                    st.metric("Primary Issue", analysis_result.primary_issue_type.replace('_', ' ').title())
                
                if show_stages:
                    with st.expander("📊 Detailed Analysis", expanded=False):
                        st.subheader("Issues Found:")
                        for idx, issue in enumerate(analysis_result.issues, 1):
                            severity_color = {
                                'critical': '🔴',
                                'high': '🟠',
                                'medium': '🟡',
                                'low': '🟢'
                            }
                            st.markdown(f"""
                            **{idx}. {severity_color.get(issue.severity, '⚪')} Line {issue.line_number}** - *{issue.issue_type}* ({issue.severity})
                            
                            {issue.description}
                            """)
                
                # Stage 2: Specialized Review
                with st.spinner(f"🎯 Generating specialized review..."):
                    review_branch = create_review_branch()
                    specialized_review = review_branch.invoke({
                        "code": code_input,
                        "analysis": analysis_result.json(),
                        "primary_issue_type": analysis_result.primary_issue_type
                    })
                
                if show_stages:
                    with st.expander(f"🎯 Specialized Review", expanded=False):
                        st.markdown(specialized_review)
                
                # Stage 3: Final Report
                with st.spinner("📄 Creating final report..."):
                    final_report = final_report_chain.invoke({
                        "analysis": analysis_result.json(),
                        "specialized_review": specialized_review
                    })
                
                # Display Final Report
                st.success("✅ Code Review Complete!")
                st.markdown("### 📄 Final Review Report")
                st.markdown(final_report)
                
                # Download report
                st.download_button(
                    label="📥 Download Report as Markdown",
                    data=final_report,
                    file_name="code_review_report.md",
                    mime="text/markdown",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"❌ Error during code review: {str(e)}")
                st.exception(e)
    
    elif analyze_button and not code_input.strip():
        results_container.warning("⚠️ Please enter some code to review!")


if __name__ == "__main__":
    main()
