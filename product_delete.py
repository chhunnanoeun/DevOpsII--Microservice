
from flask import Flask,  request, jsonify
import product_item as prod

app = Flask(__name__) 

@app.route('/delete/<name>', methods=["DELETE"])
def delete(name):
  _user = prod.get_product(name)
  data = [x for x in _user if x["name"]==name]
  if data:
    prod.delete_product(name)
    return jsonify({'email': 'Item deleted successfully.'}),200
  else:
     return jsonify({'email': 'Item deleted successfully.'}),404
  
  if __name__=='__main__':
    app.run(host='0.0.0',port=5000, debug=True)

  


  



    
    
      
