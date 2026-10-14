from pyscript import document, display

# Predefined sets of student club members
grade7 = {
    "Peter Quill",
    "Peter Parker",
    "Peter Pettigrew"
}

grade8 = {
    "Jacob Collier",
    "John Mayer",
    "Hayley Williams"
}

grade9 = {
    "Anthony Cases",
    "Lara Georgina"
}

grade10 = {
    "Christer Ian",
    "Dustin Cunanan",
    "Adriana Averilla",
    "Ciara De Guzman",
    "Rafael Roncal"
}

# Combine all grade levels into one master set
members = grade7 | grade8 | grade9 | grade10

def recruit(e):

    # Get the first and last names
    Fname = document.querySelector("#Fname").value.strip()
    Lname = document.querySelector("#Lname").value.strip()

    # Combine the names
    name = (Fname + " " + Lname).title()

    # Add the new member to the master set
    members.add(name)

    # Display all members on separate lines
    document.querySelector("#list").innerHTML = "<br>".join(sorted(members))

    # Display total number of members
    document.querySelector("#count").innerText = str(len(members))