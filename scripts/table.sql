create table candle
(
    market          varchar   not null,
    unit            varchar   not null,
    datetime        timestamp not null,
    open_price      float     not null,
    high_price      float     not null,
    low_price       float     not null,
    last_price      float     not null,
    create_datetime timestamp not null,
    update_datetime timestamp not null,
    constraint candle_pk
        unique (market, unit, datetime)
);

