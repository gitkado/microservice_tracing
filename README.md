# microservice_tracing

### Sample applications

```shell
# Build
$ docker-compose build --no-cache
# Up
$ docker-compose up
# Down
$ docker-compose down
# Request
$ curl http://127.0.0.1:5000
$ curl http://127.0.0.1:5000/request_github
# JaegerWebGUI
$ open -a "Google Chrome" http://localhost:16686
```

### TODO

- Fix to Log format key name 
- Add span log in app.py
- Add the second of application container to docker-compose.yml

### Reference

- [JaegerOfficial](https://www.jaegertracing.io/docs/1.21/getting-started/)
- [Github: JaegerClientPython](https://github.com/jaegertracing/jaeger-client-python#getting-started)
- [Github: FlaskOpentracing](https://github.com/opentracing-contrib/python-flask#usage)
- [Tutorial: Tracing Python Flask requests with OpenTracing](https://scoutapm.com/blog/tutorial-tracing-python-flask-requests-with-opentracing)
- [DatadogTracing](https://docs.datadoghq.com/ja/tracing/connect_logs_and_traces/python/)
