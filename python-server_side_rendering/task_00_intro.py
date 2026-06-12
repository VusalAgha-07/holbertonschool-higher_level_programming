#!/usr/bin/python3
def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return

    # Handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, 1):
        # Prepare data, replacing missing or None values with "N/A"
        data = {
            "name": attendee.get("name") if attendee.get("name") else "N/A",
            "event_title": attendee.get("event_title") if attendee.get("event_title") else "N/A",
            "event_date": attendee.get("event_date") if attendee.get("event_date") else "N/A",
            "event_location": attendee.get("event_location") if attendee.get("event_location") else "N/A"
        }

        # Format the template
        try:
            content = template.format(**data)
            
            # Generate output file
            filename = f"output_{i}.txt"
            with open(filename, 'w') as f:
                f.write(content)
        except KeyError as e:
            print(f"Error: Missing key in template - {e}")
