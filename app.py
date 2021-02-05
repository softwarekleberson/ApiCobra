from flask import Flask, render_template,request

app = Flask(__name__, template_folder='./src/view')

@app.route("/", methods=["GET", "POST"])
def home():
    if(request.method == "GET"):    
        return render_template("index.html")
    
    else:
        if(request.form["num1"] != "" and request.form["num2"] != ""):
            num1 = request.form["num1"]
            num2 = request.form["num2"]

            if(request.form["opc"] == "soma"):
                soma = int(num1) + int(num2)
                return str(soma)
            
            elif (request.form["opc"] == "subt"):
                subt = int(num1) - int(num2)
                return str(subt)

            elif (request.form["opc"] == "mult"):
                mult = int(num1) * int(num2)
                return str(mult)

            elif (request.form["opc"] == "divi"):
                div = int(num1) // int(num2)
                return str(div)
        
        else:
            return"informe um valor valido"

@app.errorhandler(404)
def not_found(error):
    return render_template("erro.html")

app.run(port=8000, debug=True)
