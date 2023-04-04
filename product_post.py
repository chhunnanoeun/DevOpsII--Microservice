
from flask import Flask,  request, jsonify
import product_item as prod

app = Flask(__name__) 

@app.route('/delete/<name>', methods=["DELETE"])
def create():
  name = request.form.get('name')
  category = request.form.get('category')
  price = request.form.get('price')
  warehouse = request.form.get('warehouse')

  _user = prod.get_products()
  data = [x for x in _user if x['name']==name]
  
  if (data):
    return jsonify({'email': 'can not create item.'}),401
  else:
    prod.add_product(name,category,price,warehouse)
  
  if __name__=='__main__':
    app.run(host='0.0.0',port=5000, debug=True)

  


  



    
    
      
