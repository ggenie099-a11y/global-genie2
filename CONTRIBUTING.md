# Contributing to GlobalGenie

Thank you for your interest in contributing to GlobalGenie! We welcome contributions from developers of all skill levels. This guide will help you get started with contributing to our AI agent framework.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Setup](#development-setup)
4. [Contributing Guidelines](#contributing-guidelines)
5. [Pull Request Process](#pull-request-process)
6. [Issue Reporting](#issue-reporting)
7. [Community](#community)

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

## Getting Started

### Ways to Contribute

- **🐛 Bug Reports**: Help us identify and fix issues
- **💡 Feature Requests**: Suggest new capabilities and improvements
- **📝 Documentation**: Improve guides, tutorials, and API documentation
- **💻 Code Contributions**: Fix bugs, implement features, optimize performance
- **🧪 Testing**: Write tests, improve test coverage, test new features
- **🎨 Examples**: Create tutorials and real-world usage examples
- **🌍 Community**: Help other users, answer questions, share knowledge

### Before You Start

1. **Check existing issues** - Look for similar bug reports or feature requests
2. **Read the documentation** - Familiarize yourself with GlobalGenie's architecture
3. **Join our community** - Connect with other contributors on [Discord](https://discord.gg/globalgenie)
4. **Start small** - Begin with good first issues or documentation improvements

## Development Setup

### Prerequisites

- **Python 3.8+** (Python 3.9+ recommended)
- **Git** for version control
- **Virtual environment** (venv, conda, or similar)

### Local Development Environment

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/your-username/globalgenie.git
   cd globalgenie
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv globalgenie_dev
   source globalgenie_dev/bin/activate  # On Windows: globalgenie_dev\Scripts\activate
   ```

3. **Install development dependencies:**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Install pre-commit hooks:**
   ```bash
   pre-commit install
   ```

5. **Verify installation:**
   ```bash
   python -c "import globalgenie; print('GlobalGenie development setup complete!')"
   ```

### Development Dependencies

The development environment includes:

- **Testing**: `pytest`, `pytest-cov`, `pytest-asyncio`
- **Code Quality**: `black`, `isort`, `flake8`, `mypy`
- **Documentation**: `sphinx`, `sphinx-rtd-theme`
- **Pre-commit**: `pre-commit` for automated code quality checks

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=globalgenie --cov-report=html

# Run specific test file
pytest tests/test_agent.py

# Run tests matching a pattern
pytest -k "test_agent_creation"
```

### Code Quality Checks

```bash
# Format code
black .
isort .

# Check code style
flake8 globalgenie tests

# Type checking
mypy globalgenie

# Run all quality checks
pre-commit run --all-files
```

## Contributing Guidelines

### Code Style

We follow Python best practices and use automated tools to maintain code quality:

- **Formatting**: Black with 88-character line length
- **Import sorting**: isort with Black-compatible settings
- **Linting**: flake8 with custom configuration
- **Type hints**: mypy for static type checking

### Coding Standards

1. **Write clear, readable code** with descriptive variable and function names
2. **Add type hints** to all public functions and methods
3. **Include docstrings** for all public classes and functions
4. **Follow PEP 8** style guidelines (enforced by our tools)
5. **Write tests** for new functionality and bug fixes
6. **Keep functions focused** - each function should do one thing well

### Documentation Standards

- **Docstrings**: Use Google-style docstrings for consistency
- **Comments**: Explain complex logic and business decisions
- **README updates**: Update relevant documentation for new features
- **Examples**: Include practical examples for new functionality

Example docstring format:
```python
def create_agent(model: str, tools: List[Tool]) -> Agent:
    """Create a new GlobalGenie agent with specified model and tools.
    
    Args:
        model: The AI model identifier (e.g., "gpt-4", "claude-3-sonnet")
        tools: List of tools to equip the agent with
        
    Returns:
        Configured Agent instance ready for use
        
    Raises:
        ValueError: If model is not supported
        ConfigurationError: If tools configuration is invalid
        
    Example:
        >>> from globalgenie.agent import Agent
        >>> from globalgenie.models.openai import OpenAIChat
        >>> from globalgenie.tools.web import WebSearchTools
        >>> 
        >>> agent = create_agent(
        ...     model=OpenAIChat(id="gpt-4"),
        ...     tools=[WebSearchTools()]
        ... )
    """
```

### Testing Guidelines

1. **Write tests for all new functionality**
2. **Maintain high test coverage** (aim for >90%)
3. **Use descriptive test names** that explain what is being tested
4. **Test both success and failure cases**
5. **Mock external dependencies** (API calls, file system, etc.)
6. **Write integration tests** for complex workflows

Test structure example:
```python
import pytest
from unittest.mock import Mock, patch
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat

class TestAgent:
    """Test suite for Agent class."""
    
    def test_agent_creation_with_valid_model(self):
        """Test that agent can be created with valid model."""
        model = OpenAIChat(id="gpt-4")
        agent = Agent(model=model)
        
        assert agent.model == model
        assert agent.tools == []
        assert agent.memory is None
    
    def test_agent_run_with_simple_query(self):
        """Test agent can process simple text query."""
        with patch('globalgenie.models.openai.OpenAIChat.generate') as mock_generate:
            mock_generate.return_value = "Hello! How can I help you?"
            
            agent = Agent(model=OpenAIChat(id="gpt-4"))
            response = agent.run("Hello")
            
            assert response.content == "Hello! How can I help you?"
            mock_generate.assert_called_once()
```

## Pull Request Process

### Before Submitting

1. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our coding standards

3. **Write or update tests** for your changes

4. **Run the test suite** and ensure all tests pass:
   ```bash
   pytest
   ```

5. **Run code quality checks**:
   ```bash
   pre-commit run --all-files
   ```

6. **Update documentation** if needed

7. **Commit your changes** with clear, descriptive messages:
   ```bash
   git commit -m "feat: add support for custom tool validation
   
   - Add validation framework for custom tools
   - Include comprehensive error messages
   - Add tests for validation edge cases
   - Update documentation with validation examples"
   ```

### Commit Message Format

We use conventional commits for clear change tracking:

- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `test:` Test additions or modifications
- `refactor:` Code refactoring without functionality changes
- `perf:` Performance improvements
- `chore:` Maintenance tasks

### Submitting Your Pull Request

1. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a pull request** on GitHub with:
   - **Clear title** describing the change
   - **Detailed description** explaining what and why
   - **Link to related issues** if applicable
   - **Screenshots or examples** for UI/UX changes

3. **Fill out the PR template** completely

4. **Request review** from maintainers

### Pull Request Template

```markdown
## Description
Brief description of changes and motivation.

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated (comments, docstrings)
- [ ] Examples and guides updated (if applicable)
- [ ] Tested in clean environment
```

### Review Process

1. **Automated checks** must pass (tests, linting, type checking)
2. **Code review** by at least one maintainer
3. **Discussion and iteration** if changes are requested
4. **Approval and merge** once all requirements are met

## Issue Reporting

### Bug Reports

When reporting bugs, please include:

1. **Clear title** summarizing the issue
2. **GlobalGenie version** (`pip show globalgenie`)
3. **Python version** (`python --version`)
4. **Operating system** and version
5. **Minimal code example** that reproduces the issue
6. **Expected behavior** vs actual behavior
7. **Error messages** and stack traces
8. **Additional context** that might be relevant

Use this template:

```markdown
**Bug Description**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Create agent with '...'
2. Run query '...'
3. See error

**Expected Behavior**
What you expected to happen.

**Actual Behavior**
What actually happened.

**Environment**
- GlobalGenie version: 
- Python version: 
- OS: 

**Code Example**
```python
# Minimal code that reproduces the issue
from globalgenie.agent import Agent
# ... rest of code
```

**Error Message**
```
Full error traceback here
```
```

### Feature Requests

For feature requests, please include:

1. **Clear description** of the proposed feature
2. **Use case** - why is this feature needed?
3. **Proposed solution** - how should it work?
4. **Alternatives considered** - other approaches you've thought about
5. **Additional context** - mockups, examples, references

## Community

### Getting Help

- **📖 [Documentation](https://docs.globalgenie.com)** - Comprehensive guides and API reference
- **💬 [Discord Community](https://discord.gg/globalgenie)** - Real-time chat with other developers
- **🐛 [GitHub Issues](https://github.com/globalgenie-agi/globalgenie/issues)** - Bug reports and feature requests
- **📧 [Email Support](mailto:support@globalgenie.com)** - Direct support from our team

### Community Guidelines

- **Be respectful** and inclusive in all interactions
- **Help others** when you can - we all started somewhere
- **Share knowledge** - write blog posts, create tutorials, give talks
- **Provide constructive feedback** in code reviews and discussions
- **Follow our Code of Conduct** in all community spaces

### Recognition

We appreciate all contributions! Contributors are recognized through:

- **Contributors list** in our README
- **Release notes** mentioning significant contributions
- **Community highlights** in our newsletter and blog
- **Swag and rewards** for significant contributions
- **Speaking opportunities** at conferences and meetups

## Development Workflow

### Branch Strategy

- **`main`** - Stable release branch
- **`develop`** - Integration branch for new features
- **`feature/*`** - Feature development branches
- **`fix/*`** - Bug fix branches
- **`docs/*`** - Documentation update branches

### Release Process

1. **Feature freeze** on develop branch
2. **Release candidate** testing
3. **Final testing** and bug fixes
4. **Merge to main** and tag release
5. **Deploy to PyPI** and update documentation
6. **Announce release** to community

### Versioning

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality additions
- **PATCH** version for backwards-compatible bug fixes

## Advanced Contributing

### Architecture Overview

Understanding GlobalGenie's architecture helps with contributions:

```
globalgenie/
├── agent/          # Core agent implementation
├── models/         # AI model integrations
├── tools/          # Tool implementations
├── memory/         # Memory systems
├── knowledge/      # Knowledge base systems
├── team/           # Multi-agent coordination
├── utils/          # Utility functions
└── config/         # Configuration management
```

### Adding New Model Support

To add support for a new AI model provider:

1. **Create model class** in `globalgenie/models/your_provider/`
2. **Implement base model interface**
3. **Add configuration options**
4. **Write comprehensive tests**
5. **Update documentation** and examples
6. **Add to model registry**

### Creating New Tools

To create a new tool:

1. **Inherit from base Tool class**
2. **Implement required methods**
3. **Add proper error handling**
4. **Write unit and integration tests**
5. **Document usage and examples**
6. **Consider security implications**

### Performance Optimization

When optimizing performance:

1. **Profile before optimizing** - measure actual bottlenecks
2. **Consider async alternatives** for I/O bound operations
3. **Implement caching** where appropriate
4. **Optimize database queries** and memory usage
5. **Add performance tests** to prevent regressions

## Questions?

If you have questions about contributing that aren't covered here:

1. **Check our [FAQ](TROUBLESHOOTING.md#frequently-asked-questions)**
2. **Search existing [GitHub issues](https://github.com/globalgenie-agi/globalgenie/issues)**
3. **Ask in our [Discord community](https://discord.gg/globalgenie)**
4. **Email us** at [contributors@globalgenie.com](mailto:contributors@globalgenie.com)

Thank you for contributing to GlobalGenie! Your efforts help make AI agents more accessible and powerful for developers worldwide. 🚀