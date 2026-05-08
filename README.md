# Pixelle-Video

A fork of [AIDC-AI/Ovis](https://github.com/AIDC-AI/Pixelle-Video) focused on video understanding and generation with multimodal large language models.

## Overview

Pixelle-Video extends the Pixelle framework with dedicated video processing capabilities, enabling:

- **Video Understanding**: Analyze and describe video content frame-by-frame or holistically
- **Temporal Reasoning**: Understand sequences of events across video timelines
- **Multimodal Interaction**: Combine video, image, and text inputs for rich interactions
- **Efficient Inference**: Optimized pipeline for both short clips and longer video content

## Features

- 🎬 Support for multiple video formats (MP4, AVI, MOV, WebM)
- 🖼️ Frame extraction and visual token encoding
- 🧠 Integration with state-of-the-art vision-language models
- ⚡ Batch processing for efficient throughput
- 🐳 Docker and Dev Container support for reproducible environments

## Installation

### From PyPI

```bash
pip install pixelle-video
```

### From Source

```bash
git clone https://github.com/your-org/Pixelle-Video.git
cd Pixelle-Video
pip install -e ".[dev]"
```

### Using Docker

```bash
docker build -t pixelle-video .
docker run --gpus all -it pixelle-video
```

### Using Dev Container

Open in VS Code and select **Reopen in Container** when prompted.

## Quick Start

```python
from pixelle_video import VideoProcessor, PixelleVideoModel

# Load model
model = PixelleVideoModel.from_pretrained("pixelle-video-7b")

# Process a video
processor = VideoProcessor()
video_frames = processor.load_video("path/to/video.mp4", num_frames=16)

# Run inference
response = model.chat(
    video=video_frames,
    prompt="Describe what is happening in this video."
)
print(response)
```

## Documentation

Full documentation is available at [https://your-org.github.io/Pixelle-Video](https://your-org.github.io/Pixelle-Video).

## Requirements

- Python >= 3.10
- PyTorch >= 2.1.0
- CUDA 11.8+ (for GPU acceleration)
- 16GB+ VRAM recommended for 7B models

## Model Zoo

| Model | Parameters | Video Frames | VRAM |
|-------|-----------|--------------|------|
| pixelle-video-3b | 3B | Up to 32 | 8GB |
| pixelle-video-7b | 7B | Up to 64 | 16GB |
| pixelle-video-14b | 14B | Up to 64 | 32GB |

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) and submit pull requests to our repository.

1. Fork the repository
2. Create your feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 — see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Original [Pixelle](https://github.com/AIDC-AI/Ovis) project by AIDC-AI
- Built on top of the Hugging Face Transformers ecosystem
- Inspired by VideoLLaMA, Video-LLaVA, and related works

## Citation

If you use Pixelle-Video in your research, please cite:

```bibtex
@software{pixelle_video,
  title  = {Pixelle-Video: Multimodal Video Understanding with Large Language Models},
  year   = {2024},
  url    = {https://github.com/your-org/Pixelle-Video}
}
```
