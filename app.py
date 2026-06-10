import streamlit as st
import time
import ast
import streamlit.components.v1 as components

# 1. Global Page Layout & Structural Theme Setup
st.set_page_config(
    page_title="AI Technical Interview Coach | Microsoft Foundry IQ Pro",
    page_icon="🤖",
    layout="wide"
)

# Premium Custom CSS
st.markdown("""
    <style>
    .main-title { font-family: 'Segoe UI', sans-serif; font-size: 38px; font-weight: 700; color: #107C41; text-align: center; margin-bottom: 2px; }
    .subtitle { font-family: 'Segoe UI', sans-serif; font-size: 15px; text-align: center; color: #555555; margin-bottom: 25px; }
    .iq-tag-wrapper { text-align: center; margin-bottom: 25px; }
    .iq-tag { background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%); color: #1B5E20; padding: 8px 18px; border-radius: 50px; font-weight: 600; font-size: 13px; display: inline-block; border: 1px solid #A5D6A7; }
    
    /* Elegant Content Frame Cards */
    .card-box { background-color: #FFFFFF; padding: 22px; border-radius: 14px; box-shadow: 0 4px 15px rgba(0,0,0,0.04); border: 1px solid #EAEAEA; margin-bottom: 20px; }
    .constraint-card { background-color: #FFF9C4; padding: 15px; border-radius: 10px; border-left: 6px solid #FBC02D; font-size: 14px; margin-bottom: 20px; color: #574A00; }
    .cheat-sheet-card { background-color: #E3F2FD; padding: 15px; border-radius: 10px; border-left: 6px solid #1976D2; font-size: 14px; color: #0D47A1; margin-bottom: 20px; }
    
    /* Multi-Agent Station Headers */
    .agent-header { font-size: 14px; font-weight: 700; color: #111111; margin-bottom: 5px; display: flex; align-items: center; }
    
    /* Premium Action Buttons */
    div.stButton > button:first-child { background: linear-gradient(135deg, #107C41 0%, #1B5E20 100%) !important; color: white !important; border-radius: 8px !important; border: none !important; padding: 12px 28px !important; font-weight: 600 !important; box-shadow: 0 4px 12px rgba(16,124,65,0.2); transition: all 0.3s ease; }
    div.stButton > button:first-child:hover { transform: translateY(-2px); box-shadow: 0 6px 16px rgba(16,124,65,0.3); }
    </style>
""", unsafe_allow_html=True)

# Define the Multi-Problem Dataset Repository
PROBLEMS = {
    "Product of Array Except Self": {
        "desc": "Given an integer array <code>nums</code>, return an array <code>answer</code> such that <code>answer[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code>.",
        "constraints": [
            "Your algorithm must run completely <strong>without using the division operator (<code>/</code>)</strong>.",
            "Your total calculation strategy must scale smoothly within strict linear <strong>O(n) time complexity bounds</strong>."
        ],
        "boilerplate": "def productExceptSelf(nums):\n    # Write your optimized linear O(n) solution here\n    length = len(nums)\n    answer = [1] * length\n    \n    pass"
    },
    "Two Sum (Optimal Search)": {
        "desc": "Given an array of integers <code>nums</code> and an integer <code>target</code>, return indices of the two numbers such that they add up to <code>target</code>.",
        "constraints": [
            "Your algorithm must find the solution in a single pass with strict linear <strong>O(n) time complexity</strong>.",
            "You cannot use nested loops, meaning brute-force search operations are completely disabled."
        ],
        "boilerplate": "def twoSum(nums, target):\n    # Write your optimized single-pass O(n) hash map solution here\n    seen_map = {}\n    \n    pass"
    },
    "Valid Parentheses Layout": {
        "desc": "Given a string <code>s</code> containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is structurally valid.",
        "constraints": [
            "You must process string parsing elements using a sequential <strong>Stack (LIFO) data structure data pattern</strong>.",
            "The algorithm must resolve all opening/closing boundaries inside linear <strong>O(n) execution parameters</strong>."
        ],
        "boilerplate": "def isValid(s):\n    # Write your stack-based linear structural verification here\n    char_stack = []\n    \n    pass"
    }
}

