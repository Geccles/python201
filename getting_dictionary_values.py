courses = {
    "js": "Javascript 101",
    "python": ["Python 101", "Python 201"],
    "html": "HTML 101",
    "css": "CSS"
}

if courses.get("js", None):
    print(f"We got: {courses['js']}")

if courses.get("go", "We could not find the course"):
    print(f"We could not find the course")
