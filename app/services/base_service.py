from db import db
from sqlalchemy import String, or_


class BaseService:
    def __init__(self, model) -> None:
        self.model = model

    def get(self, request, columns):
        # Get parameters from the request
        start = int(request.args.get("start"))
        length = int(request.args.get("length"))
        search_value = request.args.get("search[value]")
        order_dir = request.args.get("order[0][dir]")
        order_column_index = int(request.args.get("order[0][column]") or "0")
        sort_column = columns[order_column_index]

        # Base query
        query = self.model.query

        # search should applied to only string columns
        string_columns = [
            c.name for c in self.model.__table__.columns if isinstance(c.type, String)
        ]

        # define an empty list to store filters
        filter_conditions = []

        for column in columns:
            # add to filter conditions if string column
            if column in string_columns:
                filter_conditions.append(
                    getattr(self.model, column).ilike(f"%{search_value}%")
                )

        # filter search
        query = query.filter(or_(*filter_conditions))

        # sorting order
        if order_dir == "desc":
            query = query.order_by(getattr(self.model, sort_column).desc())
        else:
            query = query.order_by(getattr(self.model, sort_column))

        # Paginate the data
        data = query.offset(start).limit(length).all()

        # Total records without filtering
        total_records = self.model.query.count()

        # Total records after filtering
        filtered_records = query.count()

        # Format the data for DataTables
        formatted_data = [
            {
                key: getattr(item, key)
                for key in item.__dict__
                if not key.startswith("_")
            }
            for item in data
        ]

        return {
            "recordsTotal": total_records,
            "recordsFiltered": filtered_records,
            "data": formatted_data,
        }

    def create(self, **kwargs):
        entity = self.model(**kwargs)
        db.session.add(entity)
        db.session.commit()
        return entity

    def get_by_id(self, id):
        return self.model.query.get(id)

    def update(self, id, **kwargs):
        entity=self.get_by_id(id)
        for key, value in kwargs.items():
            setattr(entity, key, value)
        db.session.commit()
        return entity

    def status(self,id):
        entity=self.get_by_id(id)
        if not entity.is_active:
            entity.is_active=True
        else:
            entity.is_active=False
        db.session.commit()
        return entity.is_active
    
    def get_active(self):
        return self.model.query.filter_by(is_active=True).all()