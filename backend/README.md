# Recetario de la Abuela (Grandma’s Cookbook) - Backend

Grandma’s Cookbook is a web application designed to be a recipe book.  It is a place where you can share your recipes and create your shopping lists from the recipes you want to cook. You can also read all the recipes available on the platform.

This is the backend repository of Grandma's cookbook. 

## How does the backend work?
The backend is built using Python and FastAPI, and it is connected to the frontend using Axios. In addition, the data is stored in a PostgreSQL database.
There are different endpoints depending on the table being accessed.

### Endpoints 

| Endpoint | Description | Requires Auth |
| :--- | :--- | :--- |
| **Recetas** |  |  |
| `GET /recetas` | Gets all the recipes, it can be filtered by ingredients | No |
| `GET /recetas/{receta_id}` | Gets a recipe by its ID | No |
| `POST /recetas/` | Creates a new recipe | Yes |
| **Session** |  |  |
| `GET /sesion/check-login` | Check if there is a valid session | No |
| `POST /sesion/signup` | Sign up a new user | No |
| `POST /sesion/login` | Login with a existing user | No |
| `POST /sesion/logout` | Delete the session from memory and delete the cookie | Yes |
| **Lista de compra (shopping list)** |  |  |
| `GET /lista-compra/obtener/{usuario_id}` | Get the shopping cart of a user| Yes |
| `POST /lista-compra/agregar` | Add the ingredients of a recipe to the shopping list of the user| Yes |
| **Favorites** |  |  |
| `GET /favoritas/{usuario_id}` | Get the favorite recipes of a user| Yes |
| `GET /favoritas/favorita-check/{usuario_id}/{receta_id}` | Check if a recipe is on the list of favorites of a user| Yes |
| `POST /favoritas/{usuario_id}/{receta_id}` | Add a recipe to the favorite list of a user| Yes |
| `DELETE /favoritas/{usuario_id}/{receta_id}` | Remove a recipe to the favorite list of a user| Yes |

### SeedData
The `seedData.py` file includes seed data (users, recipes, shopping lists, and favorites) pre-populated to provide the necessary content to thoroughly test all application features.
