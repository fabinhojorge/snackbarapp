# Snack Bar App [![CircleCI](https://circleci.com/gh/fabinhojorge/snackbarapp.svg?style=svg)](https://circleci.com/gh/fabinhojorge/snackbarapp)
A simple project with a real business case to practice Django knowledge 


# Introduction
The idea of this project is to study some technologies like:
* Django
* CLI
* Tests
* Django template

# Business
The system should allow the user (_Owner_) to register new products and his ingredients.
Also, the user (_Customer_) can construct his own Snack or Hamburger, and the system should provide the price of the product based in some rules.

As a start, you can use the below list of ingredients and theirs respective prices:

| Ingredient | Price |
|:----------:|-------|
|Bread| _R$2.50_|
|Hamburger of Meat| _R$5.00_|
|Lettuce(_Alface_)| _R$0.80_|
|Bacon| _R$3.00_|
|Egg| _R$1.20_|
|Tomato|_R$1.20_|
|Cheese| _R$2.50_|

To Calculate a Product´s price, you only needed to __sum all the ingredients prices__.
But, there are some __special__ conditions that can change the final price. It´s when the Product belongs to a Promotion. Take a look in the special rules below:

|Promotion| Price Rules| Discount/Charge|
|:---:|---|---|
|__Light__| If the Product have Lettuce but not Bacon|10% of Discount|
|__A lot o Meat__|For each 3 portion of meat| The customer only pays 2 portions of meat|
|__A lot of Cheese__|For each 3 portion of cheese| The customer only pays 2 portions of cheese|


# To Do
[ ] ...
