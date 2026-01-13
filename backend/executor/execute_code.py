import subprocess
import os

def execute_and_capture_output(filepath):
    """
    Executes the code in `filepath` based on its extension (.js, .rb, .py).
    Captures stdout and stderr.
    """
    extension = os.path.splitext(filepath)[1]
    if extension == ".js":
        command = ["node", filepath]
    elif extension == ".rb":
        command = ["ruby", filepath]
    elif extension == ".py":
        command == ["python", filepath]
    else:
        raise ValueError("Unsupported file type. us .js, .rb, or. py.")
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"output": result.stdout, "error": None}
    except subprocess.CalledProcessError as e:
        return {"output": None, "error": e.stderr}
    