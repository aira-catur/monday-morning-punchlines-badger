import os

TEXT = "Monday morning: my bed won custody in the divorce, my alarm is the bailiff, and coffee is my court-appointed lawyer, late and billing by the sip."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
