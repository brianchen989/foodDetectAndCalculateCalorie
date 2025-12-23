# 計算 Bounding Box 的像素面積
def get_pixel_area(xyxy):
    """
    計算給定邊界框的總像素面積。
    
    參數:
    xyxy: 一個包含 [x1, y1, x2, y2] 座標的列表或陣列
          x1, y1: 左上角座標
          x2, y2: 右下角座標
    
    回傳:
    pixel_count: 像素總數 (面積)
    """
    x1, y1, x2, y2 = xyxy
    
    # 寬度 = 右邊界(x2) - 左邊界(x1)
    width = x2 - x1
    
    # 高度 = 下邊界(y2) - 上邊界(y1)
    height = y2 - y1
    
    # 面積 = 寬 * 高
    pixel_count = width * height
    
    return pixel_count


# 簡單重量估算：重量 = 像素面積 * 係數
def pixels_to_weight_simple(pixel_count, factor=0.002):
    """
    將像素面積轉換為估計重量。
    
    參數:
    pixel_count: 像素面積
    factor: 轉換係數，代表每一像素對應多少公克。
            預設值 0.005 代表每 200 像素 = 1g。
            (這個數值受拍攝距離和相機解析度影響很大，建議根據實際情況調整)
            
    回傳:
    weight_grams: 估算的重量 (公克)
    """
    weight_grams = pixel_count * factor
    return weight_grams