from flask import Flask, request, render_template
from werkzeug.utils import redirect
from flask_debugtoolbar import DebugToolbarExtension

from stories import stories_list
# from random import randint,  choice, sample

app = Flask(__name__)

app.config['SECRET_KEY'] = "hi"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def select_story():
    story_titles = [*stories_list]
    return render_template('home.html', story_titles=story_titles)

@app.route('/<story_title>')
def story_form(story_title):
    story = stories_list[story_title]
    prompts = story.prompts
    
    story_title_disp = story_title.replace('_', ' ')
    return render_template('story_form.html', story_title=story_title, prompts=prompts, story_title_disp=story_title_disp)

@app.route('/<story_title>/story')
def show_story_output(story_title):
    story = stories_list[story_title]
    story_text = story.generate(request.args)
    
    story_title_disp = story_title.replace('_', ' ')
    return render_template('story.html', story_text=story_text, story_title_disp=story_title_disp)

@app.route('/', methods=["POST"])
def redirect_to_story():
    story_title = request.form["story-select"]
    return redirect(f'/{story_title}')