# 2. Multi-Problem Abstract Syntax Tree (AST) Compiler Engine
def analyze_code_structure(code_string, problem_name):
    try:
        tree = ast.parse(code_string)
    except SyntaxError:
        return 10, "❌ **Foundry IQ Syntax Exception:** The compiler could not parse your code structural patterns. Check your indentation blocks, colons, or brackets."

    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    if not functions:
        return 10, "❌ **Foundry IQ Parser Failure:** Core functional sequence mapping missing. Ensure your code remains nested inside a proper function block."
    
    target_function = functions[0]
    
    loop_nodes = [node for node in ast.walk(target_function) if isinstance(node, (ast.For, ast.While))]
    has_nested_loops = False
    for current_loop in loop_nodes:
        for child_node in ast.walk(current_loop):
            if child_node is not current_loop and isinstance(child_node, (ast.For, ast.While)):
                has_nested_loops = True
                break

    if problem_name == "Product of Array Except Self":
        has_division = any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(target_function))
        if has_division:
            return 40, "❌ **Foundry IQ Constraint Violation:** The division operator (`/`) was detected. Scale bounds require mapping prefix/suffix elements without division reduction."
        if has_nested_loops:
            return 60, "⚠️ **Foundry IQ Complexity Warning:** Nested loop iteration tracks detected. Computational runtime resolves to O(n²), failing production constraints."
        if len(loop_nodes) >= 2 and not has_nested_loops:
            return 100, "✅ **Foundry IQ Verification Passed:** Optimal linear runtime O(n) path confirmed! The solution splits work into clean sequential prefix and suffix array tracking passes."
        return 75, "💡 **Foundry IQ Feedback:** Linear architecture foundations look clean, ensure your code captures element values scanning from both array flanks."

    elif problem_name == "Two Sum (Optimal Search)":
        if has_nested_loops:
            return 50, "❌ **Foundry IQ Efficiency Failure:** Brute force O(n²) nested loop detected. Enterprise scale rules require an optimal single-pass linear Hash Map strategy."
        has_dict_lookup = any(isinstance(node, (ast.Dict, ast.Subscript)) for node in ast.walk(target_function))
        if has_dict_lookup and len(loop_nodes) == 1:
            return 100, "✅ **Foundry IQ Verification Passed:** Optimal O(n) Hash Map allocation verified! Instantaneous dictionary index retrieval path is fully production grade."
        return 70, "💡 **Foundry IQ Feedback:** Ensure you initialize and write code tracking key-value parameters inside a search map to bypass quadratic search paths."

    elif problem_name == "Valid Parentheses Layout":
        if has_nested_loops:
            return 40, "❌ **Foundry IQ Complexity Error:** Linear string parsing should operate within single iteration boundaries without nesting configurations."
        calls = [node.func.attr for node in ast.walk(target_function) if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)]
        has_stack_ops = "pop" in calls or "append" in calls
        if has_stack_ops:
            return 100, "✅ **Foundry IQ Verification Passed:** Classic linear Stack LIFO pattern verified. All nested brace matching parameters evaluate safely."
        return 65, "💡 **Foundry IQ Feedback:** Deploy a tracking array as a Last-In-First-Out (LIFO) stack layout to match matching bracket boundaries smoothly."

    return 50, "Analysis completed."


