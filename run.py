from app import create_app

myapp_obj = create_app()  

if __name__ == "__main__":
    myapp_obj.run(debug=True)

