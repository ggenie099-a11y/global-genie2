"""
GlobalGenie CLI Branding Assets
This module contains branded CLI output functions and ASCII art for terminal display
"""

# Color codes for terminal output
class Colors:
    # Brand colors
    DEEP_BLUE = '\033[38;2;26;54;93m'      # #1a365d
    GOLD = '\033[38;2;214;158;46m'         # #d69e2e
    LIGHT_BLUE = '\033[38;2;49;130;206m'   # #3182ce
    
    # Standard colors
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    
    # Formatting
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'
    UNDERLINE = '\033[4m'

# ASCII Art Logos
LOGO_FULL = f"""{Colors.DEEP_BLUE}
   ██████╗ ██╗      ██████╗ ██████╗  █████╗ ██╗      ██████╗ ███████╗███╗   ██╗██╗███████╗
  ██╔════╝ ██║     ██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝ ██╔════╝████╗  ██║██║██╔════╝
  ██║  ███╗██║     ██║   ██║██████╔╝███████║██║     ██║  ███╗█████╗  ██╔██╗ ██║██║█████╗  
  ██║   ██║██║     ██║   ██║██╔══██╗██╔══██║██║     ██║   ██║██╔══╝  ██║╚██╗██║██║██╔══╝  
  ╚██████╔╝███████╗╚██████╔╝██████╔╝██║  ██║███████╗╚██████╔╝███████╗██║ ╚████║██║███████╗
   ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝╚══════╝{Colors.RESET}"""

LOGO_COMPACT = f"""{Colors.DEEP_BLUE}
  ██████╗  ██████╗ 
 ██╔════╝ ██╔════╝ 
 ██║  ███╗██║  ███╗
 ██║   ██║██║   ██║
 ╚██████╔╝╚██████╔╝
  ╚═════╝  ╚═════╝ {Colors.RESET}
  {Colors.GOLD}GlobalGenie{Colors.RESET}"""

LOGO_MINI = f"{Colors.DEEP_BLUE}◆{Colors.GOLD}GG{Colors.DEEP_BLUE}◆{Colors.RESET}"

# Welcome messages
def get_welcome_message(version="1.7.6"):
    return f"""{LOGO_COMPACT}
   {Colors.GOLD}The Complete AI Agent Framework{Colors.RESET}
   {Colors.DIM}Version {version}{Colors.RESET}
"""

def get_cli_header():
    return f"""{Colors.DEEP_BLUE}╭─────────────────────────────────────────────╮
│{Colors.RESET}  {LOGO_MINI} {Colors.BOLD}GlobalGenie CLI{Colors.RESET}                    {Colors.DEEP_BLUE}│
│{Colors.RESET}  {Colors.DIM}Build intelligent, autonomous agents{Colors.RESET}     {Colors.DEEP_BLUE}│
╰─────────────────────────────────────────────╯{Colors.RESET}"""

# Status indicators
def success(message):
    return f"{Colors.GREEN}✓{Colors.RESET} {message}"

def error(message):
    return f"{Colors.RED}✗{Colors.RESET} {message}"

def warning(message):
    return f"{Colors.YELLOW}⚠{Colors.RESET} {message}"

def info(message):
    return f"{Colors.LIGHT_BLUE}ℹ{Colors.RESET} {message}"

def step(number, message):
    return f"{Colors.GOLD}{number}.{Colors.RESET} {message}"

# Progress indicators
def progress_bar(current, total, width=40):
    filled = int(width * current / total)
    bar = '█' * filled + '░' * (width - filled)
    percentage = int(100 * current / total)
    return f"{Colors.DEEP_BLUE}[{Colors.GOLD}{bar}{Colors.DEEP_BLUE}]{Colors.RESET} {percentage}%"

