"""
ComfyUI-FirstframeLastframeExtractor
====================================
Registers the First & Last Frame Extractor node with ComfyUI.
"""

from .nodes import FirstFrameLastFrameExtractor

NODE_CLASS_MAPPINGS = {
    "FirstFrameLastFrameExtractor": FirstFrameLastFrameExtractor,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FirstFrameLastFrameExtractor": "First & Last Frame Extractor 🎬",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
