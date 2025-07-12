# Python ReadMe File Generator

## Introduction:

Herewith my submission for Week-6's challenge: a Python ReadMe file generator. The file generator project comprising: python source files (main.py, function.py, project.py), and dependencies (managed through requirements.txt) is executed within a virtual environment (myvenv).

The source code has been modularised to enhance maintainability and promote code reuse. The entry point for the project solution is main.py. This deals with presentation, user input, file output, and exception handling. It creates and uses a object of the Project class, defined in the project.py file. It also uses a function (multiline_inputthe()), from the function.py file.

The project is dependent on a number of Python libraries (rich and InquirerPy). These were installed within the project's virtual environment (myvenv). Installation was completed by calling the requirements.txt file from the command line (cmd). See Installation Instructions for further details.

Specific solution features and coding strategies are not listed within this document. The Python file have been judiciously commented, to provide in-line documentation. However, some justification of my solution strategy will be offered. The solution has been pushed to my GitHub repository, for public access and review.

---

## The Solution

### Behind the README File Generator

The main functionality of the ReadMe file generator is defined within the main.py file; the entry point for the solution. The main.py script utilises project.py and function.py files.

#### main.py

Main presents a welcome message using 'rich.console'. It then goes on to question the user (for simple sort answers and list selection), employing 'InquirerPy.prompt'. It accepts larger text inputs by using the multiline_input() function, from the function.py file. I decided to implement the multiline_input() function, because I was not happy with the user simply typing (what could be a very long string) at the cmd prompt. However, multiline_input() was not my first choice of solution, and I do not think that it is the best solution. Initially, I wanted to use the InquirerPy.prompt's editor type. When the Editor is called, it opens an editor in the user's default text editor (where text could be word processed in a familiar environment). Despite putting a lot of time and effort into that solution, I couldn't reliably get it to work. Hence, multiline_input() emerged as my best compromise. Caveat No1: We can't make the perfect product. So, sometimes, we just have to ship the product that we've got.

Main collects all the user responses into a dictionary (answers). With 'answers' in the bag (dictionary), I could have proceeded to create the readme file. However, for this project, a key learning item was creating and using classes. So, the project information was transferred to a Project object. Using an object to persist our project information does offer benefits in further processing the information for presentation.

Main uses the return from a call to Project's create_MD_doc() method to create and write (overwrite if already existing) our ReadMe.md file. Main also deals with exception handling of this process.

#### project.py

The Project object created my main.py persists the user information in its attributes. It also defines a method (create_MD_doc()), that formats the individual pieces of information into a single final_document (very long) string, and returns that string.

The create_MD_doc() function also adds a publishing_message to the end of the document (as a footer). This includes the authors name, date/time of publication, and licensing information for the ReadMe.md Generator product.

#### function.py

This file contains a single function (multiline_input()), that retrieves the long multi-line text inputs from the user. The multiline_input() function does interact directly with the user, requesting multi-line input. This was probably not my best design decision, as it doesn't adhere to clean/clear division of labour between modules. It doesn't really enhance maintainability or promote code reuse. With the clock ticking to submit the project, Caveat No1 applies.

#### Redundant Code

During development consol.print() was judiciously employed to confirm the assignment of data elements (in the answers dictionary and the Project object), and to model styling strategies. Though now redundant, these segments of code have been retained (commented out) to demonstrate that part of the development process. 

At one point during development, the main.py file defined a function that implemented a progress bar (loading_simulation()). This was to be used while the ReadMe.md file was being created. However, this was a simulation of progress that simply displayed elapsed time, as a purely aesthetic filler. The feature was removed from the final deployment, as a frivolous exercise. The code remains in place, now commented out.

---

## Installation and Deployment

The project (source file and dependencies) needs to be executed within a virtual environment. The virtual environment is created in the root file of the project. The virtual environment is then activated, and the dependencies installed into the virtual environment, along with the source files.

### Procedures:

In the root directory of the project:  

1. Create a virtual environemnt named myvenv:  
/path/to/your/project$ python -m venv myvenv  

2. Activate the virtual environment:  
/path/to/your/project$ .\myvenv\Scripts\activate

Outcome (myvenv)/path/to/your/project$

3. Install the packages listed in your requirements.txt file:  
(myvenv)/path/to/your/project$ pip install -r requirements.txt

While the project should be pushed to GitHub, for remote source control, the virtual environment and installed dependencies must remain local. To achieve this, a .gitignore file is place in the root of the repository.

On creation of the new (week6) repository, a .gitignore file is added. This file should be edited to exclude the virtual environment (myvenv) file. By adding the line **/myvenv/. git will ignore any file named myvenv anywhere (in root or subdirectory).

The week6 repository can now be cloned to the local host, and the project files added to the repository. Thereafter, git source control can be employed as normal.

### GitHub repository:

My solution is contained within a project called: W6-Challenge-Mayer.  

---

## To Conclude:

I hope that that this submission is adequate and appropriate, at this stage of the course.  

Though I believe that the project does fulfil the challenge requirements brief, I do not believe it to be sufficiently flexible/scalable to draft this ReadMe.md document.


---

<br/>

<hr style="height: 5px; background-color: black; border: none;">
