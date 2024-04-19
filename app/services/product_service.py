from db import db
from app.models import ProductModel
from .base_service import BaseService
from sqlalchemy import or_, and_

class ProductService(BaseService):
    def __init__(self) -> None:
        super().__init__(ProductModel)

    def add_product_with_this(self, items: dict) -> dict:
        for item in items["data"]:
            item["product_name"] = self.get_product_name_by_id(item["product_id"])
        return items
    
    def get_product_name_by_id(self,product_id):
        return ProductModel.query.filter_by(id=product_id).first().product_name
    
        
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
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 10))
    
        query = self.model.query
    
        # Apply filters
        category_filter = request.args.get('category')
        print(category_filter)
        if category_filter:
            query = query.filter(self.model.category_id == int(category_filter))
    
        brand_filter = request.args.get('brand')
        if brand_filter:
            query = query.filter(self.model.brand == brand_filter)
    
        price_filter = request.args.get('price')
        if price_filter == 'less_than_1000':
            query = query.filter(self.model.price < 1000)
        elif price_filter == '1000_to_5000':
            query = query.filter(and_(self.model.price >= 1000, self.model.price <= 5000))
        elif price_filter == '5000_to_10000':
            query = query.filter(and_(self.model.price >= 5000, self.model.price <= 10000))
        elif price_filter == 'more_than_10000':
            query = query.filter(self.model.price > 10000)
    
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