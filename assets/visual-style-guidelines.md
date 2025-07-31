# GlobalGenie Visual Style Guidelines

## Design Principles

### 1. Professional Excellence
- Clean, modern aesthetics that inspire confidence
- Consistent visual hierarchy and spacing
- High-quality imagery and graphics
- Attention to detail in all visual elements

### 2. Global Accessibility
- Universal design patterns and symbols
- High contrast ratios for readability
- Scalable designs that work across cultures
- Inclusive color choices and imagery

### 3. Tech-Forward Innovation
- Modern UI patterns and interactions
- Cutting-edge visual treatments
- Progressive enhancement approach
- Future-proof design systems

### 4. Developer-Centric
- Code-friendly visual elements
- Terminal and CLI optimized designs
- Documentation-first approach
- Tool-focused user experience

## Layout System

### Grid Structure
- **Base unit**: 8px grid system
- **Columns**: 12-column responsive grid
- **Gutters**: 24px on desktop, 16px on mobile
- **Margins**: 32px on desktop, 16px on mobile
- **Max width**: 1200px for content areas

### Spacing Scale
```css
--gg-space-1: 0.25rem;  /* 4px */
--gg-space-2: 0.5rem;   /* 8px */
--gg-space-3: 0.75rem;  /* 12px */
--gg-space-4: 1rem;     /* 16px */
--gg-space-5: 1.25rem;  /* 20px */
--gg-space-6: 1.5rem;   /* 24px */
--gg-space-8: 2rem;     /* 32px */
--gg-space-10: 2.5rem;  /* 40px */
--gg-space-12: 3rem;    /* 48px */
--gg-space-16: 4rem;    /* 64px */
--gg-space-20: 5rem;    /* 80px */
```

## Component Styles

### Buttons
```css
/* Primary Button */
.gg-button-primary {
  background: var(--gg-primary-blue);
  color: var(--gg-white);
  border: 2px solid var(--gg-primary-blue);
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.2s ease;
}

.gg-button-primary:hover {
  background: var(--gg-accent-gold);
  border-color: var(--gg-accent-gold);
  color: var(--gg-dark-navy);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(214, 158, 46, 0.3);
}

/* Secondary Button */
.gg-button-secondary {
  background: transparent;
  color: var(--gg-primary-blue);
  border: 2px solid var(--gg-primary-blue);
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.2s ease;
}

.gg-button-secondary:hover {
  background: var(--gg-primary-blue);
  color: var(--gg-white);
}
```

### Cards
```css
.gg-card {
  background: var(--gg-white);
  border: 1px solid var(--gg-border-light);
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(26, 54, 93, 0.08);
  transition: all 0.2s ease;
}

.gg-card:hover {
  box-shadow: 0 8px 24px rgba(26, 54, 93, 0.12);
  transform: translateY(-2px);
}

.gg-card-header {
  border-bottom: 1px solid var(--gg-border-light);
  padding-bottom: 16px;
  margin-bottom: 16px;
}

.gg-card-title {
  color: var(--gg-primary-blue);
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0;
}
```

### Code Blocks
```css
.gg-code-block {
  background: var(--gg-dark-navy);
  color: var(--gg-light-gray);
  border-radius: 8px;
  padding: 20px;
  font-family: var(--gg-font-mono);
  font-size: 14px;
  line-height: 1.5;
  overflow-x: auto;
  position: relative;
}

.gg-code-block::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--gg-accent-gold), var(--gg-primary-blue));
}

.gg-code-inline {
  background: var(--gg-soft-gold);
  color: var(--gg-accent-gold);
  padding: 2px 6px;
  border-radius: 4px;
  font-family: var(--gg-font-mono);
  font-size: 0.875em;
  font-weight: 500;
}
```

### Navigation
```css
.gg-nav {
  background: var(--gg-white);
  border-bottom: 1px solid var(--gg-border-light);
  padding: 16px 0;
}

.gg-nav-link {
  color: var(--gg-text-secondary);
  text-decoration: none;
  padding: 8px 16px;
  border-radius: 6px;
  font-weight: 500;
  transition: all 0.2s ease;
}

.gg-nav-link:hover {
  color: var(--gg-primary-blue);
  background: var(--gg-soft-gold);
}

.gg-nav-link.active {
  color: var(--gg-accent-gold);
  background: rgba(214, 158, 46, 0.1);
}
```

## Icon System

### Icon Style
- **Style**: Outline/stroke-based icons
- **Stroke width**: 2px
- **Corner radius**: 2px for rounded elements
- **Size scale**: 16px, 20px, 24px, 32px, 48px
- **Color**: Inherit from parent or use brand colors

### Common Icons
```
⚙️  Settings/Configuration
🚀  Launch/Deploy
📚  Documentation
🔧  Tools
💡  Ideas/Tips
⚡  Performance/Speed
🌐  Global/Network
🧠  AI/Intelligence
💾  Storage/Memory
🔍  Search
📊  Analytics/Data
✨  Features/New
```

