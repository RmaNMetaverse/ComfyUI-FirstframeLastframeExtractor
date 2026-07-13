# ComfyUI-FirstframeLastframeExtractor 🎬

> Extract the **first frame** and **last frame** from any video — directly in your ComfyUI workflow.

A lightweight, zero-config utility node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that takes any video input and returns the first and last frames as standard `IMAGE` outputs. Works with direct file paths **and** image batches from other nodes like [VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite).

---

## ✨ Features

- 🎯 **Dual Input Mode** — Accepts a video file path (`STRING`) or a pre-loaded image batch (`IMAGE`) from other nodes
- 🔄 **Auto Detection** — Connect whichever input you have; the node handles the rest
- 🎥 **Broad Codec Support** — `.mp4`, `.avi`, `.mkv`, `.mov`, `.webm`, `.gif` and more via OpenCV
- 🛡️ **Robust Fallback** — If the codec doesn't support direct seeking, falls back to sequential reading
- ⚡ **Lightweight** — No heavy dependencies beyond what ComfyUI already ships with
- 🔗 **Universal Compatibility** — Works with all ComfyUI versions using the stable node API

---

## 📦 Installation

### Option A — Git Clone (Recommended)

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/RmaNMetaverse/ComfyUI-FirstframeLastframeExtractor.git
pip install -r ComfyUI-FirstframeLastframeExtractor/requirements.txt
```

Restart ComfyUI.

### Option B — ComfyUI Manager

Search for **"First & Last Frame Extractor"** in the ComfyUI Manager and click **Install**.

### Option C — Manual Download

1. Download and extract the [latest release](https://github.com/RmaNMetaverse/ComfyUI-FirstframeLastframeExtractor/releases)
2. Place the folder inside `ComfyUI/custom_nodes/`
3. Install dependencies: `pip install -r requirements.txt`
4. Restart ComfyUI

---

## 🚀 Quick Start

1. **Right-click** the ComfyUI canvas
2. Navigate to **Add Node → Video/Utils → First & Last Frame Extractor 🎬**
3. Connect an input (see below)
4. Wire the outputs to **Preview Image**, **Save Image**, or any downstream node
5. **Queue** the prompt

---

## 🔧 Node Reference

### Inputs

| Name | Type | Required | Description |
|:-----|:-----|:--------:|:------------|
| `video_path` | `STRING` | Optional | Absolute path to a video file (`.mp4`, `.avi`, `.mkv`, `.mov`, `.webm`, `.gif`) |
| `images` | `IMAGE` | Optional | Image batch tensor from another node (e.g., VHS Load Video) |

> [!NOTE]
> At least one input must be provided. If both are connected, the **image batch** takes priority.

### Outputs

| Name | Type | Description |
|:-----|:-----|:------------|
| `first_frame` | `IMAGE` | The very first frame of the video `[1, H, W, C]` |
| `last_frame` | `IMAGE` | The very last frame of the video `[1, H, W, C]` |

### Category

📁 `Video/Utils` → **First & Last Frame Extractor 🎬**

---

## 💡 Usage Examples

### Example 1: Direct File Path

Paste or type a video file path directly into the node — no other nodes needed.

```
┌─────────────────────────────────┐       ┌────────────────┐
│ First & Last Frame Extractor 🎬 │       │                │
│                                 │       │  Preview Image │
│  video_path: C:\video.mp4      ├──────►│                │
│                                 │       └────────────────┘
│                 first_frame  ○──┤
│                  last_frame  ○──┼──────►┌────────────────┐
│                                 │       │   Save Image   │
└─────────────────────────────────┘       └────────────────┘
```

### Example 2: From VideoHelperSuite (VHS)

Connect the IMAGE output of a VHS **Load Video** node to extract the boundary frames from a loaded sequence.

```
┌──────────────────┐       ┌─────────────────────────────────┐       ┌────────────────┐
│  VHS Load Video  │       │ First & Last Frame Extractor 🎬 │       │                │
│                  │       │                                 │       │  Preview Image │
│        IMAGE  ○──┼──────►│  images                        ├──────►│                │
│                  │       │                 first_frame  ○──┤       └────────────────┘
└──────────────────┘       │                  last_frame  ○──┤
                           │                                 │
                           └─────────────────────────────────┘
```

### Example 3: Frame-to-Frame Comparison

Use both outputs for side-by-side comparison, img2img pipelines, or interpolation workflows.

---

## 🔗 Compatibility

| Component | Supported |
|:----------|:----------|
| **ComfyUI** | All versions (stable `NODE_CLASS_MAPPINGS` API) |
| **Python** | 3.8+ |
| **OS** | Windows, Linux, macOS |
| **Interop** | VideoHelperSuite (VHS), or any node that outputs `IMAGE` batches |

---

## 🛠️ Dependencies

| Package | Notes |
|:--------|:------|
| `opencv-python-headless` ≥ 4.5.0 | For reading video files from disk |
| `torch` | Already included in ComfyUI |
| `numpy` | Already included in ComfyUI |

---

## 🧪 Running Tests

A smoke test suite is included for local verification:

```bash
cd ComfyUI-FirstframeLastframeExtractor
python test_node.py
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an [issue](https://github.com/RmaNMetaverse/ComfyUI-FirstframeLastframeExtractor/issues) or submit a pull request.

---

<p align="center">
  Made with ❤️ for the ComfyUI community
</p>
