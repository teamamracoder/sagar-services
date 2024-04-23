from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateProductForm,UpdateProductForm
from app.services import ProductService
from app.services import CategoryService,ProductQnAService,ProductReviewService
from datetime import datetime
from app.constants import payment_methods
from app.auth import get_current_user
from app.utils import FileUtils
from app.services import CartService
from app.services import WishlistService


class ProductController:
    def __init__(self) -> None:
        self.product_service = ProductService()
        self.category_service = CategoryService()
        self.product_qna_service = ProductQnAService()
        self.product_review_service = ProductReviewService()
        self.cart_service = CartService()
        self.wishlist_service = WishlistService()

    def get(self):
        return render_template("admin/product/index.html")

    def get_product_data(self):
        columns = ["id", "product_name", "brand","model","price","discount","stock","created_by","created_at","updated_by", "updated_at", "is_active", "category_id", "product_img_urls"]
        data = self.product_service.get(request, columns)
        combined_data = self.category_service.add_category_with_products(data)
        return jsonify(combined_data)

    def create(self):
        logged_in_user,roles=get_current_user().values()
        form = CreateProductForm()
        categories=self.category_service.get_active()
        form.category_id.choices = [(category.id, category.category_name) for category in categories]
        form.payment_methods.choices = payment_methods.get_all_items()
        if form.validate_on_submit():
            filepath=FileUtils.save('products',form.product_img_urls.data)
            if isinstance(filepath,str):
                filepath=[filepath]
            pincode_string = form.available_area_pincodes.data
            pincode_list = [pin.strip() for pin in pincode_string.split(',')]
            self.product_service.create(
                created_by=logged_in_user.id,
                created_at=datetime.now(),
                product_name=form.product_name.data,
                brand=form.brand.data.capitalize(),
                model=form.model.data,
                price=form.price.data,
                discount=form.discount.data,
                stock=form.stock.data,
                sort_description=form.sort_description.data,
                product_img_urls=filepath,
                specifications=form.specifications.data,
                payment_methods=form.payment_methods.data,
                available_area_pincodes=pincode_list,
                category_id=form.category_id.data,
                # return_policy=form.return_policy.data
            )
            return redirect(url_for("product.index"))
            # return render_template("admin/product/add.html", form=form, error="Product already exists")
        return render_template("admin/product/add.html", form=form)

    def update(self, id):
        logged_in_user,roles=get_current_user().values()
        product = self.product_service.get_by_id(id)
        if product is None:
            return render_template("admin/error/something_went_wrong.html")

        categories=self.category_service.get_active()
        form = UpdateProductForm(obj=product)
        form.category_id.choices = [(category.id, category.category_name) for category in categories]
        form.payment_methods.choices = payment_methods.get_all_items()

        if form.validate_on_submit():
            filepath=product.product_img_urls
            new_filepath=FileUtils.save('products',form.product_img_urls.data)
            if isinstance(new_filepath,str):
                new_filepath=[new_filepath]
            all_filepath=filepath+new_filepath
            pincode_string = form.available_area_pincodes.data
            pincode_list = [pin.strip() for pin in pincode_string.split(',')]
            updated_data = {
                'category_id': form.category_id.data,
                'product_name': form.product_name.data,
                'brand': form.brand.data.capitalize(),
                'model': form.model.data,
                'price': form.price.data,
                'discount': form.discount.data,
                'stock': form.stock.data,
                'sort_description': form.sort_description.data,
                'product_img_urls': all_filepath,
                'specifications': form.specifications.data,
                'payment_methods': form.payment_methods.data,
                'available_area_pincodes': pincode_list,
                # 'return_policy': form.return_policy.data,
                'updated_at': datetime.now(),
                'updated_by': logged_in_user.id
            }
            self.product_service.update(id, **updated_data)
            return redirect(url_for("product.index"))

        form.available_area_pincodes.data = ', '.join(product.available_area_pincodes)
        return render_template("admin/product/update.html", id=id, form=form)

    def status(self, id):
        product = self.product_service.get_by_id(id)
        if product is None:
            return {"status":"error","message":"Product Not Found"}
        is_active=self.product_service.status(id)
        if is_active:
            return {"status":"success","message":"Product Activated","data":is_active}
        return {"status":"success","message":"Product Deactivated","data":is_active}

    def get_total_price(self):
        price_calculated_data=self.product_service.get_total_price(request)
        return jsonify(price_calculated_data)

    def get_available_pincodes(self):
        available_pincodes=self.product_service.get_available_pincodes(request)
        if available_pincodes:
            return jsonify({'status': 'success', 'pincodes': available_pincodes})
        return jsonify({'status': 'error', 'message':'Not available','pincodes': [None]})


    def details(self,id):
        product=self.product_service.get_by_id(id)
        return render_template("admin/product/details.html",product=product)



     ## customer controllers ##

    def products_page(self):
        categories = self.category_service.get_active()
        brands = self.product_service.get_all_brands()
        return render_template("customer/products.html", categories=categories, brands = brands)

    def products_page_data(self):
        logged_in_user,roles=get_current_user().values()
        columns = ["id", "product_name", "brand","model","price","discount","stock", "product_img_urls"]
        data = self.product_service.get_filtered_list(request, columns)
        data = self.product_review_service.get_reviews_by_product(data)
        try:
            data = self.cart_service.add_cart_with_user_and_product(logged_in_user.id,data)
            data = self.wishlist_service.add_wishlist_with_user_and_product(logged_in_user.id,data)
            return jsonify(data)
        except Exception as e:
            return jsonify(data)
        finally:
            print(data)


    def product_details_page(self,product_id):
        logged_in_user,roles=get_current_user().values()
        product = self.product_service.get_by_id(product_id)
        product_reviews = self.product_review_service.get_review_by_product_id(product_id)
        if product:
            try:
                cart=self.cart_service.get_cart_item_by_user_id_product_id(logged_in_user.id,product_id)
                if cart.is_active:
                    return render_template("customer/product_details.html", product=product, product_reviews=product_reviews, cart=cart)
                return render_template("customer/product_details.html", product=product, product_reviews=product_reviews)
            except Exception as e:
                return render_template("customer/product_details.html", product=product, product_reviews=product_reviews)
        return render_template("error/page_not_found.html")