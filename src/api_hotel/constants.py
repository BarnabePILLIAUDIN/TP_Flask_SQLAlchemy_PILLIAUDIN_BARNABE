# Limit the possible types of rooms and status of booking to make the seed more coherent
SEED_TYPE_OF_ROOMS = ['simple', 'double', 'suite', "delux", 'presidentielle']
STATUS_OF_BOOKING = ['Confirmee', 'annulee', 'En cours de validation']
CREATE_ROOMS_FIELDS = [
    {
        "name": "numero",
        "type": int,
        "required": True,
    },
    {
        "name": "type",
        "type": str,
        "required": True,
    },
    {
        "name": "prix",
        "type": float,
        "required": True,
    }
]

GET_AVAILABLE_ROOMS_FIELDS = [
    {
        "name": "date_arrivee",
        "type": str
    },
    {
        "name": "date_depart",
        "type": str
  }
]

CREATE_BOOKING_FIELDS = [
        {
            "name": "date_arrivee",
            "type": str
        },
        {
            "name": "date_depart",
            "type": str
        },
        {
            "name": "id_client",
            "type": int
        },
        {
            "name": "id_chambre",
            "type": int
        }
]
