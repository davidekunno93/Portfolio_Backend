# importing app to route different web directories
from app import app
from .models import Projects, Feedback, MiniApps
from flask import request

# if url = localhost:5000/ call this function and return this
@app.route('/')
def index():
    return "Home page"

@app.route('/add-project', methods=["GET"])
def addProject():
    
    title = "RealPeace Website"
    display_picture_url = "https://i.imgur.com/QAbvGvf.png"
    title_img_url = "https://i.imgur.com/DtRwseu.png"
    description = "RealPeace is a website for social gatherings and organized group meditation meetups"
    text1 = "RealPeace is a group created by one of my close friends. The group aims to create a space and provide activities for people who are interested in meditation to meet, socialize and practice meditation together. I was particularly interested in making this website responsive for phone devices as this is likely the primary way the website will be accessed. This project the opportunity for me to learn how to optimize UX, my goal was to create a stylistic website which looks both professional and modern but also has a calm feel with softer colors and round edges. I also learned how to build a carousel during this project. Flask is used for the Backend, React JS is used for the Frontend"
    text2 = "When this website is complete, users will be able to find scheduled meetups and register to go those meetups. Users will also be able to subscribe to meetups so they receive email reminders for them, and users will be able to make donations to the event organizers if they would like to."
    more_imgs_urls = "https://i.imgur.com/w4yT2Bw.png*https://i.imgur.com/g3wpY65.png"
    technologies = "HTML, CSS, Python, React JS, Flask, PostgreSQL"
    github_link = "Coming soon..."
    website_link = "Coming soon..."

    project = Projects(title, display_picture_url, title_img_url, description, text1, text2, more_imgs_urls, technologies, github_link, website_link)

    # project.save_to_db()
    # print("project added")

    return "All done Master Wayne"


@app.route('/add-mini-app', methods=["GET"])
def addMiniApp():
    
    title = "Geo-Weather App"
    display_picture_url = "https://i.imgur.com/GSFFAdd.png"
    title_img_url = "https://i.imgur.com/X6WuFtg.png"
    description = "Search any city to find out what the weather is like there right now."
    text = "This app allowed me to explore using API calls from multiple different APIs simultaneously, sorting through that returned information and displaying it on the page. I also continued to practice using the DOM and took the opportunity to exercise my creativity producing icons and images for this project."
    more_imgs_urls = "https://i.imgur.com/HQav78j.png*https://i.imgur.com/K7lyfDa.png"
    technologies = "HTML, CSS, JavaScript"
    github_link = "https://github.com/davidekunno93/Weather_App.git"
    website_link = "Coming soon..."

    mini_app = MiniApps(title, display_picture_url, title_img_url, description, text, more_imgs_urls, technologies, github_link, website_link)

    # mini_app.save_to_db()
    # print("mini-app added")

    return "Coast is clear"

@app.route('/update-more-imgs', methods=["GET"])
def update_more_img_urls():

    project = Projects.query.filter_by(title="Pokemon Battle X").first()
    print(project)
    # project.update_more_imgs("https://i.imgur.com/x58F4yh.png*https://i.imgur.com/H1w3kaT.png*https://i.imgur.com/8pUi2Ue.png*https://i.imgur.com/cGX5imp.png*https://i.imgur.com/Qf3kZoO.png*https://i.imgur.com/KtqKI1z.png")

    # print("images updated")
    return "Complete Sir"

@app.route('/submit-feedback', methods=["POST"])
def submit_feedback():

    data = request.get_json()

    # data.suggestion

    return "nothing"