# Command examples
COMMAND_EXAMPLES = f"""
{Colors.BOLD}Quick Start Commands:{Colors.RESET}

  {Colors.GOLD}gg init{Colors.RESET}                    Initialize a new GlobalGenie project
  {Colors.GOLD}gg ws create{Colors.RESET}              Create a new workspace
  {Colors.GOLD}gg ws up{Colors.RESET}                  Start your workspace
  {Colors.GOLD}gg agent create{Colors.RESET}           Create a new AI agent
  {Colors.GOLD}gg --help{Colors.RESET}                 Show detailed help information

{Colors.BOLD}Learn More:{Colors.RESET}
  {Colors.DIM}Documentation:{Colors.RESET} https://docs.globalgenie.com
  {Colors.DIM}Examples:{Colors.RESET}      https://docs.globalgenie.com/examples
  {Colors.DIM}Community:{Colors.RESET}     https://discord.gg/globalgenie
"""

# Installation success message
def installation_success():
    return f"""
{success("GlobalGenie installed successfully!")}

{Colors.BOLD}Next Steps:{Colors.RESET}
{step(1, "Initialize your first project:")} {Colors.GOLD}gg init{Colors.RESET}
{step(2, "Create a workspace:")} {Colors.GOLD}gg ws create{Colors.RESET}
{step(3, "Start building agents:")} {Colors.GOLD}gg agent create{Colors.RESET}

{Colors.DIM}Need help? Visit https://docs.globalgenie.com{Colors.RESET}
"""

# Error messages
def command_not_found(command):
    return f"""
{error(f"Command '{command}' not found")}

{Colors.BOLD}Available commands:{Colors.RESET}
  {Colors.GOLD}init{Colors.RESET}      Initialize a new project
  {Colors.GOLD}ws{Colors.RESET}        Workspace management
  {Colors.GOLD}agent{Colors.RESET}     Agent operations
  {Colors.GOLD}config{Colors.RESET}    Configuration management
  {Colors.GOLD}help{Colors.RESET}      Show help information

{Colors.DIM}Run {Colors.GOLD}gg --help{Colors.DIM} for detailed information{Colors.RESET}
"""

# Loading animations
def loading_spinner(text="Loading"):
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    return f"{Colors.LIGHT_BLUE}{{frame}}{Colors.RESET} {text}..."

# Configuration display
def config_display(config_dict):
    output = f"\n{Colors.BOLD}Current Configuration:{Colors.RESET}\n"
    for key, value in config_dict.items():
        if value:
            output += f"  {Colors.GOLD}{key}:{Colors.RESET} {value}\n"
        else:
            output += f"  {Colors.GOLD}{key}:{Colors.RESET} {Colors.DIM}(not set){Colors.RESET}\n"
    return output

# Agent status display
def agent_status(name, status, model=None, tools=None):
    status_color = Colors.GREEN if status == "running" else Colors.YELLOW if status == "idle" else Colors.RED
    status_icon = "●" if status == "running" else "○" if status == "idle" else "✗"
    
    output = f"\n{Colors.BOLD}Agent: {Colors.GOLD}{name}{Colors.RESET}\n"
    output += f"  Status: {status_color}{status_icon} {status}{Colors.RESET}\n"
    
    if model:
        output += f"  Model:  {Colors.LIGHT_BLUE}{model}{Colors.RESET}\n"
    
    if tools:
        output += f"  Tools:  {Colors.DIM}{', '.join(tools)}{Colors.RESET}\n"
    
    return output

# Workspace display
def workspace_display(name, agents_count, status):
    status_color = Colors.GREEN if status == "active" else Colors.YELLOW
    
    return f"""
{Colors.BOLD}Workspace: {Colors.GOLD}{name}{Colors.RESET}
  Status: {status_color}{status}{Colors.RESET}
  Agents: {Colors.LIGHT_BLUE}{agents_count}{Colors.RESET}
"""

# Help sections
HELP_HEADER = f"""
{get_cli_header()}

{Colors.BOLD}GlobalGenie CLI - The Complete AI Agent Framework{Colors.RESET}

Build intelligent, autonomous agents with memory, reasoning, and multi-modal capabilities.
"""

