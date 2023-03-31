import pandas as pd
import difflib
df_expertise = pd.read_csv(r'C:\Users\13911\Desktop\test\static\Complete expertiselijst NDV.csv')
cnt = df_expertise["Expertise"].value_counts()
cnt_expertise= {'type':cnt.index,'numbers':cnt.values}
df_cnt=pd.DataFrame(cnt_expertise)
expertise=(df_cnt.to_dict(orient='records'))
# name = 'Expertise data'


from flask import Flask, render_template,request

# ...
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('homepage.html',  expertise=expertise)





# @app.route('/', methods=['post', 'get'])

# def search():
#     content = request.form.get('content') #需要查询的内容
#     df_expert=df_expertise[df_expertise["Expertise"]==content]
#     dict_expert={col:df_expert[col].tolist()for col in df_expert}
#     df_ex=pd.DataFrame(dict_expert)
#     expertise=(df_ex.to_dict(orient='records'))

#     return render_template('friday_website.html',expertise = expertise) #将查询结果返回到前端


@app.route('/friday_website',methods=['GET'])
def show_expertise():
    expert=request.args.get('expert')
    keyword=difflib.get_close_matches('expert',df_expertise["Expertise"].tolist())
    df_expert=df_expertise[df_expertise["Expertise"]==keyword]
    dict_expert={col:df_expert[col].tolist()for col in df_expert}
    df_ex=pd.DataFrame(dict_expert)
    expertise=(df_ex.to_dict(orient='records'))
    # expertise["location"] = expertise.pop("Eenheid/netwerk")
    return render_template('friday_website.html', expertise=expertise)

@app.route('/agusti_branxart',methods=['GET'])
def expertise_detail():
    expert=request.args.get('phone')
    df_expert=df_expertise[df_expertise["Telefoon"]==expert]
    dict_expert={col:df_expert[col].tolist()for col in df_expert}
    df_ex=pd.DataFrame(dict_expert)
    expertise=(df_ex.to_dict(orient='records'))
    # expertise["location"] = expertise.pop("Eenheid/netwerk")
    return render_template('agusti_branxart.html', expertise=expertise)

# @app.route('/agusti_branxart/<expert>')
# def expertise_details(expert):
#     df_expert=df_expertise[df_expertise["Expertise"]==expert]
#     dict_expert={col:df_expert[col].tolist()for col in df_expert}
#     df_ex=pd.DataFrame(dict_expert)
#     expertise=(df_ex.to_dict(orient='records'))
#     # expertise["location"] = expertise.pop("Eenheid/netwerk")
#     return render_template('agusti_branxart.html', expertise=expertise)



# from flask import Flask, render_template, request


# Expertises = [
#     {'type': 'Chinese network', 'number': '198'},
#     {'type': 'LGBTQ', 'number': '208'},
#     {'type': 'ROze in blauw', 'number': '48'},
#     {'type': 'Maroku', 'number': '184'},
#     {'type': 'Iran', 'number': '239'},
    # {'title': 'Dead Poets Society', 'year': '1989'},
    # {'title': 'A Perfect World', 'year': '1993'},
    # {'title': 'Leon', 'year': '1994'},
    # {'title': 'Mahjong', 'year': '1996'},
    # {'title': 'Swallowtail Butterfly', 'year': '1996'},
    # {'title': 'King of Comedy', 'year': '1999'},
    # {'title': 'Devils on the Doorstep', 'year': '1999'},
    # {'title': 'WALL-E', 'year': '2008'},
    # {'title': 'The Pork of Music', 'year': '2012'},
# ]
# print(type(Expertises))
# app = Flask(__name__)
# @app.route("/")
# def index():
#     return render_template("homepage.html")

# @app.route("/agusti_branxart.html",methods=['GET','POST'])
# def detail():
#     # if request.method=='POST':
#     # name= request.form.get("first_name")
#         return render_template("agusti_branxart.html")

# @app.route("/friday_website.html",methods=['GET','POST'])
# def expertise():
#     # if request.method=='POST':
#     # name= request.form.get("first_name")
#         return render_template("friday_website.html")
