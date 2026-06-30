# 📹 Manim Animations - CPS Educational Videos

## Overview

This directory contains Manim animation projects for creating educational videos about Cyber-Physical Systems.

**Manim** is a Python library for programmatic animation production, perfect for creating clear, professional educational content.

---

## 📚 Subfolders

### **presentation/** 
Complete Manim animation about **Cybersecurity and Cyber-Physical Systems**
- Educational video on CPS fundamentals
- Security implications for connected systems
- Rendered MP4 output ready for distribution
- See [presentation/README.md](presentation/README.md) for details

---

## 🎯 Purpose

Educational animations for:
- Learning complex CPS concepts visually
- Teaching cybersecurity principles
- Creating engaging educational content
- Documenting technical workflows

---

## 🛠️ Technology Stack

- **Manim Community** v0.20.1+ - Animation framework
- **Python** 3.13+ - Programming language
- **FFmpeg** - Video processing
- **NumPy/SciPy** - Mathematical computation

---

## 📖 Getting Started

### **Installation**
```bash
# Using uv (recommended)
uv sync

# Or standard pip
pip install manim>=0.20.1
```

### **Basic Rendering**
```bash
# Navigate to project directory
cd presentation

# Render animation (low quality for speed)
uv run manim -ql scene.py CybersecurityAndCPS

# Output saved to: media/videos/scene/480p15/CybersecurityAndCPS.mp4
```

---

## 📁 File Organization

```
manim_animations/
├── presentation/
│   ├── README.md              # Presentation documentation
│   ├── scene.py               # Main animation scene
│   ├── main.py                # Entry point
│   ├── pyproject.toml         # Dependencies
│   └── CybersecurityAndCPS.mp4 # Rendered output
└── README.md (this file)
```

---

## 🚀 Creating New Animations

### **Project Structure**
```bash
mkdir -p my_project
cd my_project
cp ../presentation/pyproject.toml .
cp ../presentation/scene.py scene_template.py
```

### **Basic Scene Template**
```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # Create objects
        title = Text("My Title", font_size=60)
        
        # Animate
        self.play(Write(title))
        self.wait(2)
        
        # Fade out
        self.play(FadeOut(title))
```

### **Render**
```bash
manim -ql scene.py MyScene
```

---

## 🎨 Animation Best Practices

### **Design Principles**
1. **Clarity** - Make concepts immediately understandable
2. **Pacing** - Match educational rhythm (not too fast)
3. **Color** - Use consistent, professional palette
4. **Transitions** - Smooth, meaningful scene changes

### **Technical Tips**
- Use `Scene` for simple animations
- Use `MovingCameraScene` for dynamic views
- Group related objects with `VGroup`
- Pre-compute complex mathematics
- Test with low quality (-ql) before high quality

### **Performance**
- Low quality: ~5-10 min per minute of video
- Medium quality: ~20-40 min per minute of video
- High quality: ~1-2 hours per minute of video

---

## 📹 Video Format

### **Recommended Settings**
- **Resolution:** 1080p or 4K for final output
- **Frame Rate:** 60 fps for smooth motion
- **Format:** MP4 (H.264) for compatibility
- **Bitrate:** 5-10 Mbps for quality

### **Export Options**
```bash
# Low quality (development)
manim -ql scene.py MyScene

# High quality (distribution)
manim -qh scene.py MyScene

# 4K resolution
manim -ql --resolution 3840,2160 scene.py MyScene
```

---

## 🎬 Adding Audio

### **FFmpeg Method**
```bash
ffmpeg -i animation.mp4 -i voiceover.mp3 \
    -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 \
    final_with_audio.mp4
```

### **Subtitle Support**
```bash
ffmpeg -i final_with_audio.mp4 -vf subtitles=subs.srt \
    final_with_subtitles.mp4
```

---

## 📚 Learning Resources

### **Manim Official**
- [Manim Documentation](https://docs.manim.community/)
- [Community GitHub](https://github.com/ManimCommunity/manim)
- [Examples Gallery](https://docs.manim.community/en/stable/examples.html)

### **Tutorials**
- YouTube: "Manim Tutorial" series
- 3Blue1Brown Channel (original Manim creator)
- Manim Community Discord

### **Best Practices**
- Watch 3Blue1Brown videos for inspiration
- Study animation timing
- Learn mathematical visualization
- Practice with simple scenes first

---

## 🐛 Troubleshooting

### **Common Issues**

**Problem:** "Module not found"
```bash
# Solution: Install Manim
pip install manim
```

**Problem:** Slow rendering
```bash
# Solution: Use low quality for development
manim -ql scene.py MyScene
```

**Problem:** Memory errors
```bash
# Solution: Reduce resolution or break into smaller files
manim -ql --resolution 1280,720 scene.py MyScene
```

---

## 📋 Project Checklist

- [ ] Concept and storyboard planned
- [ ] Scene structure outlined
- [ ] Animation code written
- [ ] Low-quality test render successful
- [ ] High-quality final render
- [ ] Video edited (if needed)
- [ ] Audio/voiceover added
- [ ] Subtitles created
- [ ] Final review complete
- [ ] Published/distributed

---

## 🌟 Ideas for New Animations

- IoT device communication
- CPS attack scenarios
- Robot arm kinematics
- Autonomous vehicle sensors
- Smart grid energy flow
- Medical device interfaces
- Network protocols
- Machine learning concepts

---

## 📄 License & Attribution

These projects are for educational purposes. When publishing:
- Credit Manim Community
- Provide source code
- Include educational context
- Respect any used resources

---

## 🚀 Next Steps

1. **Explore** - Check out `presentation/` for complete example
2. **Experiment** - Create simple test animations
3. **Learn** - Study Manim documentation
4. **Create** - Build your own educational content
5. **Share** - Distribute and collaborate

---

## 📞 Support

- **Manim Issues:** GitHub Issues
- **Community Help:** Manim Discord
- **CPS Content:** Repository Issues

---

**Last Updated:** 2026-06-30  
**Manim Version:** 0.20.1+  
**Repository:** https://github.com/MELAI-1/cyberphysical-systems
