#!/usr/bin/env python3
"""
GlobalGenie Dashboard - Professional UI Showcase
A comprehensive dashboard demonstrating GlobalGenie's branding and capabilities
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Page configuration with GlobalGenie branding
st.set_page_config(
    page_title="GlobalGenie Dashboard",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded",
)

# GlobalGenie Brand CSS
GLOBALGENIE_CSS = """
<style>
:root {
    --gg-primary: #1a365d;
    --gg-accent: #d69e2e;
    --gg-primary-light: #2d5a87;
    --gg-accent-light: #e6b84a;
    --gg-success: #38a169;
    --gg-warning: #d69e2e;
    --gg-error: #e53e3e;
    --gg-info: #3182ce;
}

/* Main Dashboard Header */
.dashboard-header {
    background: linear-gradient(135deg, var(--gg-primary) 0%, var(--gg-primary-light) 100%);
    padding: 2rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    color: white;
    text-align: center;
}

.dashboard-title {
    font-size: 2.5rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
    background: linear-gradient(45deg, white, var(--gg-accent-light));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.dashboard-subtitle {
    font-size: 1.2rem;
    opacity: 0.9;
}

/* Metric Cards */
.metric-card {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    border-left: 4px solid var(--gg-primary);
    margin-bottom: 1rem;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.metric-value {
    font-size: 2rem;
    font-weight: bold;
    color: var(--gg-primary);
    margin-bottom: 0.5rem;
}

.metric-label {
    color: #666;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.metric-change {
    font-size: 0.8rem;
    margin-top: 0.5rem;
}

.metric-change.positive {
    color: var(--gg-success);
}

.metric-change.negative {
    color: var(--gg-error);
}

/* Status Indicators */
.status-indicator {
    display: inline-block;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    margin-right: 8px;
}

.status-active {
    background-color: var(--gg-success);
}

.status-warning {
    background-color: var(--gg-warning);
}

.status-error {
    background-color: var(--gg-error);
}

/* Feature Cards */
.feature-card {
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid #dee2e6;
    margin-bottom: 1rem;
    transition: all 0.3s ease;
}

.feature-card:hover {
    border-color: var(--gg-accent);
    box-shadow: 0 4px 12px rgba(214, 158, 46, 0.2);
}

.feature-icon {
    font-size: 2rem;
    margin-bottom: 1rem;
}

.feature-title {
    font-size: 1.2rem;
    font-weight: bold;
    color: var(--gg-primary);
    margin-bottom: 0.5rem;
}

.feature-description {
    color: #666;
    line-height: 1.5;
}

/* Navigation */
.nav-item {
    padding: 0.75rem 1rem;
    margin: 0.25rem 0;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.nav-item:hover {
    background-color: rgba(26, 54, 93, 0.1);
    color: var(--gg-primary);
}

.nav-item.active {
    background-color: var(--gg-primary);
    color: white;
}

/* Charts and Visualizations */
.chart-container {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 2rem;
}

.chart-title {
    font-size: 1.3rem;
    font-weight: bold;
    color: var(--gg-primary);
    margin-bottom: 1rem;
}
</style>
"""

st.markdown(GLOBALGENIE_CSS, unsafe_allow_html=True)

def create_sample_data():
    """Create sample data for dashboard visualizations"""
    
    # Agent performance data
    dates = pd.date_range(start=datetime.now() - timedelta(days=30), end=datetime.now(), freq='D')
    agent_data = pd.DataFrame({
        'date': dates,
        'tasks_completed': np.random.randint(50, 200, len(dates)),
        'success_rate': np.random.uniform(0.85, 0.98, len(dates)),
        'response_time': np.random.uniform(0.5, 3.0, len(dates)),
        'active_agents': np.random.randint(5, 25, len(dates))
    })
    
    # Agent types data
    agent_types = pd.DataFrame({
        'type': ['Research Agent', 'Data Analyst', 'Python Agent', 'Calculator', 'Investment Agent'],
        'count': [45, 32, 28, 15, 12],
        'utilization': [0.92, 0.87, 0.94, 0.76, 0.89]
    })
    
    return agent_data, agent_types

def render_dashboard_header():
    """Render the main dashboard header"""
    st.markdown("""
    <div class="dashboard-header">
        <div class="dashboard-title">GlobalGenie Dashboard</div>
        <div class="dashboard-subtitle">Monitor and manage your AI agent ecosystem</div>
    </div>
    """, unsafe_allow_html=True)

def render_metrics_row(agent_data):
    """Render key metrics in a row"""
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">1,247</div>
            <div class="metric-label">Tasks Completed</div>
            <div class="metric-change positive">↗ +12% from last week</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">94.2%</div>
            <div class="metric-label">Success Rate</div>
            <div class="metric-change positive">↗ +2.1% from last week</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">1.8s</div>
            <div class="metric-label">Avg Response Time</div>
            <div class="metric-change negative">↘ +0.3s from last week</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">18</div>
            <div class="metric-label">Active Agents</div>
            <div class="metric-change positive">↗ +3 from last week</div>
        </div>
        """, unsafe_allow_html=True)

def render_performance_chart(agent_data):
    """Render agent performance chart"""
    
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">📈 Agent Performance Trends</div>', unsafe_allow_html=True)
    
    fig = go.Figure()
    
    # Tasks completed
    fig.add_trace(go.Scatter(
        x=agent_data['date'],
        y=agent_data['tasks_completed'],
        mode='lines+markers',
        name='Tasks Completed',
        line=dict(color='#1a365d', width=3),
        marker=dict(size=6)
    ))
    
    # Success rate (scaled for visibility)
    fig.add_trace(go.Scatter(
        x=agent_data['date'],
        y=agent_data['success_rate'] * 100,
        mode='lines+markers',
        name='Success Rate (%)',
        line=dict(color='#d69e2e', width=3),
        marker=dict(size=6),
        yaxis='y2'
    ))
    
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Tasks Completed",
        yaxis2=dict(
            title="Success Rate (%)",
            overlaying='y',
            side='right',
            range=[80, 100]
        ),
        hovermode='x unified',
        showlegend=True,
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_agent_distribution(agent_types):
    """Render agent type distribution"""
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">🤖 Agent Distribution</div>', unsafe_allow_html=True)
        
        fig = px.pie(
            agent_types, 
            values='count', 
            names='type',
            color_discrete_sequence=['#1a365d', '#d69e2e', '#2d5a87', '#e6b84a', '#38a169']
        )
        
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(
            showlegend=True,
            height=300,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">⚡ Agent Utilization</div>', unsafe_allow_html=True)
        
        fig = px.bar(
            agent_types,
            x='utilization',
            y='type',
            orientation='h',
            color='utilization',
            color_continuous_scale=['#e6b84a', '#d69e2e', '#1a365d']
        )
        
        fig.update_layout(
            xaxis_title="Utilization Rate",
            yaxis_title="Agent Type",
            height=300,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

def render_features_grid():
    """Render GlobalGenie features grid"""
    
    st.markdown('<div class="chart-title">🌟 GlobalGenie Features</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <div class="feature-title">Advanced Reasoning</div>
            <div class="feature-description">
                Multi-step thinking and problem-solving capabilities with sophisticated decision-making processes.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🛠️</div>
            <div class="feature-title">Tool Integration</div>
            <div class="feature-description">
                Seamless integration with APIs, databases, and external services for enhanced functionality.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💾</div>
            <div class="feature-title">Persistent Memory</div>
            <div class="feature-description">
                Long-term memory across conversations and sessions with intelligent context retention.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">👥</div>
            <div class="feature-title">Multi-Agent Collaboration</div>
            <div class="feature-description">
                Coordinate multiple agents for complex workflows and distributed problem-solving.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📚</div>
            <div class="feature-title">Knowledge Integration</div>
            <div class="feature-description">
                RAG capabilities with vector databases and intelligent document processing.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Goal-Oriented Behavior</div>
            <div class="feature-description">
                Autonomous task completion with strategic planning and adaptive execution.
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_system_status():
    """Render system status indicators"""
    
    st.markdown('<div class="chart-title">🔧 System Status</div>', unsafe_allow_html=True)
    
    status_items = [
        ("API Gateway", "active", "All endpoints responding normally"),
        ("Database", "active", "Connection stable, 99.9% uptime"),
        ("Agent Pool", "active", "18 agents online and ready"),
        ("Memory System", "warning", "High usage - 85% capacity"),
        ("Tool Services", "active", "All integrations operational"),
    ]
    
    for service, status, description in status_items:
        status_class = f"status-{status}"
        st.markdown(f"""
        <div style="display: flex; align-items: center; padding: 0.75rem; margin: 0.5rem 0; background: white; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <span class="status-indicator {status_class}"></span>
            <div style="flex-grow: 1;">
                <div style="font-weight: bold; color: #1a365d;">{service}</div>
                <div style="font-size: 0.9rem; color: #666;">{description}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def main():
    """Main dashboard application"""
    
    # Render header
    render_dashboard_header()
    
    # Create sample data
    agent_data, agent_types = create_sample_data()
    
    # Sidebar navigation
    with st.sidebar:
        st.markdown("### 🎛️ Dashboard Navigation")
        
        nav_items = [
            ("📊 Overview", "overview"),
            ("🤖 Agents", "agents"),
            ("📈 Analytics", "analytics"),
            ("⚙️ Settings", "settings"),
            ("📚 Documentation", "docs"),
        ]
        
        selected_page = st.radio("Navigate to:", [item[0] for item in nav_items], index=0)
        
        st.markdown("---")
        st.markdown("### 🌟 About GlobalGenie")
        st.markdown("""
        **GlobalGenie** is the complete AI agent framework for building sophisticated, reasoning-capable agents.
        
        🚀 **Quick Links:**
        - [GitHub Repository](https://github.com/globalgenie-agi/globalgenie)
        - [Documentation](https://docs.globalgenie.com)
        - [Community Forum](https://globalgenie.link/community)
        """)
    
    # Main content based on navigation
    if "Overview" in selected_page:
        # Metrics row
        render_metrics_row(agent_data)
        
        # Performance chart
        render_performance_chart(agent_data)
        
        # Agent distribution and utilization
        render_agent_distribution(agent_types)
        
        # Features grid
        render_features_grid()
        
        # System status
        render_system_status()
    
    elif "Agents" in selected_page:
        st.markdown("### 🤖 Agent Management")
        st.info("Agent management interface would be implemented here")
        
    elif "Analytics" in selected_page:
        st.markdown("### 📈 Advanced Analytics")
        st.info("Advanced analytics and reporting would be implemented here")
        
    elif "Settings" in selected_page:
        st.markdown("### ⚙️ System Settings")
        st.info("System configuration interface would be implemented here")
        
    elif "Documentation" in selected_page:
        st.markdown("### 📚 Documentation")
        st.info("Integrated documentation viewer would be implemented here")

if __name__ == "__main__":
    main()