HELP_FOOTER = f"""
{Colors.BOLD}Resources:{Colors.RESET}
  Documentation: {Colors.LIGHT_BLUE}https://docs.globalgenie.com{Colors.RESET}
  Examples:      {Colors.LIGHT_BLUE}https://docs.globalgenie.com/examples{Colors.RESET}
  Community:     {Colors.LIGHT_BLUE}https://discord.gg/globalgenie{Colors.RESET}
  GitHub:        {Colors.LIGHT_BLUE}https://github.com/globalgenie-agi/globalgenie{Colors.RESET}

{Colors.DIM}For more information about a specific command, run: {Colors.GOLD}gg <command> --help{Colors.RESET}
"""

# Version display
def version_display(version, python_version=None, platform=None):
    output = f"\n{LOGO_MINI} {Colors.BOLD}GlobalGenie{Colors.RESET} {Colors.GOLD}v{version}{Colors.RESET}\n"
    
    if python_version:
        output += f"Python: {Colors.LIGHT_BLUE}{python_version}{Colors.RESET}\n"
    
    if platform:
        output += f"Platform: {Colors.DIM}{platform}{Colors.RESET}\n"
    
    output += f"\n{Colors.DIM}The Complete AI Agent Framework{Colors.RESET}\n"
    output += f"{Colors.DIM}https://globalgenie.com{Colors.RESET}\n"
    
    return output

# Table formatting
def format_table(headers, rows, colors=None):
    if not rows:
        return f"{Colors.DIM}No data to display{Colors.RESET}"
    
    # Calculate column widths
    widths = [len(str(header)) for header in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))
    
    # Create header
    header_line = "  ".join(f"{Colors.BOLD}{header:<{widths[i]}}{Colors.RESET}" for i, header in enumerate(headers))
    separator = "  ".join("─" * width for width in widths)
    
    # Create rows
    table_rows = []
    for row in rows:
        formatted_row = []
        for i, cell in enumerate(row):
            if colors and i < len(colors) and colors[i]:
                formatted_row.append(f"{colors[i]}{cell:<{widths[i]}}{Colors.RESET}")
            else:
                formatted_row.append(f"{cell:<{widths[i]}}")
        table_rows.append("  ".join(formatted_row))
    
    return f"{header_line}\n{separator}\n" + "\n".join(table_rows)

# Usage examples for different commands
USAGE_EXAMPLES = {
    "init": f"""
{Colors.BOLD}Examples:{Colors.RESET}
  {Colors.GOLD}gg init{Colors.RESET}                    Initialize in current directory
  {Colors.GOLD}gg init my-project{Colors.RESET}         Initialize in new directory
  {Colors.GOLD}gg init --template basic{Colors.RESET}   Use a specific template
""",
    
    "agent": f"""
{Colors.BOLD}Examples:{Colors.RESET}
  {Colors.GOLD}gg agent create{Colors.RESET}            Create a new agent interactively
  {Colors.GOLD}gg agent list{Colors.RESET}              List all agents
  {Colors.GOLD}gg agent run my-agent{Colors.RESET}      Run a specific agent
  {Colors.GOLD}gg agent delete my-agent{Colors.RESET}   Delete an agent
""",
    
    "ws": f"""
{Colors.BOLD}Examples:{Colors.RESET}
  {Colors.GOLD}gg ws create{Colors.RESET}               Create a new workspace
  {Colors.GOLD}gg ws up{Colors.RESET}                   Start the workspace
  {Colors.GOLD}gg ws down{Colors.RESET}                 Stop the workspace
  {Colors.GOLD}gg ws status{Colors.RESET}               Show workspace status
"""
}

# Export all functions and constants for use in CLI
__all__ = [
    'Colors', 'LOGO_FULL', 'LOGO_COMPACT', 'LOGO_MINI',
    'get_welcome_message', 'get_cli_header', 'success', 'error', 'warning', 'info', 'step',
    'progress_bar', 'COMMAND_EXAMPLES', 'installation_success', 'command_not_found',
    'loading_spinner', 'config_display', 'agent_status', 'workspace_display',
    'HELP_HEADER', 'HELP_FOOTER', 'version_display', 'format_table', 'USAGE_EXAMPLES'
]