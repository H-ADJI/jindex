import databases
import sqlalchemy

import ormar


class Query(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    location: str = ormar.String(max_length=20)
    search_term: str = ormar.String(max_length=20)
