from django.shortcuts import render, redirect
import requests
from .forms import InventoryForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import User_Info as usersmodel, Inventory as inventoriesmodel, IngredientsSpecific as ingredientsmodel, IngredientsGeneric as ingredientsgenericmodel
from leaderboard.models import Leaderboard
from django.utils import timezone
from django.http import JsonResponse
from .models import IngredientsSpecific
from django.shortcuts import render, redirect, get_object_or_404

import json

API_KEY = 'E1CIuhXJ0zF0Cc3pRw/zqw==1ToroclEYuWAnJdT'

@login_required
#Whenever a user registers it will redirect them to this view.
#This method sets up the user_info and inventory objects whenever a new user registers
#This method allows users to add food to their inventory
#This method allows users to update current food stock in their inventory
def inventory(request):
    context = {}
    if (not usersmodel.objects.filter(id = request.user.id).first()):
        newUser = usersmodel.objects.create(id = request.user.id)
        newUser.save()
    if (not inventoriesmodel.objects.filter(id = request.user.id).first()):
        user_info = usersmodel.objects.get(id=request.user.id)
        newInventory = inventoriesmodel.objects.create(id = request.user.id, userID = user_info) 
        newInventory.save()
    user_info = usersmodel.objects.get(id=request.user.id)
    inventory = inventoriesmodel.objects.get(id=request.user.id)
    form = InventoryForm(request.POST or None)

    # Leaderboard 
    try:
        leaderboard_person = Leaderboard.objects.get(userID=user_info)
    except Leaderboard.DoesNotExist:
        leaderboard_person = Leaderboard.objects.create(userID=user_info)

    current_time = timezone.now().date()
    expired_objects = ingredientsmodel.objects.filter(inventoryID=inventory,expiryDate__lt=current_time)
    for expired_object in expired_objects:
        leaderboard_person.score = leaderboard_person.score - expired_object.quantity 
        expired_object.delete() 
        leaderboard_person.save()

    if(request.method == 'POST'):
        form = InventoryForm(request.POST, request.FILES)
        #If form is valid, then save the data to teams database and display success message
        if form.is_valid():
            food = form.cleaned_data['food']
            weight = form.cleaned_data['weight']
            expiry = form.cleaned_data['expiry']
            food = food.lower()
            #If the generic ingredient is new to the whole database, create genericIngredient object
            if (not ingredientsgenericmodel.objects.filter(ingredientName = food).first()):
                genericIngredient = ingredientsgenericmodel.objects.create(ingredientName = food)
                genericIngredient.save()
            #Otherwise get the genericIngredient object that already exists within the database
            else:
                genericIngredient = ingredientsgenericmodel.objects.get(ingredientName = food)
            #If the specific ingredient that wants to be added is new to the user's inventory
            if (not ingredientsmodel.objects.filter(inventoryID = inventory, ingredientID = genericIngredient, expiryDate = expiry)):
                #If weight less than 0, then it is an error
                if weight < 0:
                    return redirect('inventory')
                #Create new specific ingredient object inside user's inventory
                newSpecefic = ingredientsmodel.objects.create(inventoryID = inventory, ingredientID = genericIngredient, expiryDate = expiry, quantity = weight )
                newSpecefic.save()
            #Otherwise update the existing specific ingredient object by adding or subtracting the weight
            else:
                oldIngredient = ingredientsmodel.objects.get(inventoryID = inventory, ingredientID = genericIngredient, expiryDate = expiry)
                #If the weight goes lower than 0 delete the whole object
                if (weight < 0 and oldIngredient.quantity + weight <= 0):
                    oldIngredient.delete()
                    leaderboard_person.score += (-weight)
                    leaderboard_person.save()
                #Otherwise add the weight to the specific ingredient's current weight
                else:
                    oldIngredient.quantity += weight
                    oldIngredient.save()
                    if(weight<0):
                        leaderboard_person.score += (-weight)
                        leaderboard_person.save()
            return redirect('inventory')

    foods = []
    for ingredient in ingredientsmodel.objects.filter(inventoryID = inventory):
        name = ingredientsgenericmodel.objects.get(id = ingredient.ingredientID.id).ingredientName
        food = {
            'name' : name,
            'weight' : ingredient.quantity,
            'expiry' : ingredient.expiryDate
        }
        foods.append(food)
    context['form'] = form
    context['inventory'] = foods
    return render(request, 'inventory/inventory.html', context)

