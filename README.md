# foodDetectAndCalculateCalorie
foodDetectAndCalculateCalorie
使用步驟
1.至(https://drive.google.com/drive/u/0/folders/1osv22VzJUNak5KalmIbPsQl8_p02Kgx5)下載額外所需資料集和yolov9檔案
2.創一個資料夾分別放入1.github中程式2.yolov9檔案
3.將dataset資料夾放入yolov9的data資料夾中
4.在終端機中輸入以下(括號內圍說明不用輸入，且建議直接從remindme.md複製下面僅供參考)

(在終端機中先進入yolov9資料夾)
cd C:\Users\brian\Desktop\food_detect3\yolov9
(訓練用參數)
python train_dual.py --batch 4 --epochs 100 --img 416 --device 0 --min-items 0 --close-mosaic 15 --data data/food_datasets/data.yaml --weights weight/yolov9-c.pt --cfg models/detect/yolov9-c.yaml --hyp hyp.scratch-high.yaml

''' --epochs 20 #輪數 --img 416 #改變訓練圖片數 '''
(輸出用參數)
python detect_dual.py --weights runs\train\exp18\weights\best.pt --conf 0.30 --source data\food_datasets\train\images\WhatsApp-Image-2024-05-29-at-14-45-49_jpeg.rf.21283b1e2681989eb5c9e9b0c937e4b8.jpg --device 0
5.成功