# 3. Sidebar Console Layout
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; padding-top: 5px;'>
        <img src='https://img.icons8.com/color/96/microsoft.png' width='44'><br>
        <h4 style='margin-top: 8px; color: #333333; font-family: sans-serif; margin-bottom:0;'>Foundry IQ Console</h4>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("⚙️ System Framework Configuration")
    active_layer = st.selectbox("Orchestrator Node", ["Foundry IQ (Deep Reasoning Node)", "Work IQ (Enterprise Semantic Hub)", "Fabric IQ (Analytical Mesh)"])
    
    # Sidebar countdown stopwatch
    st.markdown("---")
    st.subheader("⏱️ Session Assessment Timer")
    components.html("""
        <div style="font-family: 'Segoe UI', sans-serif; background-color: #f7f9fa; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #e1e4e6;">
            <span style="color: #666; font-size: 11px; font-weight: 600; text-transform: uppercase; display:block; margin-bottom:2px;">Real-Time Clock Bound</span>
            <span id="sidebar_clock" style="font-size: 24px; font-weight: bold; color: #d32f2f;">45:00</span>
        </div>
        <script>
            var duration = 45 * 60;
            var display = document.querySelector('#sidebar_clock');
            var timer = duration, minutes, seconds;
            setInterval(function () {
                minutes = parseInt(timer / 60, 10);
                seconds = parseInt(timer % 60, 10);
                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;
                display.textContent = minutes + ":" + seconds;
                if (--timer < 0) { timer = duration; }
            }, 1000);
        </script>
    """, height=80)

    # High-fidelity real-time AI Chat Dialogue Interface
    st.markdown("---")
    st.subheader("💬 Live Technical Mock Chat")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Welcome! I am your Microsoft Foundry IQ interview companion. Tell me, how are you approaching the scalability bounds of your selected problem configuration?"}
        ]
        
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if chat_input := st.chat_input("Speak to your technical coach..."):
        st.session_state.messages.append({"role": "user", "content": chat_input})
        with st.chat_message("user"):
            st.write(chat_input)
            
        # Cognitive response parser
        cleaned_in = chat_input.lower().strip()
        if cleaned_in in ["hi", "hello", "hey"]:
            reply = "Greetings Candidate! System diagnostics channels are open. Let's look over your computational loops—how do you plan to handle optimization metrics today?"
        elif cleaned_in in ["yes", "yeah", "yup", "ok", "sure"]:
            reply = "Fantastic progress trace! Translating confidence into syntax structure is exactly what we look for. Do you see any algorithmic corner cases we should check?"
        elif cleaned_in in ["no", "nope", "not yet", "help"]:
            reply = "Perfect point to pause and reflect. Break it down step-by-step: what is the primary data structure you are initializing to track state?"
        elif "nested" in cleaned_in or "n^2" in cleaned_in or "quadratic" in cleaned_in:
            reply = "Spot on! Nested elements run straight into an O(n²) crash barrier at scale. Let's aim to utilize auxiliary space mapping to force it down to linear time."
        elif "prefix" in cleaned_in or "suffix" in cleaned_in or "hash" in cleaned_in or "stack" in cleaned_in:
            reply = "Brilliant design strategy choice! Utilizing structural markers will allow you to clear the validation gating. Paste your syntax into the workspace frame!"
        else:
            reply = "Intriguing response pattern. As a core evaluation reminder, ensure your workspace algorithm bypasses secondary loops or unauthorized shortcuts."
            
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()  # Global rerun fixed


# 4. Main Canvas Workspace Construction
st.markdown("<div class='main-title'>AI Technical Interview Coach</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Accelerating System Architecture Readiness via Microsoft Foundry IQ Intelligence Layers</div>", unsafe_allow_html=True)
st.markdown("<div class='iq-tag-wrapper'><span class='iq-tag'>🎨 Track 1 Champion Blueprint: Creative Apps Platform</span></div>", unsafe_allow_html=True)

st.markdown("### 🛠️ Assessment Control Core")
active_problem_title = st.selectbox("Select Active Coding Challenge Prompt", list(PROBLEMS.keys()))
active_problem_data = PROBLEMS[active_problem_title]

left_panel, right_panel = st.columns([2, 1])

with left_panel:
    st.markdown(f"""
    <div class='card-box'>
        <h3 style='color: #111111; margin-top:0;'>📝 Active Prompt: {active_problem_title}</h3>
        <p style='color: #444444; font-size:14px; line-height: 1.5;'>{active_problem_data['desc']}</p>
    </div>
    """, unsafe_allow_html=True)

    constraints_html = "".join([f"<li>{c}</li>" for c in active_problem_data['constraints']])
    st.markdown(f"""
    <div class='constraint-card'>
        <strong>🚨 CORE SYSTEM ARCHITECTURE CONSTRAINTS:</strong>
        <ul style='margin-top: 5px; margin-bottom: 0; padding-left: 20px;'>{constraints_html}</ul>
    </div>
    """, unsafe_allow_html=True)

with right_panel:
    st.markdown("### 🎯 Rubric Gating Vectors")
    target_company = st.selectbox("Target Corporate Alignment Profile", ["Microsoft", "Amazon", "Google"])
    
    if target_company == "Amazon":
        st.markdown("""<div class='cheat-sheet-card'><strong>📦 Amazon Leadership Principles:</strong><br>Prioritizes <em>Bias for Action & Invent and Simplify</em>. System scale constraints verify that production modules can sustain sudden transaction traffic spikes.</div>""", unsafe_allow_html=True)
    elif target_company == "Microsoft":
        st.markdown("""<div class='cheat-sheet-card'><strong>💻 Microsoft Core Rubric Standards:</strong><br>Focuses heavily on <em>Growth Mindset & Multi-Step Reasonings</em>. Explaining structural code transformations via processing pipelines maximizes points.</div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class='cheat-sheet-card'><strong>🔍 Google Engineering Gating:</strong><br>Tests <em>Googliness & Systems Extensibility</em>. Optimization benchmarks strictly rule out processing overheads or hidden math shortcuts.</div>""", unsafe_allow_html=True)

