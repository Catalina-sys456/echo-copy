# ec

A simple Python script that reads from stdin and copies the input to the system clipboard.

## Features
- Reads input from stdin (piped input or manual typing)
- Preserves input in real-time while copying
- Handles keyboard interrupts gracefully
- Works with both X11 and Wayland systems

## Requirements
- Python 3.x
- `pyperclip` Python package
- System clipboard utilities:
  - **X11 (Xorg)**: `xclip` or `xsel` (usually pre-installed)
  - **Wayland**: `wl-clipboard` (must be installed manually)

## Installation

### 1. Install Python Dependencies
```bash
pip install pyperclip ec
```

### 2. Install System Clipboard Utilities

#### For X11 (Xorg) Users
Most Linux distributions come with `xclip` or `xsel` pre-installed. If not:
```bash
# Debian/Ubuntu
sudo apt install xclip

# Arch Linux
sudo pacman -S xclip

# Fedora
sudo dnf install xclip
```

#### For Wayland Users
Install `wl-clipboard` (required for Wayland compatibility):
```bash
# Debian/Ubuntu
sudo apt install wl-clipboard

# Arch Linux
sudo pacman -S wl-clipboard

# Fedora
sudo dnf install wl-clipboard
```

## Usage

### Basic Usage
Pipe any command's output to the clipboard:
```bash
echo "Hello, clipboard!" | ec
# or
cat file.txt | ec
# or 
ping google.com | ec
```


## Notes
- On Wayland, ensure `wl-copy` (from `wl-clipboard`) is in your `PATH`
- If you encounter clipboard issues, try running with `sudo` (not recommended for security)
- The script preserves all whitespace and formatting from the input


### Key Points Covered:
1. **Dependencies**: Clearly lists both Python and system requirements
2. **Wayland Support**: Explicitly mentions `wl-clipboard` installation
3. **Usage Examples**: Shows both piped and interactive usage
4. **Troubleshooting**: Includes common issues and solutions
5. **Security Note**: Warns about `sudo` usage

You may want to adjust the installation commands based on the specific Linux distributions your users might have.
