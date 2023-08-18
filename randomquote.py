import random

#Dictionary of categories and their corresponding quotes
quotes ={
    'motivation':[
        "Success is not final,failure is not fatal: It is the courage to continue that counts.- {name}",
        "Believe you can and you're halfway there. - {name}",
        "The future belongs to those who believe in the beauty of their dreams. -{name}",
    ],
    'success':[
    "The only way to do great work is to love what you do. -{name}",
    "Success is not in what you have,but who you are. -{name}",
    "Success is walking from failure to failure with no loss of enthusiasm. -{name}",
    ],
    'life':[
        "In the end,its not the years in your life that count.its the life in your years. -{name}",
        "life is 10% what happens to us and 90% How we react to it. -{name}",
        "Life is really simple,but we insist on making it complicated. -{name}",
    ],
    'love':[
        "The best thing to hold onto in life is each other. -{name}",
        "Love is not about possession.Its about appreciation. -{name}",
        "To love and be loved is ti feel the sun from both sides. -{name}",
    ]

}

def get_user_input(prompt):
    return input(prompt).strip()

def get_random_quote(category,name):
    category_quotes = quotes.get(category)
    if category_quotes:
        quote_template = random.choice(category_quotes)
        personalized_quote = quote_template.format(name=name)
        return personalized_quote
    else:
        return "Invalid category. please choose a valid category."
    
def main():
    name = get_user_input("Enter your name:")
    print("Choose a category:")
    for category in quotes.keys():
        print(category)

    category = get_user_input("Enter a category:")
    category = category.lower()

    quote = get_random_quote(category,name)
    print("\n"+quote)

    if __name__ == "__main__":
        main()
