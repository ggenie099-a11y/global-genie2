CUSTOM_CSS = """
<style>
/* GlobalGenie Brand Typography */
.heading {
    text-align: center;
    background: linear-gradient(45deg, #1a365d, #d69e2e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 2.5em;
    font-weight: bold;
    margin-bottom: 0.5em;
}

.subheading {
    text-align: center;
    font-weight: 600;
    color: #666;
    font-size: 1.2em;
    margin-bottom: 2em;
}

/* GlobalGenie Brand Links */
a {
    text-decoration: underline;
    color: #1a365d;
    transition: color 0.3s ease;
}

a:hover {
    color: #d69e2e;
}

/* GlobalGenie Brand Buttons and Components */
.stButton > button {
    background: linear-gradient(45deg, #1a365d, #2d5a87);
    color: white;
    border: none;
    border-radius: 8px;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background: linear-gradient(45deg, #d69e2e, #e6b84a);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(214, 158, 46, 0.3);
}

/* GlobalGenie Brand Sidebar */
.css-1d391kg {
    background-color: #f8f9fa;
}

/* GlobalGenie Brand Expanders */
.streamlit-expanderHeader {
    background-color: #1a365d;
    color: white;
}

/* GlobalGenie Brand Success/Info Messages */
.stSuccess {
    background-color: rgba(214, 158, 46, 0.1);
    border-left: 4px solid #d69e2e;
}

.stInfo {
    background-color: rgba(26, 54, 93, 0.1);
    border-left: 4px solid #1a365d;
}
</style>
"""
