import sys
import pyperclip

def collect_stdin():
    lines = []
    try:
        for line in sys.stdin:
            sys.stdout.write(line)
            sys.stdout.flush()
            lines.append(line)
        return "".join(lines)  
    except KeyboardInterrupt:
        return "".join(lines)  
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    text = collect_stdin()
    pyperclip.copy(text)

if __name__ == "__main__":
    main()
