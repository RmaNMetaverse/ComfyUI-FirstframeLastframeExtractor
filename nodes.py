"""
ComfyUI-FirstframeLastframeExtractor
====================================
A simple utility node that extracts the first and last frame from a video
file or an image batch. Works with direct file paths or piped output from
other nodes (e.g. VideoHelperSuite).
"""

import os
import cv2
import torch
import numpy as np


class FirstFrameLastFrameExtractor:
    """
    Extracts the first and last frame from a video file or image batch.

    Inputs (both optional — connect whichever you have):
      - video_path: A STRING file path to a video file (.mp4, .avi, .mkv, etc.)
      - images: An IMAGE batch tensor [B, H, W, C] from another node

    Outputs:
      - first_frame: IMAGE tensor [1, H, W, C]
      - last_frame:  IMAGE tensor [1, H, W, C]
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "video_path": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "tooltip": (
                        "Absolute path to a video file "
                        "(.mp4, .avi, .mkv, .mov, .webm, .gif)"
                    ),
                }),
                "images": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE", "IMAGE")
    RETURN_NAMES = ("first_frame", "last_frame")
    FUNCTION = "extract_frames"
    CATEGORY = "Video/Utils"
    DESCRIPTION = (
        "Extracts the first and last frame from a video file or image batch."
    )

    # ------------------------------------------------------------------
    # Main entry point
    # ------------------------------------------------------------------

    def extract_frames(self, video_path="", images=None):
        """
        Extract the first and last frames.

        Priority order:
          1. If an image batch is connected, pick frame [0] and frame [-1].
          2. Otherwise, open the file at *video_path* with OpenCV.
        """

        # --- Path A: image batch from another node ---
        if images is not None:
            first_frame = images[0].unsqueeze(0)   # [1, H, W, C]
            last_frame = images[-1].unsqueeze(0)    # [1, H, W, C]
            return (first_frame, last_frame)

        # --- Path B: read video file from disk ---
        if not video_path or not video_path.strip():
            raise ValueError(
                "No input provided. Connect an image batch (IMAGE) "
                "or enter a video file path."
            )

        video_path = video_path.strip()

        # Strip surrounding quotes that users sometimes paste
        if (
            (video_path.startswith('"') and video_path.endswith('"'))
            or (video_path.startswith("'") and video_path.endswith("'"))
        ):
            video_path = video_path[1:-1]

        if not os.path.isfile(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError(f"Could not open video file: {video_path}")

        try:
            first_cv2, last_cv2 = self._read_first_last(cap)
        finally:
            cap.release()

        first_frame = self._cv2_to_tensor(first_cv2)
        last_frame = self._cv2_to_tensor(last_cv2)

        return (first_frame, last_frame)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _read_first_last(cap):
        """
        Read the first and last frames from an open cv2.VideoCapture.

        Uses seeking first; falls back to sequential reading if the codec
        does not support seeking to the last frame.
        """
        # ---- First frame ----
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, first_frame = cap.read()
        if not ret or first_frame is None:
            raise RuntimeError(
                "Failed to read the first frame from the video."
            )

        # ---- Last frame ----
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        last_frame = None

        if total_frames > 0:
            # Try seeking directly to the last frame
            cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames - 1)
            ret, last_frame = cap.read()
            if not ret:
                last_frame = None

        # Fallback: read sequentially until the end
        if last_frame is None:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                last_frame = frame

        if last_frame is None:
            raise RuntimeError(
                "Failed to read the last frame from the video."
            )

        return first_frame, last_frame

    @staticmethod
    def _cv2_to_tensor(cv2_frame):
        """
        Convert an OpenCV BGR uint8 frame to a ComfyUI IMAGE tensor.

        Returns a torch.float32 tensor with shape [1, H, W, C], values in
        [0.0, 1.0], RGB channel order.
        """
        rgb = cv2.cvtColor(cv2_frame, cv2.COLOR_BGR2RGB)
        normalized = rgb.astype(np.float32) / 255.0
        tensor = torch.from_numpy(normalized).unsqueeze(0)  # [1, H, W, C]
        return tensor
