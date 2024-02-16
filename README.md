# PROJET FINAL EXPLOITATION DE DONNÉES BARNABÉ PILLIAUDIN

# Introduction
This project is about cretating an api for a room booking system. The data is stored in a
mysql database, and the api is created using Flask.

# Installation
First, rename `.env.example` to `.env`, `.env.mysql.example` to `.env.mysql`, and fill the variables with your own values.  

To run the project you can use Docker.

To start run 
```bash 
docker-compose up --build
```
It will build the image, create and start the containers for both api and database.

The migrations are commited in the repository, so you don't need to run `flask db init` and `flask db migrate`.  
Just run `flask db upgrade` to create the tables in the database.

Then you can do POST request to `/api/seeds/[number]` to generate random data in the database,`number` is number of records that will be generated in the database.

# DATE FORMAT

The date format is `YYYY-MM-DD` for example `2021-12-31`

# Routes
Types are checked and the types are not correct the api sill return a 400 error.

__*POST*__ `/api/seeds/<int:number_of_seeds>`: Run the seeds
__*POST*__ `/api/reservations`: Create a Booking. Required body {id_client:int, id_chambre:int, date_arrivee:string, date_depart:string}
__*DELETE*__ `/api/reservations/<int:id>`: Delete a Booking
__*GET*__ `/api/chambres/disponibles`: Return the available rooms for a given period. Required body {date_arrivee:string, date_depart:string}
__*POST*__ `/api/chambres`: Create a room. Required body {numero:int, prix:float, capacite:int}
__*PUT*__ `/api/chambres/<int:room_id>` Edit a room. No required body
__*DELETE*__ `/api/chambres/<int:room_id>` Delete a room


# Schema
In `utils.py` if you struggle to understand the condition this schema could help you.  
![Schema of cases of a room not available](img/schema-reservation.png)