from ultralytics import YOLO

def main():
    model = YOLO("yolo11s.pt")

    model.train(
        data="data.yaml",
        epochs=100,
        imgsz=640,
        batch=-1,        # 自动调整 batch size
        workers=8,       # 多线程读取
        project="fire_smoke_project",
        name="yolo11s_5000",
        close_mosaic=10,
        device=0         # 使用 GPU
    )

if __name__ == "__main__":
    main()