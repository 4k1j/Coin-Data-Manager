# CDM
### Coin Data Manager


# API
## Upbit
https://docs.upbit.com/docs/create-authorization-request


# Producer
```shell
docker build --tag consume_candle -f consume_candle.Dockerfile .
docker build --tag produce_candle -f produce_candle.Dockerfile .


docker run -d --name btc_producer -e MARKET=KRW-BTC -e ENV=prod --net host produce_candle:latest
docker run -d --name btc_consumer -e MARKET=KRW-BTC -e ENV=prod --net host consume_candle:latest
```

# Backend
```shell
docker build --tag producer_manager_backend -f backend.Dockerfile .
docker run -p 8000:8000 -d --name producer_manager_backend producer_manager_backend:latest
```