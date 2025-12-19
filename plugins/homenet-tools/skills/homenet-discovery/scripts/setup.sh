#!/usr/bin/env bash
# homenet setup - creates directories and checks prerequisites
# Output is model-friendly (structured, non-interactive)

SKILL_NAME="homenet"

# Create XDG directories
mkdir -p "$HOME/.config/$SKILL_NAME"
mkdir -p "$HOME/.local/share/$SKILL_NAME/cache"
mkdir -p "/tmp/$SKILL_NAME"

# Check prerequisites
MISSING=()

if ! command -v nmap &> /dev/null; then
    MISSING+=("nmap")
fi

if ! command -v python3 &> /dev/null; then
    MISSING+=("python3")
fi

if ! command -v dig &> /dev/null && ! command -v host &> /dev/null; then
    MISSING+=("dig")
fi

if ! command -v ssh &> /dev/null; then
    MISSING+=("ssh")
fi

# Output results
echo "SETUP_STATUS: OK"
echo "CONFIG_DIR: $HOME/.config/$SKILL_NAME"
echo "DATA_DIR: $HOME/.local/share/$SKILL_NAME"
echo "TEMP_DIR: /tmp/$SKILL_NAME"

if [ ${#MISSING[@]} -eq 0 ]; then
    echo "PREREQUISITES: ALL_INSTALLED"
else
    echo "PREREQUISITES: MISSING"
    for tool in "${MISSING[@]}"; do
        echo "  MISSING_TOOL: $tool"
    done

    # Platform-specific install hints
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "INSTALL_PLATFORM: macOS"
        for tool in "${MISSING[@]}"; do
            case $tool in
                nmap) echo "  INSTALL_HINT: brew install nmap" ;;
                python3) echo "  INSTALL_HINT: brew install python3" ;;
                dig) echo "  INSTALL_HINT: brew install bind" ;;
            esac
        done
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "INSTALL_PLATFORM: Linux"
        for tool in "${MISSING[@]}"; do
            case $tool in
                nmap) echo "  INSTALL_HINT: sudo apt install nmap" ;;
                python3) echo "  INSTALL_HINT: sudo apt install python3" ;;
                dig) echo "  INSTALL_HINT: sudo apt install dnsutils" ;;
                ssh) echo "  INSTALL_HINT: sudo apt install openssh-client" ;;
            esac
        done
    fi
fi
