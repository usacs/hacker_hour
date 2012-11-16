from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    if 'name' in request.args:
        name = request.args['name']

        if not name.isalpha():
            raise Exception('You suck')
        comments = open(name+'.txt').read()
        return render_template('profile.html', name=name, comments=comments)
    return render_template('home.html')

@app.route('/', methods=["POST"])
def comment():
    print request.form
    profile = request.form['profile']

    if not profile.isalpha():
        raise Exception('You suck')

    open(profile+'.txt', 'a').write(request.form['comment']+"\n\n")
    comments = open(profile+'.txt').read()
    return render_template('profile.html', name=profile, comments=comments)

#if __name__ == '__main__':

app.run(port=8000,debug=True)
