# Contributing to Nueva Vista Wrapped

Thank you for your interest in contributing to Nueva Vista Wrapped! This project helps people understand their AI collaboration patterns and build a community around thoughtful AI usage.

## 🎯 Project Vision

Nueva Vista Wrapped aims to:
- Provide transparent, privacy-first AI usage analytics
- Build community around meaningful AI collaboration
- Democratize understanding of human-AI interaction patterns
- Maintain the highest standards of data privacy and user control

## 🤝 How to Contribute

### Types of Contributions Welcome

1. **Bug Reports & Feature Requests**
   - Use GitHub Issues with descriptive titles
   - Include steps to reproduce for bugs
   - Provide context for feature requests

2. **Code Contributions**
   - New analysis features
   - Performance improvements
   - Bug fixes
   - Test coverage improvements

3. **Documentation**
   - README improvements
   - Code comments and docstrings
   - Tutorial content
   - Translation support

4. **Community Building**
   - Share your Nueva Vista Wrapped results with #NuevaVistaWrapped
   - Help other users in discussions
   - Provide feedback on user experience

### Development Process

#### 1. Fork & Clone
```bash
git clone https://github.com/yourusername/nueva-vista-wrapped.git
cd nueva-vista-wrapped
```

#### 2. Set Up Development Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r apps/cli/requirements.txt

# Install development dependencies (if added)
pip install pytest black flake8
```

#### 3. Make Changes
- Create a feature branch: `git checkout -b feature/your-feature-name`
- Make your changes following our coding standards
- Test your changes thoroughly
- Update documentation as needed

#### 4. Testing
```bash
# Test with sample data
python apps/cli/nv_quick_hours.py tests/sample_conversations.json
python apps/cli/nv_engagement_score.py tests/sample_conversations.json

# Run any additional tests
python -m pytest tests/ (if test suite exists)
```

#### 5. Submit Pull Request
- Push your branch to your fork
- Create a Pull Request with:
  - Clear description of changes
  - Reference to any related issues
  - Screenshots for UI changes
  - Test results

## 📋 Coding Standards

### Python Code Style
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings for all functions and classes
- Keep functions focused and small
- Use type hints where beneficial

### Example Function Structure
```python
def calculate_engagement_metric(conversations: list, metric_type: str) -> float:
    """
    Calculate specific engagement metrics from conversation data.

    Args:
        conversations: List of conversation dictionaries
        metric_type: Type of metric to calculate ('depth', 'diversity', etc.)

    Returns:
        float: Calculated metric score (0-100)

    Raises:
        ValueError: If metric_type is not supported
    """
    # Implementation here
    pass
```

### Privacy & Security Standards
- **Never collect user data**: All processing must remain local
- **No network calls**: Tools should work completely offline
- **Transparent calculations**: All algorithms must be clearly documented
- **User control**: Users must control all aspects of their data

## 🔒 Privacy Commitment

Any contribution must maintain our core privacy principles:
- 100% local processing
- No data collection or transmission
- No analytics or tracking
- Open source transparency
- User data ownership

## 🧪 Adding New Features

### New Analysis Features
1. Document the metric in `docs/TRANSPARENCY.md`
2. Add calculation method with clear assumptions
3. Include confidence intervals or uncertainty measures
4. Provide sample output format
5. Add to CLI help text

### New Export Format Support
1. Add parser in appropriate location
2. Test with real export files (anonymized)
3. Document supported format versions
4. Handle edge cases gracefully

## 📊 Badge Tier Guidelines

If contributing new badge tiers or categories:
- Tiers should be achievable but meaningful
- Names should be inspiring and inclusive
- Thresholds should be based on research or community feedback
- Include confidence intervals for calculations

## 🌐 Community Guidelines

### Communication
- Be respectful and inclusive
- Assume positive intent
- Provide constructive feedback
- Help newcomers get started

### Sharing Results
- Use #NuevaVistaWrapped hashtag
- Share insights responsibly
- Respect others' privacy choices
- Build positive AI collaboration narratives

## 🐛 Bug Reports

Include in bug reports:
- Operating system and Python version
- Full error message and stack trace
- Sample data (anonymized) that reproduces the issue
- Expected vs actual behavior
- Steps to reproduce

## 💡 Feature Requests

Include in feature requests:
- Clear use case description
- How it fits with privacy principles
- Potential implementation approach
- Expected user impact

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and community chat
- **Nueva Vista Labs**: For partnership or enterprise inquiries

## 🏷️ Release Process

For maintainers:
1. Update version numbers
2. Update CHANGELOG.md
3. Test all features with various export formats
4. Create GitHub release with binaries if applicable
5. Update documentation

## 📝 License

By contributing to Nueva Vista Wrapped, you agree that your contributions will be licensed under the MIT License.

---

**Ready to contribute?** Start by looking at issues labeled `good first issue` or `help wanted`.

Thank you for helping build a more transparent and privacy-respecting AI analytics tool! 🚀
