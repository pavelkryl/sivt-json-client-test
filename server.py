from typing import Any, Tuple
from flask import Flask, Response, request, jsonify
import copy

app = Flask(__name__)

# Sample data
repo = {
    "1": { "nazev": "mleko", "cena": 23, "skladem": True },
    "2": { "nazev": "chleba", "cena": 49, "skladem": True },
    "3": { "nazev": "tatranka", "cena": 7.50, "skladem": False },
}

repo_by_ip : dict[str,dict[str,Any]] = dict()

ServerReply = Tuple[Response, int]

# Route to get all goods
@app.route('/zbozi', methods=['GET'])
def get_items() -> Response:
    client_data = copy.deepcopy(get_client_data())
    # remove id
    for item in client_data.values():
        del item["id"]
    return jsonify(client_data)

# Route to get a student by ID
@app.route('/zbozi/<int:item_id>', methods=['GET'])
def get_student(item_id: int) -> ServerReply:
    item_data = get_client_data().get(str(item_id))
    if item_data is None:
        return jsonify({"error": f"Zbozi id={item_id} nenalezeno"}), 404
    else:
        return jsonify(item_data), 200

# Route to add a new student
@app.route('/zbozi', methods=['POST'])
def add_student() -> ServerReply:
    new_item = request.get_json()
    if "id" not in new_item or "nazev" not in new_item or "cena" not in new_item or "skladem" not in new_item:
        return jsonify({"error": "Spatny vstup: chybi jedno z id, nazev, cena, skladem"}), 400
    client_data = get_client_data()
    new_id = str(new_item.get("id"))
    # make sure we return the ID as string
    new_item["id"] = new_id
    if new_id in client_data:
        return jsonify({ "error": f"id {new_id} already used"}), 409
    # else:
    client_data[new_id] = new_item
    return jsonify(new_item), 201

# Route to update an existing item
@app.route('/zbozi/<int:item_id>', methods=['PUT'])
def update_student(item_id: int) -> ServerReply:
    new_item = request.get_json()
    to_update = get_client_data().get(str(item_id))
    if to_update is None:
        return jsonify({"error": f"Nezname id {item_id}"}), 404
    for key in new_item:
        if key == "id" and new_item["id"] != to_update["id"]:
            return jsonify({"error": f"Nelze měnit id"}), 400
        if key != "cena" and key != "nazev" and key != "skladem" and key != "id":
            return jsonify({"error": f"Spatny vstup: co to je {key}"}), 400
    to_update.update(new_item)
    return jsonify(to_update), 200

# Route to delete a student
@app.route('/zbozi/<int:item_id>', methods=['DELETE'])
def delete_item(item_id: int) -> ServerReply:
    client_data = get_client_data()
    if client_data.pop(str(item_id), None) is None:
        return jsonify({"error": f"Nezname id {item_id}"}), 404
    else:
        return jsonify({}), 200

def get_client_data() -> dict[str,Any]:
    if request.remote_addr is None:
        raise Exception("client does not have IP address?")
    if repo_by_ip.get(request.remote_addr) is None:
        deep_copy = copy.deepcopy(repo)
        repo_by_ip[request.remote_addr] = deep_copy
        # enrich each item with id
        for key, value in deep_copy.items():
            value["id"] = key
    return repo_by_ip[request.remote_addr]

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
