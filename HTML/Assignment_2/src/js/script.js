let dataP = [];

fetch('https://www.themealdb.com/api/json/v1/1/search.php?s=')
    .then(res => res.json())
    .then(data => {
        dataP = data.meals;
        renderAllFoods(dataP);
    })
    .catch(error => {
        console.error("Error fetching data:", error);
    });

let cart = [];

const renderAllFoods = (foods) => {
    const foodBox = document.getElementById('foods');
    foodBox.innerHTML = '';

    foods.forEach(food => {
        createFoodCard(food);
    });
};

const createFoodCard = (food) => {
    const foodBox = document.getElementById('foods');
    const card = document.createElement('div');
    card.classList.add('card');

    card.innerHTML = `
        <div class="card max-w-xs mx-auto bg-white rounded-lg overflow-hidden z-10 hover:shadow-2xl">
            <img class="w-full h-32 object-cover" src="${food.strMealThumb}" alt="food item" />
            <div class="p-6">
                <div class="flex gap-8">
                    <h2 class="text-xl font-semibold text-gray-800">${food.strMeal}</h2>
                    <button class="text-blue-600 text-sm font-semibold rounded focus:outline-none" onclick="showFoodDetails('${food.strMeal}', '${food.strCategory}', '${food.strArea}', '${food.strMealThumb}', '${food.strIngredient1}', '${food.strMeasure1}', '${food.strIngredient2}', '${food.strMeasure2}', '${food.strIngredient3}', '${food.strMeasure3}', '${food.strIngredient4}', '${food.strMeasure4}', '${food.strIngredient5}', '${food.strMeasure5}')">
                        Info
                    </button>
                </div>
                <p class="mt-2 text-gray-600">Category: ${food.strCategory} <br> Country: ${food.strArea}</p>
                <div class="mt-4 flex justify-between items-center">
                    <span class="text-md font-bold text-yellow-600">$2.99</span>
                    <button class="px-2 py-1 bg-black text-white text-sm font-semibold rounded hover:bg-green-500 focus:outline-none" onclick="addToCart('${food.idMeal}', '${food.strMeal}', '${food.strMealThumb}', this)">
                        Add to Cart
                    </button>
                </div>
            </div>
        </div>
    `;
    foodBox.appendChild(card);
};

const showFoodDetails = (name, cat, area, img, Ing1, Meas1, Ing2, Meas2, Ing3, Meas3, Ing4, Meas4, Ing5, Meas5) => {
    const modal = document.getElementById('foodDetailsModel');
    modal.classList.remove('hidden');
    
    modal.innerHTML = `
    <div class="fixed inset-0 bg-gray-800 bg-opacity-50 flex justify-center items-center z-50">
        <div class="bg-white p-12 rounded-lg shadow-lg w-[90%] max-w-lg relative">
            <button class="absolute top-0 right-1 text-gray-600 hover:text-gray-800 text-4xl font-bold p-4"
                aria-label="Close Modal" onclick="closeModal()">
                &times;
            </button>
            <div class="space-y-6">
                <img src="${img}" alt="food item" class="w-full h-48 object-cover rounded-md shadow-sm" />
                <div class="flex justify-between items-center">
                    <h2 class="text-2xl font-semibold text-gray-800">${name}</h2>
                    <p class="text-xl font-bold text-yellow-600">$9.99</p>
                </div>
                <div class="text-gray-700 space-y-2">
                    <p class="text-lg"><strong>Category:</strong> ${cat}</p>
                    <p class="text-lg"><strong>Country:</strong> ${area}</p>
                </div>
                <div>
                    <h3 class="text-xl font-semibold text-gray-800 mb-2">Ingredients:</h3>
                    <ul class="list-disc pl-6 space-y-1 text-gray-600">
                        <li><strong>${Ing1}</strong>: ${Meas1}</li>
                        <li><strong>${Ing2}</strong>: ${Meas2}</li>
                        <li><strong>${Ing3}</strong>: ${Meas3}</li>
                        <li><strong>${Ing4}</strong>: ${Meas4}</li>
                        <li><strong>${Ing5}</strong>: ${Meas5}</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    `;
};

const closeModal = () => {
    const modal = document.getElementById('foodDetailsModel');
    modal.classList.add('hidden');
};

const addToCart = (foodId, name, img, btn) => {
    if (cart.length >= 11) {
        alert("You cannot add more than 11 items to the cart.");
        return;
    }

    const itemAlreadyInCart = cart.some(item => item.id === foodId);
    if (itemAlreadyInCart) {
        alert("This item is already in your cart.");
        return;
    }

    cart.push({ id: foodId, name, img });
    updateCart();
    
    btn.innerHTML = "Added ✅";
    btn.classList.remove("bg-black", "hover:bg-blue-500");
    btn.classList.add("bg-yellow-500");
};

const updateCart = () => {
    const cartCount = document.getElementById('count');
    const cartList = document.getElementById('foodList');
    cartCount.innerText = cart.length;
    
    cartList.innerHTML = '';
    cart.forEach(item => {
        const div = document.createElement('div');
        div.classList.add('food-item');
        div.innerHTML = `
            <div class="food-card flex gap-4 text-left border border-gray-300 my-3 p-2 rounded-lg w-56">
                <img src="${item.img}" alt="${item.name}" class="w-16 h-16 rounded-full object-cover">
                <div>
                    <p class="font-semibold text-gray-800">${item.name}</p>
                    <button class="text-red-600 font-bold" onclick="removeFromCart('${item.id}')">Remove</button>
                </div>
            </div>
        `;
        cartList.appendChild(div);
    });
};

const removeFromCart = (foodId) => {
    cart = cart.filter(item => item.id !== foodId);
    updateCart();
};

const searchFoods = () => {
    const searchInput = document.getElementById('searchField').value.toLowerCase();
    const filteredFoods = dataP.filter(food => food.strMeal.toLowerCase().includes(searchInput));
    
    renderAllFoods(filteredFoods);
};

document.getElementById('home').addEventListener('click', () => {
    document.getElementById('searchField').value = '';
    renderAllFoods(dataP);
});

// Order function
const placeOrder = () => {
    if (cart.length === 0) {
        alert("Your cart is empty! Add items before ordering.");
        return;
    }

    // Place the order (could be an API call in a real-world scenario)
    alert("Your order has been placed successfully!");
    
    // Clear the cart
    cart = [];
    
    // Update the cart UI
    updateCart();
    
    // Close the sidebar after placing the order
    document.getElementById('foodSideBarList').classList.add('hidden');
};