@login_required
def impact(request):
    context = {}
    return render(request, 'inventory/impact.html', context)

@login_required
#This method returns recipes recommendations and nutritional data to the user based on their inventory
def recipes(request):
    context = {}
    ID = request.user.id
    nutritionInfo = []
    recipeQuery = ''

    # Check if there are any ingredients in the inventory
    inventory_items = ingredientsmodel.objects.filter(inventoryID = ID)
    if not inventory_items.exists():
        context['message'] = 'Your inventory is empty. Please add some items.'
        return render(request, 'inventory/recipes.html', context)

    # If there are ingredients, proceed as before
    for food in inventory_items:
        foodName = ingredientsgenericmodel.objects.filter(id = food.ingredientID.id).first().ingredientName
        weight = food.quantity
        query = str(int(weight)) + 'g ' + str(foodName)
        recipeQuery += str(foodName) +'+'
        #For each ingredient, get nutritional information from API and append to nutritionInfo array
        url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        resp = requests.get(url, headers={'X-Api-Key': API_KEY}).json()
        #Change the indexes to the food names
        resp[0].update({"weight": str(weight)})
        nutritionInfo.append(resp)

    recipes = []
    #Query API for recipes
    recipeQuery = recipeQuery.rstrip(recipeQuery[-1])
    url2 = "https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id=2ba59917&app_key=4b87b1b3bb5b06a75104fe8d535cdcbf".format(recipeQuery)
    resp2 = requests.get(url2)
    data = resp2.json()
    resp2 = data['hits']
    #For each recipe, turn it into a dictionary and append it to the recipes array
    for result in resp2:
        recipe = result['recipe']
        toAdd = {
            'name' : recipe['label'],
            'image' : recipe['image'],
            'url' : recipe['url'],
            'ingredients' : recipe['ingredientLines'],
            'calories' : recipe['calories'],
            'time' : str(round(int(recipe['totalTime']))) + ' minutes'
        }
        recipes.append(toAdd)
    context['recipes'] = recipes
    context['info'] = nutritionInfo
    return render(request, 'inventory/recipes.html', context)


@login_required
def delete_entry(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        food_id = data.get('foodId')

        try:
            ingredient = get_object_or_404(IngredientsSpecific, id=food_id)
            ingredient.delete()
            return JsonResponse({'message': 'Entry deleted successfully'})
        except:
            return JsonResponse({'error': 'Entry not found'}, status=404)

    return JsonResponse({'error': 'Invalid request'}, status=400)


def calculate_food_cost(food_name):
    # Make a request to the Nutritionix API
    response = requests.get(
        "https://api.nutritionix.com/v1_1/search",
        params={
            "appId": "bef4870d",
            "appKey": "4363582fe9859fc9034f4ac63bc8b97f	",
            "query": food_name,
            "fields": "item_name,nf_calories,nf_total_fat,nf_protein,nf_total_carbohydrate,nf_serving_size_qty,nf_serving_size_unit",
            "sort": {
                "field": "item_name",
                "order": "asc"
            }
        }
    )

    # Parse the response and calculate the cost
    if response.status_code == 200:
        data = response.json()
        food_items = data.get("hits", [])
        
        if food_items:
            food_item = food_items[0]["fields"]
            cost = calculate_cost_from_nutrition_data(food_item)
            return cost

    return None

def calculate_cost_from_nutrition_data(food_item):
    # Perform your own calculations based on the nutrition data
    # and any other factors that determine the cost of the food item
    # You can consider factors such as price per serving, nutrient density, etc.
    # For simplicity, let's assume a constant price per gram of the food item
    price_per_gram = 0.05

    serving_size = food_item.get("nf_serving_size_qty", 1)
    serving_unit = food_item.get("nf_serving_size_unit", "")
    total_weight = serving_size * 1000  # convert serving size to grams
    cost = total_weight * price_per_gram

    return cost

# Example usage
food_name = "Apple"
cost = calculate_food_cost(food_name)
if cost is not None:
    print(f"The cost of {food_name} is $ {cost:.2f}")
else:
    print(f"Failed to calculate the cost of {food_name}")