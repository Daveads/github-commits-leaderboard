import re
import datetime

async def generate_html_table(Lead_data):
    current_date = datetime.datetime.now()  # Get the current date and time
    current_date_str = current_date.strftime("%d-%m-%Y") 
    NUM = 4
    # Generate html table
    html_table = "<table>"
    html_table += f"<thead><tr><th>Username</th><th>Name</th><th>Current_Commit {current_date_str}</th></tr></thead>"
    html_table += "<tbody>"
    for row in Lead_data:
        # Access individual elements of each list (username, name, and contributions)
        username = row[0]
        name = row[1]
        contributions = row[2]

        html_table += f"<tr><td>{username}</td><td>{name}</td><td>{contributions}</td></tr>"
    html_table += "</tbody></table>"
    
    html_table +=f"<p>YOUR COMMITS FOR THE DAY : {NUM} </p>"
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
