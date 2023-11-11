# flask boiler

Barebones backend server running on flask, mysql, and redis queue

## setup

```
docker-compose up
```

## routes

* ```/v1/run_pipe``` (PUT)
* ```/v1/grab_datetimes``` (GET)
* ```v1/grab_one_datetime``` (GET)

## azure deployment
* https://learn.microsoft.com/en-us/azure/container-instances/tutorial-docker-compose

## resources
* https://dev.mysql.com/doc/mysql-getting-started/en/
* https://github.com/UCB-INFO-BACKEND-WEBARCH/spring-22-labs/tree/main