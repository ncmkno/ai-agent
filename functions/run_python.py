import subprocess
import os
from pathlib import Path


def run_python_file(working_directory, file_path):
    """
    Execute a Python file within a specified working directory with security checks.
    
    Args:
        working_directory (str): The directory where execution is permitted
        file_path (str): The path to the Python file to execute
        
    Returns:
        str: The execution result or error message
    """
    try:
        # Convert to Path objects for easier manipulation
        working_dir = Path(working_directory).resolve()
        
        # Join file_path with working_directory and resolve
        full_file_path = (working_dir / file_path).resolve()
        
        # Security check: ensure file is within working directory
        try:
            full_file_path.relative_to(working_dir)
        except ValueError:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # Check if file exists
        if not full_file_path.exists():
            return f'Error: File "{file_path}" not found.'
        
        # Check if file is a Python file
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        
        # Execute the Python file
        result = subprocess.run(
            ['python', str(full_file_path)],
            cwd=str(working_dir),
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Format output
        output_parts = []
        
        if result.stdout:
            output_parts.append(f"STDOUT:\n{result.stdout}")
        
        if result.stderr:
            output_parts.append(f"STDERR:\n{result.stderr}")
        
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        
        if not output_parts:
            return "No output produced."
        
        return '\n'.join(output_parts)
        
    except subprocess.TimeoutExpired:
        return "Error: Python file execution timed out after 30 seconds"
    except Exception as e:
        return f"Error: executing Python file: {e}" 