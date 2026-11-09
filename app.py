#Este archivo es súper liviano; su único trabajo es importar 
#la función que crea la aplicación desde la carpeta src y ponerla a correr.


from src import create_app

app = create_app()

print(app.url_map)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    