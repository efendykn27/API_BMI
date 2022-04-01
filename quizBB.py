from flask import Flask, request, make_response, jsonify
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

class BMI(Resource):
    def post(self):
        dataBerat = float(request.form['berat'])
        dataTinggi = float(request.form['tinggi'])

        BMI = dataBerat/(dataTinggi/100)**2
        
        if BMI <18.5:            
            keterangan = "Kurus"
            
        elif BMI>18.5 and BMI<25 :
            keterangan = "Nomral"
        elif BMI>25 and BMI<40:
            keterangan = "Berlebih"
        else:
            keterangan = "Bahaya"        
        hasil = {"success" : True, "BMI":BMI,"Hasil":keterangan}
        return jsonify(hasil)

api.add_resource(BMI, "/api/BMI", methods=["POST"])


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True , port=4000)
