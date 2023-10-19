# flask boiler

Barebones backend server running on flask, mysql, and redis

## setup

```
docker-compose up
```

## routes

1. /v1/run_pipeline 
    * methods=["PUT"]
    * no input
2. /v1/grab_datetimes
    * methods=["GET"]
    * no input
3. v1/grab_one_datetime
    * methods=["GET"]
    * input json with key "datetime_id"

## resources
* https://dev.mysql.com/doc/mysql-getting-started/en/
* https://github.com/UCB-INFO-BACKEND-WEBARCH/spring-22-labs/tree/main