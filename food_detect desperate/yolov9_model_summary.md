# YOLOv9 模型架構與訓練設置

此文件整理了本專案中使用的 YOLOv9 模型架構、訓練參數以及相關設置。

## 1. 模型架構

*   **基礎模型**: YOLOv9
*   **模型變體**: `yolov9-c` (Compact 版本)
*   **主要特徵**:
    *   **PGI (Programmable Gradient Information)**: 可程式化梯度資訊，用於解決深層網路中的資訊瓶頸問題，確保梯度能有效傳遞並更新參數。
    *   **GELAN (Generalized Efficient Layer Aggregation Network)**: 廣義高效層聚合網路，結合了 CSPNet 和 ELAN 的優點，提供輕量級且高效的特徵提取能力。
*   **設定檔**: `models/detect/yolov9-c.yaml`
    *   定義了 Backbone (骨幹網路) 與 Head (偵測頭) 的結構。
    *   包含輸入通道數 (ch)、類別數 (nc) 以及錨點 (anchors) 設定。

## 2. 訓練設置 (Training Configuration)

以下參數基於 `remind.md` 中的訓練指令整理：

*   **訓練腳本**: `train_dual.py` (支援雙流/輔助訓練邏輯)
*   **預訓練權重 (Pre-trained Weights)**: `weight/yolov9-c.pt` (載入預先訓練好的權重以加速收斂)
*   **資料集設定 (Data Configuration)**: `data/food_datasets/data.yaml`
    *   包含訓練集、驗證集路徑。
    *   定義食物類別名稱與數量。

### 超參數 (Hyperparameters)

*   **Epochs (訓練輪數)**: `100` (訓練總共進行 100 個世代)
*   **Batch Size (批次大小)**: `4` (依據顯示卡記憶體調整，較小的值可減少記憶體佔用但可能影響 Batch Normalization)
*   **Image Size (圖片尺寸)**: `416` (輸入圖片被調整為 416x416 像素進行訓練)
*   **Device (裝置)**: `0` (使用第一張 GPU 進行訓練)
*   **超參數設定檔**: `hyp.scratch-high.yaml`
    *   定義了學習率 (lr), 動量 (momentum), 權重衰減 (weight decay) 等詳細參數，針對從頭訓練或微調進行了優化。

### 其他訓練參數

*   **--min-items 0**: 即使圖片中沒有標註物件也可能被包含（視具體實作而定，通常用於過濾空圖片）。
*   **--close-mosaic 15**: 在訓練的最後 15 個 epoch 關閉 Mosaic 資料增強。
    *   Mosaic 增強會將 4 張圖片拼貼在一起，有助於檢測小物體。
    *   在最後階段關閉它可以讓模型適應正常的圖片分佈，提升最終精度。

## 3. 推論/偵測設置 (Inference/Detection Settings)

以下參數基於 `remind.md` 中的偵測指令整理：

*   **偵測腳本**: `detect_dual.py`
    *   **客製化功能**: 已整合 `img_to_calo` 模組，在偵測時會同步計算並顯示食物的估計重量與熱量。
*   **權重來源**: `runs\train\exp18\weights\best.pt` (使用訓練實驗 exp18 中表現最好的權重)
*   **信心閾值 (Confidence Threshold)**: `0.30` (只顯示信心分數大於 30% 的偵測結果)
*   **輸入來源**: 圖片檔案 (例如 `.../train/images/....jpg`)

## 4. 功能擴充：熱量計算系統

本專案在 YOLOv9 的基礎上擴充了熱量計算功能：

1.  **物件偵測**: YOLOv9 識別食物類別 (如 Apple) 與位置 (Bounding Box)。
2.  **像素面積計算**: `weight_calcu.py` 計算 Bounding Box 的面積。
3.  **重量估算**: `weight_calcu.py` 使用係數 (目前設為 `0.002`) 將像素面積轉換為公克數。
4.  **熱量查詢**: `calculate.py` 根據食物名稱查詢資料庫 (`database.py`)，並依據重量計算總熱量。
5.  **結果顯示**: `detect_dual.py` 將 "類別 + 信心度 + 重量 + 熱量" 標註在輸出圖片上。
