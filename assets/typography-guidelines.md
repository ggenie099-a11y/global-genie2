# GlobalGenie Typography Guidelines

## Font Stack

### Primary Typeface: Inter
**Usage**: All body text, UI elements, documentation
**Fallback**: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif
**Characteristics**: Clean, modern, highly readable, optimized for screens
**License**: Open Font License (free for commercial use)

### Code Typeface: JetBrains Mono
**Usage**: Code blocks, terminal output, technical examples
**Fallback**: "SF Mono", Monaco, "Cascadia Code", "Roboto Mono", "Courier New", monospace
**Characteristics**: Developer-friendly, excellent readability, ligature support
**License**: Apache 2.0 (free for commercial use)

## Typography Scale

### Headings
- **H1**: 2.5rem (40px) - Bold (700) - Deep Blue (#1a365d)
- **H2**: 2rem (32px) - Semibold (600) - Deep Blue (#1a365d)
- **H3**: 1.5rem (24px) - Semibold (600) - Deep Blue (#1a365d)
- **H4**: 1.25rem (20px) - Medium (500) - Deep Blue (#1a365d)
- **H5**: 1.125rem (18px) - Medium (500) - Dark Gray (#2d3748)
- **H6**: 1rem (16px) - Medium (500) - Dark Gray (#2d3748)

### Body Text
- **Large**: 1.125rem (18px) - Regular (400) - Dark Gray (#2d3748)
- **Base**: 1rem (16px) - Regular (400) - Dark Gray (#2d3748)
- **Small**: 0.875rem (14px) - Regular (400) - Medium Gray (#718096)
- **Extra Small**: 0.75rem (12px) - Regular (400) - Medium Gray (#718096)

### Code Text
- **Inline Code**: 0.875rem (14px) - Medium (500) - Gold (#d69e2e)
- **Code Block**: 0.875rem (14px) - Regular (400) - Light Gray (#f7fafc)

## Line Heights
- **Headings**: 1.2 (tight)
- **Body Text**: 1.6 (relaxed)
- **Code**: 1.4 (normal)
- **UI Elements**: 1.5 (normal)

## Font Weights
- **Light**: 300 (rarely used)
- **Regular**: 400 (body text)
- **Medium**: 500 (emphasis, UI elements)
- **Semibold**: 600 (subheadings)
- **Bold**: 700 (main headings, strong emphasis)

## CSS Implementation

### CSS Custom Properties
```css
:root {
  /* Font Families */
  --gg-font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --gg-font-mono: 'JetBrains Mono', 'SF Mono', Monaco, 'Cascadia Code', monospace;
  
  /* Font Sizes */
  --gg-text-xs: 0.75rem;    /* 12px */
  --gg-text-sm: 0.875rem;   /* 14px */
  --gg-text-base: 1rem;     /* 16px */
  --gg-text-lg: 1.125rem;   /* 18px */
  --gg-text-xl: 1.25rem;    /* 20px */
  --gg-text-2xl: 1.5rem;    /* 24px */
  --gg-text-3xl: 2rem;      /* 32px */
  --gg-text-4xl: 2.5rem;    /* 40px */
  
  /* Line Heights */
  --gg-leading-tight: 1.2;
  --gg-leading-normal: 1.4;
  --gg-leading-relaxed: 1.6;
  
  /* Font Weights */
  --gg-font-light: 300;
  --gg-font-normal: 400;
  --gg-font-medium: 500;
  --gg-font-semibold: 600;
  --gg-font-bold: 700;
}
```

### Base Styles
```css
body {
  font-family: var(--gg-font-sans);
  font-size: var(--gg-text-base);
  line-height: var(--gg-leading-relaxed);
  color: var(--gg-text-primary);
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--gg-font-sans);
  line-height: var(--gg-leading-tight);
  color: var(--gg-primary-blue);
  margin-bottom: 0.5em;
}

code {
  font-family: var(--gg-font-mono);
  font-size: var(--gg-text-sm);
  color: var(--gg-accent-gold);
  background-color: var(--gg-bg-secondary);
  padding: 0.125rem 0.25rem;
  border-radius: 0.25rem;
}

pre {
  font-family: var(--gg-font-mono);
  font-size: var(--gg-text-sm);
  line-height: var(--gg-leading-normal);
  background-color: var(--gg-dark-navy);
  color: var(--gg-light-gray);
  padding: 1rem;
  border-radius: 0.5rem;
  overflow-x: auto;
}
```

## Usage Examples

### Documentation Headers
```markdown
# GlobalGenie Documentation
## Getting Started Guide
### Installation Instructions
#### Prerequisites
```

### Code Examples
```python
from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4"),
    instructions="You are a helpful assistant."
)
```

### UI Components
```html
<button class="gg-button-primary">Get Started</button>
<p class="gg-text-secondary">Learn more about GlobalGenie</p>
<code class="gg-code-inline">pip install globalgenie</code>
```

## Accessibility Guidelines

### Contrast Ratios
- **Normal text**: Minimum 4.5:1 contrast ratio
- **Large text** (18px+ or 14px+ bold): Minimum 3:1 contrast ratio
- **UI components**: Minimum 3:1 contrast ratio

### Font Size Guidelines
- **Minimum body text**: 16px (1rem)
- **Minimum UI text**: 14px (0.875rem)
- **Maximum line length**: 75 characters for optimal readability

### Responsive Typography
```css
/* Mobile First */
h1 { font-size: 2rem; }
h2 { font-size: 1.75rem; }

/* Tablet and up */
@media (min-width: 768px) {
  h1 { font-size: 2.25rem; }
  h2 { font-size: 2rem; }
}

/* Desktop and up */
@media (min-width: 1024px) {
  h1 { font-size: 2.5rem; }
  h2 { font-size: 2rem; }
}
```

## Brand Voice in Typography

### Tone Indicators
- **Professional**: Use semibold weights for authority
- **Friendly**: Use regular weights with good spacing
- **Technical**: Use monospace fonts for code
- **Urgent**: Use bold weights sparingly for emphasis

### Hierarchy Best Practices
1. **One H1 per page** - Main page title
2. **Logical nesting** - Don't skip heading levels
3. **Consistent spacing** - Use consistent margins
4. **Scannable content** - Break up long text blocks
5. **Clear labels** - Descriptive headings and subheadings