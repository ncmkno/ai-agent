import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Import our custom functions
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python import run_python_file
from functions.write_file_content import write_file

# Check if prompt is provided as command line argument
if len(sys.argv) < 2:
    print("Error: Please provide a prompt as a command line argument.")
    print("Usage: python3 main.py \"Your prompt here\" [--verbose]")
    sys.exit(1)

# Get the prompt from command line arguments
user_prompt = sys.argv[1]

# Check if verbose flag is provided
verbose = "--verbose" in sys.argv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# Function declaration schema for get_files_info
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

# Function declaration schema for get_file_content
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the content of a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)

# Function declaration schema for run_python_file
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory with optional arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)

# Function declaration schema for write_file
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file, creating it if it doesn't exist or overwriting if it does.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)

# Create tool with available functions
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

# System prompt
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, you can use the available functions to investigate, analyze, and modify code. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

Continue using these tools until you have enough information to provide a complete and helpful response to the user's request. When you're finished with your investigation and have completed the task, provide your final response without calling any more functions.

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

# Print user prompt if verbose
if verbose:
    print(f"User prompt: {user_prompt}")

def call_function(function_call_part, verbose=False):
    """
    Handle the abstract task of calling one of our four functions.
    
    Args:
        function_call_part: A types.FunctionCall with .name and .args properties
        verbose: Whether to print detailed output
        
    Returns:
        types.Content with function response
    """
    function_name = function_call_part.name
    function_args = dict(function_call_part.args)  # Copy the args dict
    
    # Add working directory to the args
    function_args["working_directory"] = "./calculator"
    
    # Print function call info
    if verbose:
        print(f"Calling function: {function_name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_name}")
    
    # Map function names to actual functions
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }
    
    # Check if function name is valid
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    # Call the function with the arguments
    try:
        function_result = function_map[function_name](**function_args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                )
            ],
        )
    except Exception as e:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Error calling {function_name}: {str(e)}"},
                )
            ],
        )

# Initialize messages with user prompt
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

# Agent loop - iterate at most 20 times
max_iterations = 20
for iteration in range(max_iterations):
    if verbose:
        print(f"\n--- Iteration {iteration + 1} ---")
    
    # Generate response from LLM
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], 
            system_instruction=system_prompt
        ),
    )
    
    function_called = False
    
    # Check if LLM called a function
    if hasattr(response, 'candidates') and response.candidates:
        # Add each candidate's content to the messages
        for candidate in response.candidates:
            if hasattr(candidate, 'content'):
                messages.append(candidate.content)
                
                # Check for function calls in this candidate
                if candidate.content.parts:
                    for part in candidate.content.parts:
                        if hasattr(part, 'function_call') and part.function_call is not None:
                            function_called = True
                            function_call_part = part.function_call
                            function_call_result = call_function(function_call_part, verbose)
                            
                            # Add the function result to messages
                            messages.append(function_call_result)
                            
                            if verbose:
                                response_data = function_call_result.parts[0].function_response.response
                                if "result" in response_data:
                                    print(f"-> {response_data['result']}")
                                elif "error" in response_data:
                                    print(f"-> Error: {response_data['error']}")
    
    # If no function was called, we're done - print final response and break
    if not function_called:
        print("Final response:")
        if hasattr(response, 'candidates') and response.candidates:
            candidate = response.candidates[0]
            if hasattr(candidate, 'content') and candidate.content.parts:
                for part in candidate.content.parts:
                    if hasattr(part, 'text'):
                        print(part.text)
        elif hasattr(response, 'text'):
            print(response.text)
        break
    
    # If this was the last iteration, warn and break
    if iteration == max_iterations - 1:
        print(f"Warning: Reached maximum iterations ({max_iterations}). Agent may not have completed the task.")
        break

# Print token usage information if verbose
if verbose and hasattr(response, 'usage_metadata'):
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    print(f"\nPrompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
elif verbose:
    print("\nToken usage information not available")
