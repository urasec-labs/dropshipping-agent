import sys

class SimpleLogger:
    def info(self, msg): print(f"[INFO] {msg}", file=sys.stderr)
    def error(self, msg): print(f"[ERROR] {msg}", file=sys.stderr)
    def warning(self, msg): print(f"[WARN] {msg}", file=sys.stderr)

logger = SimpleLogger()
