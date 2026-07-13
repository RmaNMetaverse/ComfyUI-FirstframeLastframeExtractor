# ComfyUI-FirstframeLastframeExtractor 🎬

> Extract the **first frame** and **last frame** from any video — directly in your ComfyUI workflow.

A lightweight, zero-config utility node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that takes any video input and returns the first and last frames as standard `IMAGE` outputs. Works with direct file paths **and** image batches from other nodes like [VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite).*

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

### Option A — ComfyUI Manager (Easiest)

If you have [ComfyUI Manager](https://github.com/Comfy-Org/ComfyUI-Manager) installed (it comes pre-installed with Comfy Desktop):

1. Open ComfyUI and click the **Manager** button
2. Click **"Install Custom Nodes"**
3. Search for **"FirstFrameLastFrame"** or **"First Frame Last Frame"**
4. Click **Install** → Restart ComfyUI

> ComfyUI Manager handles cloning and dependency installation automatically.

---

### Option B — ComfyUI Portable (Windows Standalone)

This is the most common Windows setup — the one you download as a `.7z` or `.zip` from the [ComfyUI releases page](https://github.com/comfyanonymous/ComfyUI/releases).

**Step 1: Clone the node**

Open a Command Prompt or PowerShell window and navigate to your portable folder:

```bash
cd ComfyUI_windows_portable\ComfyUI\custom_nodes
git clone https://github.com/RmaNMetaverse/ComfyUI-FirstframeLastframeExtractor.git
```

**Step 2: Install requirements**

> [!IMPORTANT]
> You **must** use the embedded Python that ships with the portable version, **not** your system Python. Otherwise the packages will be installed in the wrong place and ComfyUI won't see them.

Navigate back to the portable root folder and run:

```bash
cd ComfyUI_windows_portable
.\python_embeded\python.exe -m pip install -r .\ComfyUI\custom_nodes\ComfyUI-FirstframeLastframeExtractor\requirements.txt
```

**Step 3:** Restart ComfyUI.

---

### Option C — Comfy Desktop (Electron App)

Comfy Desktop runs its own isolated Python environment. It also comes with **ComfyUI Manager pre-installed**, so **Option A above is the recommended method**.

If you need to install manually:

**Step 1: Clone the node**

Find your Comfy Desktop's `custom_nodes` folder. The typical location is:

| OS | Path |
|:---|:-----|
| Windows | `C:\Users\<YOU>\AppData\Roaming\ComfyUI\custom_nodes\` |
| macOS | `~/Library/Application Support/ComfyUI/custom_nodes/` |
| Linux | `~/.config/ComfyUI/custom_nodes/` |

```bash
cd <path_to_custom_nodes>
git clone https://github.com/RmaNMetaverse/ComfyUI-FirstframeLastframeExtractor.git
```

**Step 2: Install requirements**

Locate the `python_embeded` (or `python`) folder inside your Comfy Desktop installation directory, then run:

```bash
"<path_to_comfy_desktop_python>\python.exe" -m pip install -r "<path_to_custom_nodes>\ComfyUI-FirstframeLastframeExtractor\requirements.txt"
```

> [!TIP]
> The easiest way to find the right Python path: open Comfy Desktop → Manager → click **"Open Terminal"** — this opens a terminal pre-configured with the correct Python. Then just run:
> ```bash
> pip install -r custom_nodes/ComfyUI-FirstframeLastframeExtractor/requirements.txt
> ```

**Step 3:** Restart Comfy Desktop.

---

### Option D — Manual Install (pip / venv / conda)

For users who installed ComfyUI manually via `git clone` into a **virtual environment** or **conda environment**:

**Step 1: Clone the node**

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/RmaNMetaverse/ComfyUI-FirstframeLastframeExtractor.git
```

**Step 2: Install requirements**

Make sure your virtual environment is **activated first**, then:

```bash
pip install -r ComfyUI/custom_nodes/ComfyUI-FirstframeLastframeExtractor/requirements.txt
```

**Step 3:** Restart ComfyUI.

---

### Option E — Manual Download (No Git)

1. Go to the [GitHub repo](https://github.com/RmaNMetaverse/ComfyUI-FirstframeLastframeExtractor)
2. Click **Code → Download ZIP**
3. Extract the folder into your `ComfyUI/custom_nodes/` directory
4. Make sure the folder structure is correct — `__init__.py` should be directly inside `custom_nodes/ComfyUI-FirstframeLastframeExtractor/` (no double nesting)
5. Install requirements using the method for your ComfyUI version (see above)
6. Restart ComfyUI

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

| Name         | Type     | Required | Description                                                                     |
|:------------ |:-------- |:--------:|:------------------------------------------------------------------------------- |
| `video_path` | `STRING` | Optional | Absolute path to a video file (`.mp4`, `.avi`, `.mkv`, `.mov`, `.webm`, `.gif`) |
| `images`     | `IMAGE`  | Optional | Image batch tensor from another node (e.g., VHS Load Video)                     |

> [!NOTE]
> At least one input must be provided. If both are connected, the **image batch** takes priority.

### Outputs

| Name          | Type    | Description                                      |
|:------------- |:------- |:------------------------------------------------ |
| `first_frame` | `IMAGE` | The very first frame of the video `[1, H, W, C]` |
| `last_frame`  | `IMAGE` | The very last frame of the video `[1, H, W, C]`  |

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

| Component   | Supported                                                        |
|:----------- |:---------------------------------------------------------------- |
| **ComfyUI** | All versions (stable `NODE_CLASS_MAPPINGS` API)                  |
| **Python**  | 3.8+                                                             |
| **OS**      | Windows, Linux, macOS                                            |
| **Interop** | VideoHelperSuite (VHS), or any node that outputs `IMAGE` batches |

---

## 🛠️ Dependencies

| Package                          | Notes                             |
|:-------------------------------- |:--------------------------------- |
| `opencv-python-headless` ≥ 4.5.0 | For reading video files from disk |
| `torch`                          | Already included in ComfyUI       |
| `numpy`                          | Already included in ComfyUI       |

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

## 👤 Author

**RmaN** (Arman Jangmiri)

- GitHub: [@RmaNMetaverse](https://github.com/RmaNMetaverse)

---

<p align="center">
  Made with ❤️ by RmaN for the ComfyUI community
</p>
