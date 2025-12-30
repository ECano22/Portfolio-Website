from flask import render_template
from app import app

PROJECTS = {
    "Console-Tile-Generator": {
        "title": "Console Tile Generator",
        "languages": ["C++", "test"],
        "desc": "",
        "githubLink": "https://github.com/ECano22/Portfolio/tree/main/C%2B%2B/WorldGen",
        "shortdesc": "A procedural terrain generation engine that renders an infinite, explorable 2D world directly in the console.",
        "pagelink": "",
        "thumbnaillink": "ConsoleCPP.png",
    },
    "Data-Driven-Command-Line-RPG": {
        "title": "Data-Driven Command-Line RPG",
        "languages": ["Python"],
        "desc": "",
        "githubLink": "https://github.com/ECano22/Portfolio/tree/main/Python/Turn-Based%20Game",
        "shortdesc": "A feature-complete, text-based RPG that simulates turn-based combat.",
        "pagelink": "",
        "thumbnaillink": "",
    },
    "Portfolio-Website": {
        "title": "Portfolio Website",
        "languages": ["Python", "HTML", "CSS", "JavaScript"],
        "desc": "",
        "githubLink": "https://github.com/ECano22/Portfolio-Website",
        "shortdesc": "A website to host my portfolio projects.",
        "pagelink": "",
        "thumbnaillink": "",
    },
}

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')
@app.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS)
@app.route('/projects/<project_id>')
def project_page(project_id):
    try:
        project = PROJECTS[project_id]
        return render_template('project.html', project=project)
    except KeyError:
        #return 404 page, not created yet
        return 

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')