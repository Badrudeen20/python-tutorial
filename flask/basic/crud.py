from flask import Flask,jsonify,request
app = Flask(__name__)

course = [
    {
        'name':'python',
        'duration':'Three month',
        'fees':2000,
    },
    {
        'name':'java',
        'duration':'five month',
        'fees':4000,
    },
    {
        'name':'c++',
        'duration':'Three month',
        'fees':1000,
    },
    {
        'name':'php',
        'duration':'one month',
        'fees':500,
    },
]

@app.route('/')
def index():
    return "welcome to badru"


# @app.route('/course',methods=['GET'])
# def get():
   
#    if request.args :
#         name = request.args.get('language')
#         return jsonify({'course':course[name]})
#    else:
#       return jsonify({'course':course})
   

@app.route('/course/<int:fees>',methods=['GET'])
def get(fees):
   
 return jsonify({'course':course[fees]})

@app.route('/create',methods=['POST'])
def create():
 add =  {
        'name':'react',
        'duration':'one month',
        'fees':900,
    },
 course.append(add)
 return jsonify({'course':course})

# @app.route('/delete/<int:id>',methods=['POST'])
# def delete(id):
#  course.remove(add)
#  return jsonify({'course':course})
   


if __name__ == "__main__":
	app.run(debug=True)