import aiml
import sys
from bottle import run
from bottle import route 
from bottle import request 
from bottle import redirect
from random import choice
from lib.views import index
from lib.views import Response

botbrain = aiml.Kernel()
botbrain.learn('brain/yulan.aiml')

@route('/')
def RenderIndex():
    return index()

@route('/answer', method='POST')
def ResponseAnswer():
    ask = request.forms.get('ask')
    if ask:
        questions.append(ask)
        try:
            ans = botbrain.respond(ask)
        except:
            ans = choice(default_excuses)
        ask_template = '<p> you just asked: {} </p>'.format(ask)
        respond_template = '<p> her answer: {} </p>'.format(ans)
        return ask_template, respond_template
        redirect('http://localhost:8080/hello')
    return "You asked nothing!"

run(host='localhost', port=sys.argv[1], debug=True)
