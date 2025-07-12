import datetime

datetime_now = datetime.datetime.now()

class Project:
    # Class defining Project information and the processing of that information. 
    def __init__(self, project_title, author_name, contact_info, license_type, about_the_author, project_description, usage_information, installation_instructions):
        # Initialises a new Project object.
        # All args are strings
        self.project_title = project_title
        self.author_name = author_name
        self.contact_info = contact_info
        self.license_type = license_type
        self.about_the_author = about_the_author
        self.usage_information = usage_information
        self.project_description = project_description
        self.installation_instructions = installation_instructions
        # Publishers promotional msg for document footer. Perhaps, not my best idea!
        self.publishing_message = f"This document has been created for {self.author_name}, using EZ Read-Me Doc Generator.  \nDate/Time: {datetime_now.strftime('%d-%m-%Y %H:%M')}  \nEZ Read-Me Doc Generator is unlicensed and free to use."

    def create_MD_doc(self):
        # Create a combined information string based on the Project object's attributes
        # Initialise empty list. To contain each section of the document
        doc_info = []

        # Start the document with Project Title <h1>
        doc_info.append(f"# {self.project_title}\n")

        # If there is a project_description, add 'Description' <h2> to document, followed by the project description.
        if self.project_description:
            doc_info.append("## Description\n") # Sub-title
            doc_info.append(f"{self.project_description}\n") # Section content
            doc_info.append("\n---\n") # Separator

        # If there is usage_information, add 'Usage Information' <h2> to document, followed by the usag info.
        if self.usage_information:
            doc_info.append("## Usage Information\n") # Sub-title
            doc_info.append(f"{self.usage_information}\n") # Section content
            doc_info.append("\n---\n") # Separator
        
        # Installation instructions
        if self.installation_instructions:
            doc_info.append("## Installation\n")
            doc_info.append(f"\n{self.installation_instructions}\n")
            doc_info.append("\n---\n")

        # Add licensing
        doc_info.append(f"{self.license_type}\n")
        doc_info.append("\n---\n") 
       
        # Add information about the author
        doc_info.append("## About the Author\n")
        doc_info.append(f"Author: {self.author_name}\n")
        # If there is information about the author, add brief CV, here.
        if self.about_the_author:
            doc_info.append("### Curriculum Vitae\n")   #sub-heading <h3>
            doc_info.append(f"{self.about_the_author}\n")
        doc_info.append(f"Contact Info: {self.contact_info}\n")
        doc_info.append("\n")
        doc_info.append("\n---\n---\n") # Double separator
        
        doc_info.append(f"\n{self.publishing_message}\n") # Add publishing_message as footer

        # Join all parts into a single final_doc (str).
        final_document = "\n".join(doc_info)
        # rtn BIG STR!
        return final_document
