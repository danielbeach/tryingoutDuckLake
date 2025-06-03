## Playing with DuckLake

Recently `DuckDB` entered the Lake House format war with `DuckLake`,
this repo simply uses Docker to setup a `DuckLake` backed by a `Postgres` 
database and play around with it.

We create a table in DuckLake based on some sample data, and then
we query that table along with the backend catalog tables created in
Postgres and used by `DuckLake` to get a feel for what is happening.

`docker-compose up --build` once you clone this repo will build all images and run the code.