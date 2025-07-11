from InquirerPy import prompt
from project import Project # Import the Project class from my project.py file
# multiline_input requies Console and creates a console. So, also import that console
from function import multiline_input, console
import time
from rich.progress import track

# Create readme.md file, or repurpose to create any file and/or path
file_name = "README_TEST.md"

# Display welcome msg.
console.print("[bold green]Welcome to the EZ Read-Me Doc Generator![/bold green]")
# question: list of dictionaries. I inherited this from week-6 module-11's exercise. 
# Perhaps should have gone strait to creating and populating a Project object instead of using this structure 
questions = [
    {"type": "input", "name": "projectTitle", "message": "What is the title of the project?"},
    {"type": "input", "name": "authorName", "message": "Who is the author of the project?"},
    {"type": "input", "name": "contactInfo", "message": "How would you like to be contacted? Please offer an e-mail or telephone number."},
    {'type': 'list',
     'name': 'license',
     'message': 'Select the software license governing usage:',
     'choices': [
         {'name': 'Arrow Up/Down to select', 'value': 'NONE. Please contact the author.'},
         {'name': 'MIT License', 'value': 'MIT'},
         {'name': 'Apache License 2.0', 'value': 'Apache 2.0'},
         {'name': 'GNU GPL v3', 'value': 'GNU GPL v3'},
         {'name': 'GNU LGPL v3', 'value': 'GNU LGPL v3'},
         {'name': 'Mozilla Public License 2.0', 'value': 'Mozilla Public License 2.0'},
         {'name': 'Creative Commons', 'value': 'Creative Commons'},
         {'name': 'Unlicensed', 'value': 'Unlicensed'},
     ],
     'default': 'NONE. Please contact the author.' # Default selection
    },
]
# answer: Dictionary containing all project information in key:value pairs
answers = prompt(questions=questions, style={"question": "yellow", "answer": "gray"})

# Now, use the custom multi-line input function for lnger texts
answers["aboutTheAuthor"] = multiline_input("About the author (a short CV offering qualifications and experiance):")

answers["projectDescription"] = multiline_input("Please describe the project:")

answers["usageInformation"] = multiline_input("Please provide usage information and/or example use cases:")

answers["installationInstructions"] = multiline_input("Installation Instructions:")
# For the purpose of creating the ReadMe.md file a Dictionary (answers) would have been sufficient.
# However, for this project, a key learning item is creating and using classes. 
# Hense, the project information will now be transfered to a Project object.
# Using an object to persist our project information may have benefits, 
# should we need to further process the information.
 
# Initialise the Project object with project information from the answers dictionary. 
project_information = Project(
    project_title = answers["projectTitle"],
    author_name = answers["authorName"],
    contact_info = answers["contactInfo"],
    license_type = answers["license"],
    about_the_author= answers["aboutTheAuthor"],
    project_description = answers["projectDescription"],
    usage_information = answers["usageInformation"],
    installation_instructions = answers["installationInstructions"]
)

# # Function implementing progress bar
# def loading_simulation():
#     console.print("[bold cyan]Creating Your File.[/bold cyan]")  # Widget title/explanation
#     for _ in track(range(10), description="Building..."): # Loop through 10 items to simulate the build
#         time.sleep(0.8)  # Simulate work taking time. Each segment (of 10) takes 0.8sec

# # Test: Display infor in the answers dictionary
# console.print(
#     f'[bold blue] Project Title: [/bold blue] [green] {answers["projectTitle"]}[/green]\n'
#     f'[bold blue] Project Author: [/bold blue] [green] {answers["authorName"]}[/green]\n'
#     f'[bold blue] Contact Author: [/bold blue] [green] {answers["contactInfo"]}[/green]\n'
#     f'[bold blue] Project Description:\n [/bold blue] [green] {answers["projectDescription"]}[/green]\n'
#     f'[bold blue] Usage Information:\n [/bold blue] [green] {answers["usageInformation"]}[/green]\n'
#     f'[bold blue] Installation Instructions:\n [/bold blue] [green] {answers["installationInstructions"]}[/green]\n'
#     f'[bold blue] Licenseing: [/bold blue] [green] {answers["license"]}[/green]\n'
# )

# Test: Print info, from the Project object
# console.print(f"[bold Red]Project Title:[/bold red]\n{project_information.project_title}")
# console.print(f"[bold Red]Project Description:[/bold red]\n{project_information.project_description}")
# console.print(f"[bold Red]Licenseing:[/bold red]\n{project_information.license_type}")

# project_information.create_MD_doc(file_name)
# try to write the file. If file exists, it will be overwritten
try:  #Creat or open the file ready to write in utf-8
    with open(file_name, "w", encoding="utf-8") as file:
        # Call the Project object's create_MD_doc() method. Write the returned str value to the file. 
        file.write(project_information.create_MD_doc())
        # loading_simulation()  # Display progress bar simulating work over time. # Removed, as fascile exercise
    # On completion, print SUCCESS   
    console.print(f"\n[bold green]Successfully generated {file_name}[/bold green]")
   # Catch exception on failure to write file
except IOError as e:
    # On failure pring ERROR msg, plua system generated error msg (e). 
    console.print(f"[bold red]ERROR! We encountered a problem writing file:[/bold red] {e}")
    # Catch-all for any other exception.
except Exception as e:
    # Catches any other error. Print ERROR msg, plus system generated msg (e).
    console.print(f"[bold red]ERROR! An unexpected error occurred: {e}[/bold red]")