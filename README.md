# RunPod Chat Interface

A beautiful web-based chat interface for communicating with RunPod's hosted language models, plus a Python CLI client.

🌐 **[Try it live on GitHub Pages →](https://willjones1.github.io/runpod-chat-client/)**

## Description

This project provides two ways to interact with RunPod instances running the `neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8` model:

1. **Web Interface** - A modern, responsive chat UI (`index.html`)
2. **Python CLI** - A command-line script for API testing (`runpod_chat.py`)

## Features

- 🎨 Beautiful, modern chat interface with real-time responses
- 🔧 Configurable parameters (temperature, max tokens)
- 💾 Automatic URL persistence in browser storage
- 📱 Responsive design for mobile and desktop
- 🛡️ Environment-based configuration for security
- ⚡ Direct API communication with error handling

## Prerequisites

- A RunPod account with an active pod running the specified model
- Your RunPod instance endpoint URL
- For Python script: Python 3.7 or higher

## Quick Start

### Web Interface (Recommended)

**Option 1: Use the hosted version**
- Visit: https://willjones1.github.io/runpod-chat-client/
- Enter your RunPod API URL
- Start chatting!

**Option 2: Run locally**
1. Download or clone this repository
2. Open `index.html` in your web browser
3. Enter your RunPod API URL in the configuration field
4. Start chatting!

### Python CLI

1. Clone this repository:
```bash
git clone https://github.com/willjones1/runpod-chat-client.git
cd runpod-chat-client
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your environment:
```bash
cp env.example .env
# Edit .env file with your configuration
```

4. Run the script:
```bash
python runpod_chat.py
```

## Configuration

### Web Interface
- Enter your RunPod API URL in the format: `https://your-endpoint-8000.proxy.runpod.net`
- Adjust temperature and max tokens as needed
- Settings are automatically saved in your browser

### Python Script
- Copy `env.example` to `.env`
- Add your configuration details to the `.env` file
- The script will load settings automatically

## Customization

The web interface allows real-time adjustment of:
- **Temperature**: Control response creativity (0.0-1.0)
- **Max Tokens**: Set response length limits
- **API Endpoint**: Switch between different RunPod instances

## Example Output

```
User: Explain quantum computing in simple terms
Assistant: Quantum computing uses quantum mechanical phenomena like superposition and entanglement to process information in ways that classical computers cannot, potentially solving certain problems exponentially faster.
```

## Error Handling

Both interfaces include comprehensive error handling for:
- Network connection issues
- API endpoint problems
- Invalid responses
- Configuration errors

## Browser Compatibility

The web interface works with all modern browsers:
- Chrome/Chromium 70+
- Firefox 65+
- Safari 12+
- Edge 79+

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE). 