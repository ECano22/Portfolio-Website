from flask import render_template
from app import app

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')
@app.route('/projects')
def projects():
    projects = [
        #This should eventually be moved into JSON file
        {
            "id": 0,
            "languages": ["C++"],
            "title": "WorldGen - Console Tile Generator",
            "shortdesc": "A procedural terrain generation engine that renders an infinite, explorable 2D world directly in the console.",
            "infolink": None,
            "demolink": None,
            "sourcelink": "https://github.com/ECano22/Portfolio/tree/main/C%2B%2B/WorldGen"
        },
        {
            "id": 1,
            "languages": ["Python"],
            "title": "Data-Driven Command-Line RPG",
            "shortdesc": "A feature-complete, text-based RPG that simulates turn-based combat.",
            "infolink": None,
            "demolink": None,
            "sourcelink": "https://github.com/ECano22/Portfolio/tree/main/Python/Turn-Based%20Game"
        },
        {
            "id": 2,
            "languages": ["Python", "HTML", "CSS", "JavaScript"],
            "title": "Portfolio Website",
            "shortdesc": "A website to host my portfolio projects.",
            "infolink": None,
            "demolink": None,
            "sourcelink": "https://github.com/ECano22/Portfolio-Website"
        },
    ]
    return render_template('projects.html', projects=projects)
@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')