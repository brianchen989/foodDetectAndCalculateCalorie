# YOLOv9 檔案結構全解析 (完整版)

這份文件詳細說明了 YOLOv9 專案中 **所有** 檔案與資料夾的詳細用途。

## 🌟 根目錄 (Root Directory)

專案的核心入口點。

| 檔案名稱 | 用途說明 |
| :--- | :--- |
| **`train_dual.py`** | **(推薦)** YOLOv9 標準訓練程式。使用 Dual 分支架構 (主分支 + 輔助分支) 進行訓練，效果最佳。 |
| `train.py` | 傳統單一分支訓練程式。 |
| `train_triple.py` | 三分支訓練程式 (實驗性)。 |
| **`detect.py`** | 通用推論程式。載入權重檔 (`.pt`) 進行物件偵測。 |
| `detect_dual.py` | 針對 Dual 架構優化的推論程式。 |
| `val.py` | 驗證程式。計算 mAP 指標。 |
| `val_dual.py` | 針對 Dual 架構的驗證程式。 |
| `val_triple.py` | 針對 Triple 架構的驗證程式。 |
| `export.py` | 模型匯出工具 (ONNX, TensorRT 等)。 |
| `hubconf.py` | PyTorch Hub 設定檔。 |
| `benchmarks.py` | 效能基準測試工具。 |
| `requirements.txt` | 專案依賴套件清單。 |
| `LICENSE.md` | 授權條款 (GPL-3.0)。 |
| `README.md` | 官方說明文件。 |

---

## 🧠 模型架構 (`models/`)

| 檔案名稱 | 用途說明 |
| :--- | :--- |
| `yolo.py` | **核心**。定義 YOLO 模型類別，解析 `.yaml` 並建立網路層。 |
| `common.py` | **核心**。定義各種網路層 (Conv, SPP, RepNCSPELAN4 等)。 |
| `experimental.py` | 實驗性網路層 (MixConv2d 等)。 |
| `tf.py` | TensorFlow 轉換支援。 |
| `detect/` | 存放 YOLOv9 模型設定檔 (`yolov9-c.yaml`, `yolov9-e.yaml` 等)。 |
| `hub/` | PyTorch Hub 相關設定檔。 |
| `panoptic/` | 全景分割模型相關定義。 |
| `segment/` | 實例分割模型相關定義。 |

---

## 🛠️ 工具函式 (`utils/`)

| 檔案名稱 | 用途說明 |
| :--- | :--- |
| `dataloaders.py` | 資料載入、預處理與增強 (Mosaic, Mixup)。 |
| `loss.py` | 傳統損失函數計算。 |
| `loss_tal.py` | Task Aligned Loss (TAL) 損失函數。 |
| `loss_tal_dual.py` | Dual 分支專用 TAL 損失函數。 |
| `loss_tal_triple.py` | Triple 分支專用 TAL 損失函數。 |
| `general.py` | 通用工具 (NMS, 座標轉換, 亂數種子)。 |
| `metrics.py` | 效能指標計算 (mAP, Precision, Recall)。 |
| `plots.py` | 繪圖工具 (訓練曲線, 標註預覽)。 |
| `augmentations.py` | 進階資料增強 (Albumentations, Copy-Paste)。 |
| `autoanchor.py` | 自動錨點計算。 |
| `torch_utils.py` | PyTorch 輔助工具 (DDP, Device 選擇)。 |
| `callbacks.py` | 訓練過程的回呼函式。 |
| `activations.py` | 激活函數定義 (SiLU, Hardswish 等)。 |
| `autobatch.py` | 自動 Batch Size 計算。 |
| `coco_utils.py` | COCO 資料集相關工具。 |
| `downloads.py` | 檔案下載工具 (下載權重、字型等)。 |
| `lion.py` | Lion 優化器實作。 |
| `triton.py` | Triton Inference Server 相關工具。 |
| `loggers/` | 實驗記錄器 (TensorBoard, WandB, ClearML)。 |

---

## 📂 資料設定 (`data/`)

| 檔案名稱 | 用途說明 |
| :--- | :--- |
| `hyps/` | 超參數設定檔目錄 (如 `hyp.scratch-high.yaml`)。 |
| `scripts/` | 輔助腳本 (如下載 COCO 資料集)。 |
| `coco.yaml` | COCO 資料集設定範本。 |
| `data.yaml` | (使用者自定義) 您的資料集設定檔。 |

---

## 🎯 特定任務目錄

這些目錄包含針對特定任務的獨立訓練/推論腳本。

### `classify/` (影像分類)
| 檔案名稱 | 用途說明 |
| :--- | :--- |
| `train.py` | 分類模型訓練程式。 |
| `val.py` | 分類模型驗證程式。 |
| `predict.py` | 分類模型推論程式。 |

### `segment/` (實例分割)
| 檔案名稱 | 用途說明 |
| :--- | :--- |
| `train.py` | 分割模型訓練程式。 |
| `train_dual.py` | Dual 架構分割模型訓練程式。 |
| `val.py` | 分割模型驗證程式。 |
| `val_dual.py` | Dual 架構分割模型驗證程式。 |
| `predict.py` | 分割模型推論程式。 |

### `panoptic/` (全景分割)
| 檔案名稱 | 用途說明 |
| :--- | :--- |
| `train.py` | 全景分割訓練程式。 |
| `val.py` | 全景分割驗證程式。 |
| `predict.py` | 全景分割推論程式。 |

---

## 🔧 其他

| 檔案名稱 | 用途說明 |
| :--- | :--- |
| `tools/` | 包含 `reparameterization.ipynb` (重參數化轉換工具)。 |
| `figure/` | 存放 README 使用的展示圖片 (如 `performance.png`)。 |
| `runs/` | **執行結果輸出目錄** (訓練權重、推論圖片)。 |
| `weight/` | **權重檔目錄** (存放 `yolov9-c.pt` 等)。 |
