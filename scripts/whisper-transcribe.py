#!/usr/bin/env python3
import argparse
import json
import os
import shutil
import sys

os.environ.setdefault("PATH", os.environ.get("PATH", "") + os.pathsep + "/data/.local/bin")

try:
    import imageio_ffmpeg
    from faster_whisper import WhisperModel
except Exception as e:
    print(f"Import error: {e}", file=sys.stderr)
    sys.exit(2)


def ensure_ffmpeg_on_path():
    if shutil.which("ffmpeg"):
        return
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    ffmpeg_dir = os.path.dirname(ffmpeg_exe)
    os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ.get("PATH", "")


def main():
    parser = argparse.ArgumentParser(description="Transcribe audio with faster-whisper")
    parser.add_argument("input", help="Path to audio/video file")
    parser.add_argument("--model", default="small", help="Whisper model size (tiny, base, small, medium, large-v3, etc.)")
    parser.add_argument("--language", default=None, help="Language code, e.g. es, en")
    parser.add_argument("--task", default="transcribe", choices=["transcribe", "translate"])
    parser.add_argument("--compute-type", default="int8", help="faster-whisper compute type")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    ensure_ffmpeg_on_path()

    model = WhisperModel(args.model, device="cpu", compute_type=args.compute_type)
    segments, info = model.transcribe(args.input, language=args.language, task=args.task, vad_filter=True)
    rows = []
    text_parts = []
    for seg in segments:
        item = {
            "start": round(seg.start, 2),
            "end": round(seg.end, 2),
            "text": seg.text.strip(),
        }
        rows.append(item)
        if item["text"]:
            text_parts.append(item["text"])

    if args.json:
        print(json.dumps({
            "language": info.language,
            "language_probability": info.language_probability,
            "duration": getattr(info, "duration", None),
            "text": " ".join(text_parts).strip(),
            "segments": rows,
        }, ensure_ascii=False, indent=2))
    else:
        for item in rows:
            print(f"[{item['start']:>7.2f} -> {item['end']:>7.2f}] {item['text']}")
        if text_parts:
            print("\nTEXT:\n" + " ".join(text_parts).strip())


if __name__ == "__main__":
    main()
