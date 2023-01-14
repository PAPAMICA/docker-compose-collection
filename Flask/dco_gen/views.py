from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iVu"D[%!N*ZL18K)s\rSW=@:s'

@app.route('/generator/interactif',methods = ['GET','POST'])
@app.route('/generator/interactif/',methods = ['GET','POST'])
def generate_compose():
    return render_template('index.html',connard="Micka")

if __name__ == "__main__":
    app.run()