from flask import Flask, jsonify, make_response, request
app = Flask(__name__)

@app.route("/json", methods=["POST"])
def json_example():

    if request.is_json:

        req = request.get_json()
        weight = req.get("weight")
        bfat = req.get("bfat")
        activity = req.get("activity")
        bmr = 21.6*(weight-(bfat/100*weight)) + 370
        tdee = bmr*activity
        response_body = {
            "BMR": bmr,
            "sender": tdee
        }

        res = make_response(jsonify(response_body), 200)

        return res

    else:

        return make_response(jsonify({"message": "Request body must be JSON"}), 400)

if __name__ == "__main__":
    app.run()