
from flask import Flask, render_template

from controllers.wines_controller import wines_blueprint
from controllers.producers_controller import producers_blueprint

from repositories import producer_repository
from repositories import wine_repository

from models.wine import Wine
from models.producer import Producer

app = Flask(__name__)

app.register_blueprint(wines_blueprint)
app.register_blueprint(producers_blueprint)

@app.route('/')
def home():
    producers = producer_repository.select_all()
    wines = wine_repository.select_all()

    return render_template('index.html', all_wines = wines, all_producers = producers)

if __name__ == '__main__':
    app.run(debug=True)

#  MVP..

#  The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.. 
#  class Wine:

#  [ Finalised ] 

#  The inventory should track manufacturers, including a name, and any other appropriate details.. 
#  class Producer:

#  [ Finalised ] 

#  The shop can sell anything you like, but you should be able to create and edit manufacturers, and products separately.. 
#  wine_repository, producer_repository, key functions..

# 	def save():, def delete_all():, def delete(id):, def select_all():, def select(id):, def update():

#  [ Finalised ] 

#   This might mean that it makes more sense for a car shop to track makes, and models of cars.. 
#   Or a bookstore might sell books by author, or by publisher, and not by manufacturer.. 
#   You are free to name classes, and tables as appropriate to your project..

#  [ Finalised ] 

#   Show an inventory page, listing all the details for all the products in stock in a single view..

#  [ Finalised ] 

#   As well as showing stock quantity as a number, the app should visually highlight "low stock", and "out of stock" items to the user..

#  [ Finalised ] 

#  EXTENSIONS..

#  Calculate the markup on items in the store, and display it in the inventory..

#  [ Finalised ] 

#  Mark manufacturers as active/deactivated. Deactivated manufacturers will not appear when creating new products..

#  [ Finalised ] 
    
#  Filter the inventory list by manufacturer. For example, provide an option to view all books in stock by a certain author..

#  [ Finalised ] 

#  Categorise your items. Books might be categorised by genre (crime, horror, romance...)
#  Cars might be categorised by type (SUV, coupé, hatchback...). 
#  Provide an option to filter the inventory list by these categories..


