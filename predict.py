# predict.py 示例代码
from ultralytics import YOLO
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Fire and Smoke Detection using YOLO11s")
    parser.add_argument("--source", type=str, default="0", help="输入源: 0代表摄像头, 或图片/视频路径")
    parser.add_argument("--conf", type=float, default=0.4, help="置信度阈值")
    args = parser.parse_args()

    # 动态获取当前脚本所在的目录，确保能找到权重
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, "weights", "best.pt")

    print(f"Loading model from: {model_path}")
    model = YOLO(model_path)

    # 运行推理
    print(f"Running inference on source: {args.source}")
    results = model.predict(source=args.source, show=True, conf=args.conf, save=True)

if __name__ == "__main__":
    main()