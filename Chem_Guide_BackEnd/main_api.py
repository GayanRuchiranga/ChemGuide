from flask import Flask, jsonify, request, json, g
from dbconnection import connection
import Conversions_Backup
# import Conversions
import lewis
import iupac
import essay
import gc

app = Flask(__name__)

print("========================================================")
print("")
print("  ____ _                       ____       _     _      ")
print(" / ___| |__   ___ _ __ ___    / ___|_   _(_) __| | ___ ")
print("| |   | '_ \ / _ \ '_ ` _ \  | |  _| | | | |/ _` |/ _ \\")
print("| |___| | | |  __/ | | | | | | |_| | |_| | | (_| |  __/")
print(" \____|_| |_|\___|_| |_| |_|  \____|\__,_|_|\__,_|\___|")
print("""╔╗ ┌─┐┌─┐┬┌─   ╔═╗┌┐┌┌┬┐
╠╩╗├─┤│  ├┴┐───║╣ │││ ││
╚═╝┴ ┴└─┘┴ ┴   ╚═╝┘└┘─┴┘""")
print("========================================================")


@app.route('/user_registration', methods=['POST'])
def user_registration():
    try:
        c, conn = connection()
        c.execute("SELECT * FROM users where email =%s",
                  (request.json['email'],))
        data = c.fetchall()

        edata = str(data).replace("'", "").replace(
            "(", "").replace("),)", "").replace(" ", "").replace(")", "")

        if (len(edata) == 0):
            c.execute("INSERT INTO users(email,password,f_name,l_name) VALUES (%s,%s,%s,%s)",
                      (request.json['email'], request.json['password'], request.json['f_name'], request.json['l_name']))
            conn.commit()

            c.close()
            conn.close()
            gc.collect()

            return "1"
        else:
            return "0"

    except Exception as e:
        return (str(e))


@app.route('/login', methods=['POST'])
def login():
    try:
        c, conn = connection()
        c.execute("SELECT id,email,f_name,l_name, password FROM users where email =%s",
                  (request.json['email'],))
        data = c.fetchall()
        edata = str(data).replace("'", "").replace("(", "").replace("),)",
                                                                    "").replace(" ", "").replace(")", "")
        if(len(edata) == 0):
            return "2,b"
        elif(edata.split(",")[4] == request.json['password']):
            info = edata.split(",")
            return "1,"+info[0]+","+info[1]+","+info[2]+","+info[3]
        else:
            return "0,a"
    except Exception as e:
        return (str(e))


@app.route('/analyze', methods=['POST'])
def analyzer():
    if request.json['type'] == 'cnv':
        json = request.get_json()
        text = (json["msg"])
        question = text.split(",")
        input = question[0].replace("0", "O")
        output = question[1].replace("0", "O")
        result = Conversions_Backup.analyze(input, output)
        # result = Conversions.analyze(input, output)

        try:
            c, conn = connection()
            c.execute("INSERT INTO conversion_questions(user_id,question,g_answer) VALUES (%s,%s,%s)",
                      (request.json['user'], text, result))
            conn.commit()

            c.close()
            conn.close()
            gc.collect()
        except Exception as e:
            return (str(e))

        type = "cnv"
        info = result
        data = {"type": type, "data": info}

        return jsonify(data)

    elif request.json['type'] == 'lewis_name':
        try:
            result = lewis.lewis_t(request.json['msg'])

            type = "lewis_name"
            data = {"type": type, "data": result}
            print(data)
            return jsonify(data)
        except Exception as e:
            return (str(e))

    elif request.json['type'] == 'lewis_struc':
        try:
            result = lewis.analyze_struc(request.json['msg'])
            type = "lewis_struc"

            #c, conn = connection()
            # c.execute("INSERT INTO lewis_questions(user_id,type,question,g_answer) VALUES (%s,%s,%s,%s)",
            #          (request.json['user'], type, request.json['msg'], result))
            # conn.commit()

            # c.close()
            # conn.close()
            # gc.collect()

            data = {"type": type, "data": result}
            return jsonify(data)
        except Exception as e:
            return (str(e))

    elif request.json['type'] == 'iupac_name':
        result = iupac.structure_to_name(request.json['msg'])
        type = "iupac"
        section = "iupac_name"
        try:
            c, conn = connection()
            c.execute("INSERT INTO iupac_questions(user_id,type,question,g_answer) VALUES (%s,%s,%s,%s)",
                      (request.json['user'], section, request.json['msg'], result))
            conn.commit()

            c.close()
            conn.close()
            gc.collect()
        except Exception as e:
            return (str(e))
        data = {"type": type, "data": result}
        return jsonify(data)

    elif request.json['type'] == 'iupac_structure':
        result = iupac.name_to_structure(request.json['msg'])
        type = "iupac"
        # try:
        #   c, conn = connection()
        #   c.execute("INSERT INTO iupac_questions(user_id,type,question,g_answer) VALUES (%s,%s,%s,%s)",(request.json['user'], type, request.json['msg'], result))
        #   conn.commit()

        #   c.close()
        #    conn.close()
        #    gc.collect()
        # except Exception as e:
        #    return (str(e))
        data = {"type": type, "data": result}
        return jsonify(data)

    elif request.json['type'] == 'essay':
        result = essay.analyze(request.json['msg'])
        print(result)
        type = "essay"
        try:
            c, conn = connection()
            c.execute("INSERT INTO essay_questions(user_id,question,g_answer) VALUES (%s,%s,%s)",
                      (request.json['user'], request.json['msg'], result))
            conn.commit()

            c.close()
            conn.close()
            gc.collect()
        except Exception as e:
            return (str(e))
        data = {"type": type, "data": result}
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