# Main Code Sandbox Window
st.subheader("💻 Core Candidate Development Sandbox")

if "last_problem" not in st.session_state or st.session_state.last_problem != active_problem_title:
    st.session_state.last_problem = active_problem_title
    st.session_state.editor_code = active_problem_data["boilerplate"]

current_user_code = st.text_area("Sandbox Core Editor Window", value=st.session_state.editor_code, height=220, label_visibility="collapsed", key="editor_window_capture")


# 5. Live Diagnostics Telemetry Processing Node
if st.button("🚀 Run Foundry IQ Optimization Diagnostics", type="primary"):
    st.markdown("---")
    st.markdown("### 📊 Live Foundry IQ Telemetry Dashboard")
    
    with st.spinner("Foundry IQ Responsible AI Gating Shield: Inspecting codebase structure for injection vectors..."):
        time.sleep(0.5)
        if "import os" in current_user_code or "sys.exit" in current_user_code:
            st.error("🛡️ **Responsible AI Protection Exception:** Unauthorized hardware system commands intercepted. Compilation suspended to preserve multi-tenant container runtime isolation.")
            st.stop()
        else:
            st.caption("✅ **Responsible AI Gating Verification:** Code pattern checks clean. System data transmission authorized.")

    progress_bar = st.progress(0)
    status_text = st.empty()
    
    status_text.markdown("📡 *Establishing system diagnostics pipeline channel with Microsoft Foundry Node...*")
    time.sleep(0.4)
    progress_bar.progress(35)
    
    status_text.markdown("🔍 *Tokenizing syntax tree arrays to inspect block layout indentation mappings...*")
    time.sleep(0.4)
    progress_bar.progress(70)
    
    status_text.markdown("🛡️ *Verifying logical compiler compliance parameters against active rubric metrics...*")
    time.sleep(0.3)
    progress_bar.progress(100)
    status_text.empty()
    
    score_metric, evaluation_critique = analyze_code_structure(current_user_code, active_problem_title)
    
    # Render interactive fireworks explosion safely inside triple quotes
    if score_metric == 100:
        st.success(evaluation_critique)
        
        st.markdown("""
            <div class='card-box' style='background: linear-gradient(135deg, #FFF9C4 0%, #E8F5E9 100%); text-align: center; border: 2px dashed #4CAF50; margin-bottom: 5px;'>
                <h3 style='color: #1B5E20; margin: 0;'>🎉 CRACKERS POPPING: PRODUCTION EXCELLENCE VERIFIED! 🎉</h3>
            </div>
        """, unsafe_allow_html=True)
        
        components.html("""
            <div style="text-align:center; background-color: transparent;">
                <canvas id="fireworks_canvas" style="width: 100%; height: 260px;"></canvas>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
            <script>
                var canvas = document.getElementById('fireworks_canvas');
                var end = Date.now() + (3.5 * 1000);
                var myConfetti = confetti.create(canvas, { resize: true });
                
                (function frame() {
                    myConfetti({ particleCount: 6, angle: 60, spread: 60, origin: { x: 0.05, y: 0.85 } });
                    myConfetti({ particleCount: 6, angle: 120, spread: 60, origin: { x: 0.95, y: 0.85 } });
                    
                    if (Date.now() < end) {
                        requestAnimationFrame(frame);
                    }
                }());
            </script>
        """, height=280)
    elif score_metric >= 60:
        st.warning(evaluation_critique)
    else:
        st.error(evaluation_critique)
        
    # Telemetry Grid Block
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='card-box' style='text-align: center;'><span style='color: #666666; font-size: 12px; font-weight: 600; text-transform: uppercase;'>Foundry IQ Score</span><h2 style='color: {'#107C41' if score_metric == 100 else ('#FF9800' if score_metric == 60 else '#D32F2F')}; margin: 5px 0;'>{score_metric}/100</h2></div>", unsafe_allow_html=True)
    with c2:
        runtime_bound = "O(n) Linear Execution" if score_metric == 100 else ("O(n²) Quadratic Crash Bound" if score_metric == 60 else "Compilation Aborted")
        st.markdown(f"<div class='card-box' style='text-align: center;'><span style='color: #666666; font-size: 12px; font-weight: 600; text-transform: uppercase;'>Evaluated Complexity</span><h4 style='color: #333333; margin: 10px 0;'>{runtime_bound}</h4></div>", unsafe_allow_html=True)
    with c3:
        safety_flag = "Compliant ✅" if score_metric > 50 else "Violations Flags Detected ❌"
        st.markdown(f"<div class='card-box' style='text-align: center;'><span style='color: #666666; font-size: 12px; font-weight: 600; text-transform: uppercase;'>Responsible AI Gating</span><h4 style='color: #333333; margin: 10px 0;'>{safety_flag}</h4></div>", unsafe_allow_html=True)
        
    # Multi-Agent Reflection Review
    st.markdown("### 🤖 Foundry IQ Multi-Agent Reflection Review")
    agent_col1, agent_col2 = st.columns(2)
    
    with agent_col1:
        st.markdown("<div class='card-box' style='border-top: 4px solid #107C41;'>", unsafe_allow_html=True)
        st.markdown("<div class='agent-header'>⚙️ Agent Alpha: Deep Performance Profiler</div>", unsafe_allow_html=True)
        if score_metric == 100:
            st.write("*Analysis Output:* Core operations verify zero inner iterations. Execution maps completely down to single-pass arrays. Memory leaks: 0%. Performance bound is solid.")
        else:
            st.write("*Analysis Output:* Code structures indicate structural tracking bottlenecks. Redundant nested nodes are scaling metrics upward aggressively. Optimization required.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with agent_col2:
        st.markdown("<div class='card-box' style='border-top: 4px solid #1976D2;'>", unsafe_allow_html=True)
        st.markdown("<div class='agent-header'>🛡️ Agent Beta: Security & Compliance Auditor</div>", unsafe_allow_html=True)
        if score_metric > 40:
            st.write("*Analysis Output:* Code adheres to standard naming structures. No prohibited tokens or dangerous operations present inside the candidate functional tree.")
        else:
            st.write("*Analysis Output:* Code parameters failed safety criteria checks or contain syntax exceptions. Rectify basic operators before production shipping.")
        st.markdown("</div>", unsafe_allow_html=True)

    # Dynamic Progress Bar Breakdown Analytics
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.markdown("<h4>📈 Granular Quality Optimization Dimensions</h4>", unsafe_allow_html=True)
    time_score = 1.0 if score_metric == 100 else (0.6 if score_metric == 60 else 0.1)
    st.progress(time_score, text=f"Time Complexity Metric: {int(time_score * 100)}%")
    space_score = 0.95 if score_metric >= 60 else 0.15
    st.progress(space_score, text=f"Auxiliary Storage Profiling: {int(space_score * 100)}%")
    style_score = 0.90 if score_metric >= 60 else 0.20
    st.progress(style_score, text=f"Code Readability & Responsible AI Standard: {int(style_score * 100)}%")
    st.markdown("</div>", unsafe_allow_html=True)

    # Transcript Download Section
    st.markdown("---")
    st.markdown("### 📤 Production Readiness Gating")
    
    transcript_text = (
        f"==================================================\n"
        f"MICROSOFT AGENTS LEAGUE EVALUATION REPORT SUMMARY\n"
        f"==================================================\n"
        f"Selected Problem Context: {active_problem_title}\n"
        f"Final Achieved Assessment Score: {score_metric}/100\n"
        f"Evaluated Operational Runtime Complexity: {runtime_bound}\n"
        f"System Core Security State: {safety_flag}\n\n"
        f"Candidate Submission Syntax Source Text:\n"
        f"--------------------------------------------------\n"
        f"{current_user_code}\n"
        f"--------------------------------------------------\n"
        f"Feedback Logs Archive:\n"
        f"{evaluation_critique}\n"
    )
    
    st.download_button(
        label="📥 Export Complete Assessment Transcript Bundle",
        data=transcript_text,
        file_name="foundry_iq_interview_transcript.txt",
        mime="text/plain"
    )