### Icon Usage Guidelines
- Use consistent stroke width across all icons
- Maintain proper spacing around icons (minimum 8px)
- Ensure icons are accessible with proper alt text
- Use brand colors for accent icons
- Keep neutral colors for functional icons

## Imagery Guidelines

### Photography Style
- **Composition**: Clean, modern, professional
- **Color treatment**: Slightly desaturated with blue/gold tints
- **Subject matter**: Technology, developers, global themes
- **Lighting**: Bright, even lighting with soft shadows
- **Background**: Clean, uncluttered backgrounds

### Illustration Style
- **Approach**: Geometric, minimal, vector-based
- **Color palette**: Brand colors with neutral accents
- **Style**: Flat design with subtle depth
- **Consistency**: Unified stroke weights and corner radius
- **Scalability**: Works from small icons to large graphics

### Image Specifications
- **Format**: WebP with PNG fallback
- **Compression**: Optimized for web (< 100KB for most images)
- **Dimensions**: Responsive with multiple sizes
- **Alt text**: Descriptive and meaningful
- **Loading**: Lazy loading for performance

## Animation Guidelines

### Micro-Interactions
```css
/* Hover animations */
.gg-hover-lift {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.gg-hover-lift:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(26, 54, 93, 0.15);
}

/* Loading animations */
.gg-loading {
  animation: gg-pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes gg-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

/* Fade in animation */
.gg-fade-in {
  animation: gg-fadeIn 0.5s ease-out;
}

@keyframes gg-fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
```

### Animation Principles
- **Duration**: 0.2s for micro-interactions, 0.5s for page transitions
- **Easing**: Use ease-out for entrances, ease-in for exits
- **Performance**: Use transform and opacity for smooth animations
- **Accessibility**: Respect prefers-reduced-motion settings
- **Purpose**: Animations should enhance UX, not distract

## Responsive Design

### Breakpoints
```css
/* Mobile first approach */
:root {
  --gg-breakpoint-sm: 640px;   /* Small devices */
  --gg-breakpoint-md: 768px;   /* Medium devices */
  --gg-breakpoint-lg: 1024px;  /* Large devices */
  --gg-breakpoint-xl: 1280px;  /* Extra large devices */
}
```

### Mobile Optimizations
- Touch-friendly button sizes (minimum 44px)
- Simplified navigation patterns
- Optimized typography scales
- Reduced animation complexity
- Faster loading times

### Desktop Enhancements
- Hover states and micro-interactions
- Multi-column layouts
- Advanced navigation patterns
- Rich media content
- Keyboard navigation support

## Accessibility Standards

### Color Accessibility
- **Contrast ratios**: WCAG AA compliant (4.5:1 minimum)
- **Color blindness**: Tested with various color vision deficiencies
- **High contrast mode**: Support for system high contrast settings
- **Dark mode**: Alternative color scheme available

### Interactive Elements
- **Focus indicators**: Clear visual focus states
- **Touch targets**: Minimum 44px for mobile
- **Keyboard navigation**: Full keyboard accessibility
- **Screen readers**: Proper ARIA labels and semantic HTML
- **Motion sensitivity**: Respect prefers-reduced-motion

## Brand Application Examples

### Website Header
```html
<header class="gg-nav">
  <div class="gg-container">
    <div class="gg-nav-brand">
      <img src="/logo.svg" alt="GlobalGenie" class="gg-logo">
    </div>
    <nav class="gg-nav-menu">
      <a href="/docs" class="gg-nav-link">Documentation</a>
      <a href="/examples" class="gg-nav-link">Examples</a>
      <a href="/community" class="gg-nav-link">Community</a>
    </nav>
    <div class="gg-nav-actions">
      <a href="/get-started" class="gg-button-primary">Get Started</a>
    </div>
  </div>
</header>
```

### Feature Card
```html
<div class="gg-card">
  <div class="gg-card-header">
    <h3 class="gg-card-title">🧠 Advanced Reasoning</h3>
  </div>
  <p>Multi-step thinking and problem-solving capabilities that enable your agents to handle complex tasks with sophisticated reasoning patterns.</p>
  <a href="/docs/reasoning" class="gg-button-secondary">Learn More</a>
</div>
```

### Code Example
```html
<div class="gg-code-block">
  <pre><code class="language-python">from globalgenie.agent import Agent
from globalgenie.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4"),
    instructions="You are a helpful assistant."
)</code></pre>
</div>
```

## Quality Assurance

### Design Review Checklist
- [ ] Brand colors used consistently
- [ ] Typography hierarchy followed
- [ ] Proper spacing and alignment
- [ ] Accessibility standards met
- [ ] Responsive design tested
- [ ] Performance optimized
- [ ] Cross-browser compatibility
- [ ] Loading states implemented
- [ ] Error states designed
- [ ] Success states included

### Testing Requirements
- **Visual regression testing**: Automated screenshot comparisons
- **Accessibility testing**: WAVE, axe, and manual testing
- **Performance testing**: Lighthouse scores and Core Web Vitals
- **Cross-browser testing**: Chrome, Firefox, Safari, Edge
- **Device testing**: Mobile, tablet, desktop across various sizes
- **User testing**: Feedback from actual developers and users