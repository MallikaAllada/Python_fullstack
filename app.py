from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "render_template"
if __name__=='__main__':
    app.run(debug=True)
    @app.route('login',methods=["POST", "GET"])
    def login():
        if request.mthod=="POST":
              return render_template("login.html")
        return render_template("login.html") 
        @app.route('/api/registr', methods=["POST"])
        def api_register():
            data=request.get_json()
            email=ata.get("email")

            if email in users_db:
                return jsonify({"status":"error","message":"user already xit with this email!"}),400
                @app.route('/api/login', methods=["post"])
                def api_login():
                    data=request.t_json()
                    email=data.get("password")
                    user=uers_db.get(email)
                    if user and user.get("pasword")==password:
                        return jsonify({"tatus":"success","message":"login successul ! welcome back,"})
                    else:
                            return jsonify({"tatus":"error","message":"invaild email o password!,"}),401
