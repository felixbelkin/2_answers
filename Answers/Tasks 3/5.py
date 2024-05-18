import xml.etree.ElementTree as ET

def parse_xml(file_name):
    """Функция для парсинга XML-файла и извлечения информации о товарах."""
    tree = ET.parse(file_name)
    root = tree.getroot()

    products = []
    
    for product in root.findall('product'):
        name = product.find('name').text
        category = product.find('category').text
        price = float(product.find('price').text)
        
        products.append({
            'name': name,
            'category': category,
            'price': price
        })
    
    return products

def sort_by_price(products):
    """Функция для сортировки товаров по цене."""
    return sorted(products, key=lambda x: x['price'])

def filter_by_category(products, category):
    """Функция для фильтрации товаров по категории."""
    return [product for product in products if product['category'] == category]

def calculate_total_cost(products):
    """Функция для расчета общей стоимости заказа."""
    return sum(product['price'] for product in products)

def display_products(products):
    """Функция для отображения списка товаров."""
    print(f"{'Название':<15}{'Категория':<20}{'Цена':<10}")
    print("-" * 45)
    for product in products:
        print(f"{product['name']:<15}{product['category']:<20}{product['price']:<10}")

# Пример использования функций
if __name__ == "__main__":
    products = parse_xml("products.xml")

    print("Все товары:")
    display_products(products)

    sorted_products = sort_by_price(products)
    print("\nТовары, отсортированные по цене:")
    display_products(sorted_products)

    electronics = filter_by_category(products, "Электроника")
    print("\nТовары в категории 'Электроника':")
    display_products(electronics)

    total_cost = calculate_total_cost(products)
    print(f"\nОбщая стоимость всех товаров: {total_cost} руб.")
