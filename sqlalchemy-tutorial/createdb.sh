docker run --name sqlalchemy-orm-psql \
    -e POSTGRES_PASSWORD=pass \
    -e POSTGRES_USER=usr \
    -e POSTGRES_DB=sqlalchemy \
    -p 5432:5432 \
    -d postgres

# stop instance
docker stop sqlalchemy-orm-psql

# destroy instance
docker rm sqlalchemy-orm-psql