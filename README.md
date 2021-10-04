# Dataframe to google spreadsheet

Este repositorio muestra el uso de la biblioteca **gspread-pandas** para crear un spreadsheet de google a partir de un dataframe de pandas.

## Dependencias

1. pandas
2. numpy
2. [gspread](https://github.com/burnash/gspread)
3. [gspread_pandas](https://github.com/aiguofer/gspread-pandas)


## Instalación

Instalar mediante pip:

```
$ pip install gspread-pandas
```

O clonar el repo:

```
$ git clone https://github.com/aiguofer/gspread-pandas.git
$ python setup.py install
```

Antes de usar, es necesario descargar las credenciales de Google Client.


## Credenciales de Google Client

Para que un script use Google Drive API primero tenemos que autentificarnos en google, para ello, es necesario crear un proyecto y generar las credenciales. Use el navegador web para ir a [Google Console](https://console.cloud.google.com/):


- Elija **crear proyecto** en el menú de la parte superior:

  - Aparece una ventana de diálogo, elija nombre el proyecto y dé click en el botón de crear.
  - En el menú de la izquierda, click en **APIs & Services**.
  - Se muestra una tabla con las APIs disponibles. Click en el botón **Enable API** y haga lo mismo para **Sheets API**
  - En el menú de la izquierda, sección **OAuth consent screen** seleccione su email y nombre del producto. Click en el botón Save.

- En la sección **Credentials** click en **Add credentials** y seleccione **OAuth client ID**:
    - Select Application type item as Other and give it a name.
    - Click on Create button.
    - Click on Download JSON icon on the right side of created OAuth client IDs and store the downloaded file on your file system.

- Move the downloaded JSON to **~/.config/gspread_pandas/google_secret.json** (UNIX) or **%APPDATA%\gspread_pandas\google_secret.json** (Windows).

**Advertencia:** El archivo *.json contiene llaves privadas, compartirlo equivale a dar acceso al drive de google.

**Nota:** Existen distintos tipos de autentificación. Para ver las diferencias entre ellos ir [aquí](https://stackoverflow.com/questions/39181501/whats-the-difference-between-api-key-client-id-and-service-account).



## Documentación

1. [gspread documentation](https://docs.gspread.org/en/latest/)
3. [gspread-pandas documentation](https://gspread-pandas.readthedocs.io/en/latest/gspread_pandas.html)


## Contacto

Jesús Castrejón (jesus.castrejon@comimsa.com)

