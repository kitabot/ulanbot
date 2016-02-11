import aiml

botbrain = aiml.Kernel()
botbrain.learn('data/brain.aiml')
exception_brainmatrix = ['\n','\t']
default_excuses = [':)','gatau :P',':3', 'ajarin ulan, dong']
with open('yulan.aiml', 'r') as readbrain:
    brains = readbrain.readlines()

brain_matrix = []
for contents in brains:
    if contents not in exception_brainmatrix:
        brain_matrix.append(contents)

knowledge = '-'.join(brain_matrix)
questions = []

def index():

    view = '''
    <html>
    <title>ulan</title>
    <h1>Ulan</h1>
    <hr>
    <b> Ulan (baca: yu-lan) is a chatterbot based on yulanyulianty's answers on her ask.fm </b>
    <hr>
    <br></br>
    <p> you just asked {} </p>
    <form action="/answer" method="post">
    ask: <input name="ask" type="text"/>
    <input value="tanya" type="submit" />
    <br></br>
    <p> status: </p>
    <p> current brain matrix: {} </p>
    <p> current AIML Brain knowledge(s)</p>
    <p> {} </p>
    </html>
    '''.format(questions,len(knowledge), knowledge)
    return view

def Response(question):
   