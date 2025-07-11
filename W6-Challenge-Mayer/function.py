from rich.console import Console

# Initialise Rich console
console = Console()

# Function that accepts one string argumen (message).
def multiline_input(message):
    # Offer user multi-line input using Rich's console.input. The user types 'END' on a new line to terminate.
    console.print(f"[yellow]{message}[/yellow] (Type [red]'END'[/red] on a new line to finish)")
    # Initialise an empty list: 'lines'
    lines = []
    # Start infinite loop
    while True:
        # Get user input, line-by-line. User text input is captured as string. On <Enter> string is assigned to 'line'.
        line = console.input()
        # If user enters 'END' (or similar), to finish the input, 'break' loop.
        if line.strip().upper() == "END":
            break
        # If not 'END', add 'line' to end of 'lines'
        lines.append(line)
    # After loop 'break', concatenate all strings in `lines` list into a single, large string.
    # Use "\n" as separater between each original line. Return large string. 
    return "\n".join(lines)
    