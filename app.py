import os
import pandas as pd
from sklearn.externals import joblib
from flask import Flask, request, jsonify, render_template, \
                    make_response, send_from_directory, abort, flash, redirect


app = Flask(__name__)


@app.route('/ca/getpredictions', methods=["POST"])
def predict():

    __feature_values = request.get_json()
    __input_cols = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked_S', 'Embarked_C']
    __input_df = pd.DataFrame(__feature_values, columns=__input_cols)
    __model = joblib.load('model_python.pkl')
    __predictions = __model.predict_proba(__input_df)[:, -1]

    return jsonify({'prediction': list(__predictions)})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)