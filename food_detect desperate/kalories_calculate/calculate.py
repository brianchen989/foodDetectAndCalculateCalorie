import database

def calculate_kalories(food_name, weight):
    """
    計算食物熱量的函式。
    
    參數:
    food_name: 食物名稱 (字串)
    weight: 重量，單位為公克 (數值)
    
    回傳:
    total_calories: 總熱量 (數值)，如果找不到食物則回傳 None
    """
    # 確保名稱為小寫以符合資料庫格式
    food_name = food_name.lower()
    
    # 檢查食物是否存在於資料庫中
    if food_name in database.food_database:
        # 從資料庫獲取每100克的熱量
        cal_100g = database.food_database[food_name]
        
        # 計算總熱量: (每100克熱量 / 100) * 重量
        total_calories = (cal_100g / 100) * weight
        return total_calories
    else:
        # 如果找不到食物，回傳 None
        return None