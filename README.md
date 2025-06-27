# AI Agent

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/ncmkno/ai-agent)
![GitHub last commit](https://img.shields.io/github/last-commit/ncmkno/ai-agent)
![GitHub stars](https://img.shields.io/github/stars/ncmkno/ai-agent)
![GitHub forks](https://img.shields.io/github/forks/ncmkno/ai-agent)
![GitHub issues](https://img.shields.io/github/issues/ncmkno/ai-agent)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

A Python-based AI agent with calculator functionality and file operations capabilities.

## Features

- **Calculator Module**: Comprehensive mathematical operations
- **File Operations**: Read, write, and manage file content
- **Python Code Execution**: Dynamic Python code execution capabilities
- **Modular Design**: Clean, well-organized code structure

## Project Structure

```
ai-agent/
├── calculator/                 # Calculator module
│   ├── main.py                # Calculator main interface
│   ├── pkg/
│   │   ├── calculator.py      # Core calculation logic
│   │   └── render.py          # Display/rendering utilities
│   ├── tests.py               # Calculator tests
│   └── wrapper.py             # Calculator wrapper functions
├── functions/                  # Core agent functions
│   ├── get_file_content.py    # File reading operations
│   ├── get_files_info.py      # File system information
│   ├── run_python.py          # Python execution engine
│   └── write_file_content.py  # File writing operations
├── main.py                     # Main agent entry point
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
└── tests.py                   # Main test suite
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ncmkno/ai-agent.git
cd ai-agent
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Main Agent
```bash
python main.py
```

### Calculator Module
```bash
cd calculator
python main.py
```

### Running Tests
```bash
python tests.py
```

## Features Overview

### Calculator
- Basic arithmetic operations
- Advanced mathematical functions
- Error handling and validation

### File Operations
- Read file contents
- Write to files
- Get file system information
- Safe file handling

### Python Execution
- Execute Python code dynamically
- Secure execution environment
- Result handling and error management

## Development

This project follows Python best practices:
- Modular design with clear separation of concerns
- Comprehensive error handling
- Clean code principles (DRY, YAGNI)
- Type hints where applicable

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is available for educational and personal use.

## About the Developer

This project was built by **Noel Malonzo** ([@ncmkno](https://github.com/ncmkno)) as part of the Boot.dev learning journey.

### Boot.dev Profile: [mushypermit51](https://www.boot.dev/u/mushypermit51)

**Learning Stats:**
- 🎯 **Level 64** with 1,472 XP
- 📚 **604 lessons solved**
- 🏆 **Leaderboard rank:** 7,772
- 📅 **Boot.dev member since:** January 9, 2025

**Completed Courses:**
- ✅ Learn to Code in Python (Jan 21, 2025)
- ✅ Learn Object Oriented Programming in Python (Jan 29, 2025)
- ✅ Learn Linux (Jan 26, 2025)
- ✅ Learn Kubernetes (Mar 14, 2025)
- ✅ Learn Git (Jan 26, 2025)
- ✅ Learn Docker (Feb 16, 2025)

**Project Portfolio:**
- 🤖 **Build an AI Agent in Python** (Jun 27, 2025) - *This project*
- 📖 **Build a Bookbot in Python** (Jan 26, 2025)
- 🚀 **Build Asteroids using Python and Pygame** (Jan 29, 2025)

**Notable Achievements:**
- 🎯 **Sharpshooter Grandmaster** - Complete 28 sharpshooter sprees
- 🏅 **Master Milestone** - Complete 480 exercises
- 🔥 **Platinum Streak** - Study consistently for 34 days
- 👥 **Bronze Fellowship** - Earn karma in the Discord community

### Connect
- 💼 [LinkedIn](https://linkedin.com/in/noel-malonzo/)
- 🐙 [GitHub](https://github.com/ncmkno)
- 🎓 [Boot.dev Profile](https://www.boot.dev/u/mushypermit51) 