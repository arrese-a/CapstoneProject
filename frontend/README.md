# Recetario de la Abuela (Grandma’s cookbook) - Frontend

Grandma’s cookbook is a web application designed to be a recipe book.  It is a place where you can share your recipes and create your shopping lists from the recipes that you want to cook. You can also read all the recipes available in the platform.

This is the frontend repository of Grandma's cookbook. The project was built using React and Vite, and the calls to the backend are made with Axios. PostgreSQL database is used to access and store the data.

## What can you do in the application?

**All users** can:
* Read all the recipes in the platform, with their preparation, list of ingredients and estimated cooking time.
* Search the recipes by ingredients
* Sign-up to the application to access enhanced features

**Authenticated users** have enhanced features:
* Recipe creation: users can create and submit new recipes to the platform 
* Favorite list: users can add recipes to their personal list of favorites by just clicking the star in the recipe page. 
* Shopping list: authenticated users can add recipe’s ingredients to a personal shopping list by clicking the cart icon. Ingredients can be removed if they are not needed in the list. 