import re
import datetime

async def generate_html_table(Lead_data):
    
    current_date = datetime.datetime.now()  # Get the current date and time
    current_date_str = current_date.strftime("%d-%m-%Y") 
    
    # Generate html table
    html_table = "<table>"
    html_table += f"<thead><tr><th>Username</th><th>Name</th><th>Contributions for {current_date_str}</th></tr></thead>"
    html_table += "<tbody>"
    for row in Lead_data:
        # Using regular expression to split by multiple spaces
        match = re.match(r"(.*?) \((.*?)\) +(\d+,*\d*)", row)
        # print(match)
        if match:
            username, name, contributions = match.groups()
            html_table += f"<tr><td>{username}</td><td>{name}</td><td>{contributions}</td></tr>"
    html_table += "</tbody></table>"

    # HTML template
    html_template = """
    <html>
        <head>
            <style>
                table {
                    border-collapse: collapse;
                    width: 50%;
                }
                
                th, td {
                    text-align: left;
                    padding: 8px;
                }
                
                th {
                    background-color: #f2f2f2;
                }
            </style>
        </head>
        <body>
            {{TABLE}}
        </body>
    </html>
    """

    html_page = html_template.replace("{{TABLE}}", html_table)
    return html_page