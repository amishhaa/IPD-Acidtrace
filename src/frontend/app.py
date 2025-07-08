from flask import Flask, request, jsonify
from flask_cors import CORS
from blockchain import TransactionGroup

app = Flask(__name__)
CORS(app)  # Enables cross-origin requests for frontend integration

# Initialize the blockchain model
group = TransactionGroup()

# [Endpoint] Root: Welcome or health check route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to AcidTrace Blockchain API!"})

# [Endpoint] Create a new acid source
@app.route('/create-source', methods=['POST'])
def create_source():
    """
    Request JSON:
    {
        "source_code": 1234,
        "amount": 100
    }
    """
    try:
        data = request.get_json()
        source_code = int(data['source_code'])
        amount = int(data['amount'])

        group.create_source(source_code, amount)

        return jsonify({
            "message": "Source created successfully.",
            "source_code": source_code,
            "amount": amount
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# [Endpoint] Create a transaction between vendors/sources
@app.route('/create-transaction', methods=['POST'])
def create_transaction():
    """
    Request JSON:
    {
        "vendor_code": 1234,
        "source_code": 1243,
        "amount": 50,
        "leaf": false
    }
    """
    try:
        data = request.get_json()
        vendor_code = int(data['vendor_code'])
        source_code = int(data['source_code'])
        amount = int(data['amount'])
        leaf = bool(data.get('leaf', False))  # Optional flag

        group.create_transaction(vendor_code, source_code, amount, leaf)

        return jsonify({
            "message": "Transaction recorded successfully.",
            "from": vendor_code,
            "to": source_code,
            "amount": amount,
            "leaf": leaf
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# [Endpoint] Check if the system is balanced (total acid tracked)
@app.route('/balance', methods=['GET'])
def check_balance():
    """
    Response:
    {
        "status": "Balanced" or "Anamoly"
    }
    """
    status = group.balance()
    return jsonify({"status": status}), 200

# [Endpoint] Get the full blockchain state
@app.route('/get-chain', methods=['GET'])
def get_chain():
    """
    Response:
    {
        "structure": {...},
        "sources": {...},
        "blocks": {
            "source_code": {
                "amount": ...,
                "hash": ...
            },
            ...
        }
    }
    """
    try:
        structure = {k: list(v) for k, v in group.structure.items()}
        sources = dict(group.sources)
        blocks = {
            k: {
                "amount": v.amount,
                "hash": v.hash
            } for k, v in group.block.items()
        }

        return jsonify({
            "structure": structure,
            "sources": sources,
            "blocks": blocks
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True)
