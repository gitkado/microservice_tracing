import os

from flask import Flask, jsonify
from flask_opentracing import FlaskTracing
from jaeger_client import Config
import requests


def init_tracer():
    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'local_agent': {
                'reporting_host': 'jaeger',
                'reporting_port': 6831,
            },
            'logging': True,
        },
        service_name='first_python',
        validate=True,
    )
    return config.initialize_tracer()


app = Flask(__name__)
FlaskTracing(tracer=init_tracer(), trace_all_requests=True, app=app)


@app.route("/")
def hello():
    return jsonify({
        "message": "Hello Flask World."
    })


@app.route("/request_github")
def request_github():
    github_uri = "https://github.com"

    # TODO: span
    app.logger.info("RequestStart: {0}".format(github_uri))
    result = requests.get(github_uri)
    app.logger.info("RequestFinish: {0}".format(github_uri))

    return jsonify({
        "message": "Request Github Success.",
        "result": result.status_code
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
