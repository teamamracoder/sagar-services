from app.models import ProductModel
from .base_service import BaseService

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