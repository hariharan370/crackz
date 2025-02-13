from flask import Flask, request, render_template
from googlesearch import search



app = Flask(__name__)

def google_search(query):
    try:
        # Get the first result
        for result in search(query, num=1):
            return result
    except Exception as e:
        print(f"An error occurred: {e}") 
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("query")
        result = google_search(query)
        

        
        return render_template("index.html", query=query, result=result)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
