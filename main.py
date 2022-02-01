from website import create_app

app = create_app()

if __name__ == '__main__':  #only if we run this file, it will execute the line below
    app.run(debug = True)   #this line shows that everytime we change a code, the system will rerun


