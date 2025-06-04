def build_homepage_prompt(data):
    return f"""
Write a homepage introduction for a {data['industry']} business named '{data['business_name']}' located in {data['location']}.
The business offers: {data['services']}.
Use a {data['tone']} tone. Include a welcoming headline, short business overview, and a bullet list of services.
"""
