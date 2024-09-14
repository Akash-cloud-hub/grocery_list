from flask import Flask , render_template , request
app = Flask(__name__)

@app.route('/')
def home():
    items = ['Milk' , 'Vegetables' , 'Fruit' , 'Drinks' , 'Cereal']
    return render_template('index.html',items = items)

if __name__ == '__main__':
    app.run(debug = True)