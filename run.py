import os
from Flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
        return "Hello, world"
    
 if __name == "__main__":
     app.run(
    

     )
     
     
     
     
     