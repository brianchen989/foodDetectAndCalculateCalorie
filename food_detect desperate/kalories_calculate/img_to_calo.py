import calculate
import weight_calcu

def process_detection(xyxy, food_name):
    """
    處理單一偵測結果的主函式。
    
    參數:
    xyxy: Bounding Box 的座標 [x1, y1, x2, y2]
    food_name: 偵測到的食物類別名稱
    
    回傳:
    字串，包含估算重量和熱量，用於顯示在標籤上。
    """
    # 1. 計算像素面積
    area = weight_calcu.get_pixel_area(xyxy)
    
    # 2. 估算重量 (使用預設係數 0.005，即 200 像素約 1 克，可依需求調整)
    weight = weight_calcu.pixels_to_weight_simple(area, factor=0.002)
    
    # 3. 計算熱量 (呼叫 calculate 模組)
    calories = calculate.calculate_kalories(food_name, weight)
    
    # 4. 回傳結果字串，讓 detect.py 可以印在圖片上
    if calories is not None:
        return f"{weight:.0f}g, {calories:.0f}kcal"
    else:
        # 如果算不出熱量（例如資料庫沒有該食物），顯示問號
        return f"{weight:.0f}g, ? kcal"
