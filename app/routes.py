from flask import render_template, current_app
from app import app
from pathlib import Path

PROJECTS = {
    "Console-Tile-Generator": {
        "title": "Console Tile Generator",
        "imglink": "ConsoleCPPImage.png",
        "languages": ["C++"],
        "desctxt": "tilegenerator",
        "githubLink": "https://github.com/ECano22/Portfolio/tree/main/C%2B%2B/WorldGen",
        "shortdesc": "A procedural terrain generation engine that renders an infinite, explorable 2D world directly in the console.",
        "pagelink": "",
        "thumbnaillink": "ConsoleCPPThumbnail.png",
    },
    "Portfolio-Website": {
        "title": "Portfolio Website",
        "imglink": "",
        "languages": ["Python", "HTML", "CSS", "JavaScript"],
        "desctxt": "portfolio",
        "githubLink": "https://github.com/ECano22/Portfolio-Website",
        "shortdesc": "A website to host my portfolio projects.",
        "pagelink": "",
        "thumbnaillink": "portfoliowebsitethumbnail.png",
    },
}

#project description is kept in txt file
BASE_DIR = Path(__file__).resolve().parent
INFO_DIR = BASE_DIR / 'static' / 'info'

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')
@app.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS)
@app.route('/projects/<project_id>')
def project_page(project_id):
    for project in PROJECTS.values():
        project["desc"] = "No description has been set for this project"
        try:
            project["desc"] = (INFO_DIR / f'{project["desctxt"]}.txt').read_text(encoding="utf-8")
        except FileNotFoundError:
            app.logger.error("File %s was not found", project["desctxt"])

    for project in PROJECTS.values():
        project["features"] = "No features have been written for this project"
        try:
            project["features"] = (INFO_DIR / f'{project["desctxt"]}features.txt').read_text(encoding="utf-8")
        except FileNotFoundError:
            app.logger.error("File for %s was not found", project["title"])
        
    try:
        project = PROJECTS[project_id]
        return render_template('project.html', project=project)
    except KeyError:
        #return 404 page, not created yet
        return 

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')