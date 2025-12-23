cd C:\Users\brian\Desktop\food_detect3\yolov9

python train_dual.py `
--batch 4 `
--epochs 100 `
--img 416 `
--device 0 `
--min-items 0 `
--close-mosaic 15 `
--data data/food_datasets/data.yaml `
--weights weight/yolov9-c.pt `
--cfg models/detect/yolov9-c.yaml `
--hyp hyp.scratch-high.yaml

'''
--epochs 20 `#輪數
--img 416 `#改變訓練圖片數
'''



python detect_dual.py `
--weights runs\train\exp18\weights\best.pt `
--conf 0.30 `
--source data\food_datasets\train\images\WhatsApp-Image-2024-05-29-at-14-45-49_jpeg.rf.21283b1e2681989eb5c9e9b0c937e4b8.jpg `
--device 0
