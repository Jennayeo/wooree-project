from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

 ## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('main_page.html')

@app.route('/about_us.html')
def about_us():
    return render_template('about_us.html')

@app.route('/product.html')
def product():
    return render_template('product.html')

## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': '이 요청은 POST!'})


@app.route('/review', methods=['GET'])
def read_reviews():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)