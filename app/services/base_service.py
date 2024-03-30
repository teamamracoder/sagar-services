from db import db


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
        query = self.model.query.filter(
            self.model.first_name.ilike(f"%{search_value}%")
            | self.model.email.ilike(f"%{search_value}%")
        )

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
