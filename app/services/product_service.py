from db import db
from app.models import ProductModel
from .base_service import BaseService
from sqlalchemy import or_, and_
from datetime import datetime, timedelta


class ProductService(BaseService):
    def __init__(self) -> None:
        super().__init__(ProductModel)

    def add_product_with_this(self, items: dict) -> dict:
        for item in items["data"]:
            item["product_name"] = self.get_product_name_by_id(item["product_id"])
            item["product_img_urls"] = self.get_product_img_by_id(item["product_id"])
            item["stock"] = self.get_product_stock_id(item["product_id"])
        return items

    def get_product_name_by_id(self,product_id):
        return ProductModel.query.filter_by(id=product_id).first().product_name

    def get_latest_products(self):
        return ProductModel.query.filter_by(is_active=True).order_by(ProductModel.id.desc()).limit(10).all()

    def get_products_by_category(self,category_id):
            return ProductModel.query.filter_by(category_id=category_id,is_active=True).order_by(ProductModel.product_name).all()


    def get_product_img_by_id(self,product_id):
        return ProductModel.query.filter_by(id=product_id).first().product_img_urls

    def get_active(self):
        return ProductModel.query.filter_by(is_active=True).order_by(ProductModel.product_name).all()

    #order creation
    def get_total_price(self,request):
        product_id = int(request.args.get("product_id"))

        quantity = int(request.args.get("quantity"))

        product=self.get_by_id(product_id)
        if product is None:
            return {"error": "Product not found"}

        discount=product.discount
        price=product.price

        total_price=float((price-discount)*quantity)

        price_calculated_data={
            'product_id':product_id,
            'price':price,
            'discount':discount,
            'quantity':quantity,
            'total_price':total_price
        }
        return price_calculated_data


    def get_product_details_by_ids(self,product_ids):
        try:
            # Query the database to get product details for the given product ids
            products = self.model.query.filter(self.model.id.in_(product_ids)).all()

            # Return list of product details
            return products

        except Exception as e:
            raise ValueError(str(e))  # Raise an exception if an error occurs

    def get_all_brands(self):
        brands= db.session.query(ProductModel.brand).distinct().all()
        brand_names = [brand[0] for brand in brands]
        return brand_names

    def get_filtered_list(self, request, columns):
        page = int(request.args.get('page'))
        page_size = int(request.args.get('page_size'))

        query = self.model.query.filter(self.model.is_active == True)

        category_filters = request.args.getlist('category[]')
        if len(category_filters)>0 and category_filters[0]:
            category_ids = [int(cat) for cat in category_filters]
            query = query.filter(self.model.category_id.in_(category_ids))

        # Apply brand filters
        brand_filters = request.args.getlist('brand[]')
        if brand_filters:
            query = query.filter(self.model.brand.in_(brand_filters))

        # Apply price filters
        price_filters = request.args.getlist('price[]')
        price_filter_queries = []
        for price_filter in price_filters:
            if price_filter == 'less_than_1000':
                price_filter_queries.append(((self.model.price - self.model.discount) < 1000))
            elif price_filter == '1000_to_5000':
                price_filter_queries.append(and_((self.model.price - self.model.discount) >= 1000, (self.model.price - self.model.discount) <= 5000))
            elif price_filter == '5000_to_10000':
                price_filter_queries.append(and_((self.model.price - self.model.discount) >= 5000, (self.model.price - self.model.discount) <= 10000))
            elif price_filter == 'more_than_10000':
                price_filter_queries.append((self.model.price - self.model.discount) > 10000)

        # Apply accumulated price filters using 'or_' operator
        if price_filter_queries:
            query = query.filter(or_(*price_filter_queries))

        sorting_option = request.args.get('sort_by')
        if sorting_option == 'latest':
            query = query.order_by(self.model.created_at.desc())
        if sorting_option == 'popularity':
            query = query.order_by(self.model.created_at.desc())
        elif sorting_option == 'price_low_to_high':
            query = query.order_by((self.model.price - self.model.discount).asc())
        elif sorting_option == 'price_high_to_low':
            query = query.order_by((self.model.price - self.model.discount).desc())

        # Perform pagination after filtering
        paginated_query = query.paginate(page=page, per_page=page_size, error_out=False)
        paginated_data = paginated_query.items

        # Format data
        formatted_data = [{key: getattr(item, key) for key in columns} for item in paginated_data]

        return {
            "recordsTotal": paginated_query.total,
            "recordsFiltered": len(paginated_data),
            "data": formatted_data,
            "page": page,
            "total_pages": paginated_query.pages
        }

    def get_available_pincodes(self,request):
        product_id = int(request.args.get("product_id"))
        product = self.get_by_id(product_id)
        if product:
            return ProductModel.query.filter_by(id=product_id).first().available_area_pincodes
        return None

    def serialized_products(self, products_item):
        if products_item:
            serialized_products_item = {key: getattr(products_item, key) for key in products_item.__dict__.keys() if not key.startswith("_")}
            return serialized_products_item
        else:
            return None

    def get_all_products(self,time_range):
           end_date = datetime.now()
           if time_range == 'Weekly':
               start_date = end_date - timedelta(days=end_date.weekday())
           elif time_range == 'Monthly':
               start_date = end_date.replace(day=1)- timedelta(days=1)
           elif time_range == 'Yearly':
               start_date = end_date.replace(month=1, day=1)

           total_products = ProductModel.query.filter(
               ProductModel.created_at >= start_date,
               ProductModel.created_at <= end_date,
               ProductModel.is_active==True
           ).count()

           return total_products

        
    def get_product_details_by_ids_dict(self, product_ids):
        product_details = []

        # Populate the list with dictionaries containing product IDs
        for product_id in product_ids:

            product = self.get_by_id(id=product_id)
            product_details.append({"product_id": product.id,"stock":product.stock})

        # Return list of product details dictionaries
        return product_details
    
    def get_product_stock_id(self,product_id):
        return ProductModel.query.filter_by(id=product_id).first().stock

