create table candle
(
    market          varchar   not null,
    unit            varchar   not null,
    datetime        timestamp not null,
    open_price      float8    not null,
    high_price      float8    not null,
    low_price       float8    not null,
    close_price      float8    not null,
    create_datetime timestamp not null,
    update_datetime timestamp not null,
    acc_trade_price     float8    not null,
    acc_trade_volume    float8    not null,
        constraint candle_pk
            unique (market, unit, datetime)
);

