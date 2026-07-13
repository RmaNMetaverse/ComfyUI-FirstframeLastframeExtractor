"""Smoke tests for FirstFrameLastFrameExtractor."""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

import torch
from nodes import FirstFrameLastFrameExtractor


def test_video_file():
    """Test extraction from a real video file."""
    node = FirstFrameLastFrameExtractor()
    video = r"C:\Users\Virtual-Pc\Desktop\Future Egypt Veo3.mp4"
    if not os.path.isfile(video):
        print("SKIP: test video not found")
        return

    first, last = node.extract_frames(video_path=video)
    assert first.dim() == 4, f"Expected 4D, got {first.dim()}D"
    assert last.dim() == 4, f"Expected 4D, got {last.dim()}D"
    assert first.shape[0] == 1
    assert first.shape[3] == 3
    assert first.dtype == torch.float32
    assert 0.0 <= first.min() and first.max() <= 1.0
    print(f"  Video file: first={list(first.shape)}, last={list(last.shape)}  OK")


def test_image_batch():
    """Test extraction from a fake image batch."""
    node = FirstFrameLastFrameExtractor()
    batch = torch.rand(10, 64, 64, 3)
    first, last = node.extract_frames(images=batch)
    assert torch.equal(first.squeeze(0), batch[0])
    assert torch.equal(last.squeeze(0), batch[-1])
    assert first.shape == torch.Size([1, 64, 64, 3])
    print(f"  Image batch: first={list(first.shape)}, last={list(last.shape)}  OK")


def test_single_frame_batch():
    """Edge case: batch with only one frame."""
    node = FirstFrameLastFrameExtractor()
    batch = torch.rand(1, 32, 32, 3)
    first, last = node.extract_frames(images=batch)
    assert torch.equal(first, last), "Single-frame: first and last must be identical"
    print("  Single-frame batch: OK")


def test_error_empty_input():
    """Should raise ValueError when nothing is provided."""
    node = FirstFrameLastFrameExtractor()
    try:
        node.extract_frames(video_path="", images=None)
        assert False, "Should have raised ValueError"
    except ValueError:
        print("  Empty input ValueError: OK")


def test_error_missing_file():
    """Should raise FileNotFoundError for non-existent path."""
    node = FirstFrameLastFrameExtractor()
    try:
        node.extract_frames(video_path="C:/nonexistent/fake.mp4")
        assert False, "Should have raised FileNotFoundError"
    except FileNotFoundError:
        print("  Missing file FileNotFoundError: OK")


def test_error_whitespace():
    """Should raise ValueError for whitespace-only path."""
    node = FirstFrameLastFrameExtractor()
    try:
        node.extract_frames(video_path="   ")
        assert False, "Should have raised ValueError"
    except ValueError:
        print("  Whitespace ValueError: OK")


def test_quoted_path():
    """Should strip surrounding quotes from path."""
    node = FirstFrameLastFrameExtractor()
    video = r"C:\Users\Virtual-Pc\Desktop\Future Egypt Veo3.mp4"
    if not os.path.isfile(video):
        print("  SKIP: test video not found")
        return

    first, last = node.extract_frames(video_path=f'"{video}"')
    assert first.dim() == 4
    print("  Quoted path stripping: OK")


if __name__ == "__main__":
    print("Running smoke tests...\n")
    tests = [
        test_video_file,
        test_image_batch,
        test_single_frame_batch,
        test_error_empty_input,
        test_error_missing_file,
        test_error_whitespace,
        test_quoted_path,
    ]
    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except Exception as e:
            print(f"  FAIL {t.__name__}: {e}")
            failed += 1

    print(f"\nResults: {passed} passed, {failed} failed")
    sys.exit(1 if failed else 0)
