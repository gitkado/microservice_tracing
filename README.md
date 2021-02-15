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
```

### Jaeger

```shell
$ docker run --rm -d --name jaeger \
   -p 6831:6831/udp \
   -p 16686:16686 \
   jaegertracing/all-in-one:1.21
$ open -a "Google Chrome" http://localhost:16686
```

https://www.jaegertracing.io/docs/1.21/getting-started/

### TODO

- Add the Jaeger container to docker-compose.yml
- Use the Jaeger Client in the first of application
- Add the second of application container to docker-compose.yml
