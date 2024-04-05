# Copyright 2023 FOSForums
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from datetime import datetime

# Read LaTeX template for certificates of participation
# This is a one-time operation, no need to read the template for every name
with open("template-attendee.tex", "r") as f:
    latex_template_attendee = f.read()

def generate_pdf(name):
    """
    Generate a PDF certificate for the given name.

    Parameters:
    name (str): The name of the attendee

    """
    # Replace the placeholder in the template with the actual name
    latex_code = latex_template_attendee.replace("[Name of the Attendee]", name)
    
    # Write the modified LaTeX code to a temporary .tex file
    with open("temp.tex", "w") as f:
        f.write(latex_code)
        
    # Compile the LaTeX code to produce a PDF
    # NOTE: You must have pdflatex installed and available in the PATH
    os.system("pdflatex temp.tex")

    # Generate a timestamp for unique file naming
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Rename the generated PDF file to include the attendee name and timestamp
    os.rename("temp.pdf", f"{name}_certificate_{timestamp}.pdf")

# Read attendee's names from a file
# Assumes one name per line in the file
with open("attendees.txt", "r") as f:
    attendees = f.readlines()

# Loop through each name and generate a PDF certificate
for attendee in attendees:
    attendee = attendee.strip()  # Remove any leading/trailing whitespace or newline characters
    generate_pdf(attendee)  # Call the function to generate PDF

# Cleanup: Remove temporary files generated during PDF creation
os.remove("temp.tex")
os.system("rm *.aux")
os.system("rm *.log")