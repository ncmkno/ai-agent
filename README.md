# AI Agent

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

## Author

[@ncmkno](https://github.com/ncmkno) 