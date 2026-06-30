# 📹 Manim Presentation - Cybersecurity & CPS

## Overview

This folder contains Manim animation scripts for creating educational videos on **Cybersecurity and Cyber-Physical Systems (CPS)**. The animations are designed to be visually appealing, scientifically accurate, and suitable for educational purposes.

---

## 📋 Contents

- **scene.py** - Main Manim scene with animation sequences
- **main.py** - Entry point and configuration
- **pyproject.toml** - Project dependencies (Manim v0.20.1+)
- **CybersecurityAndCPS.mp4** - Rendered video output

---

## 🎬 Animation Sections

### 1. **Introduction** (0:00 - 0:30)
Sets the scene with dark slate background and introduces the topic.

### 2. **Cybersecurity Overview** (0:30 - 1:00)
- Definition of cybersecurity
- Key principles (CIA Triad)
- Common threats
- Visual: Security shield with threat indicators

### 3. **Cyber-Physical Systems** (1:00 - 1:30)
- What are CPS?
- Examples: autonomous vehicles, smart grids, medical devices
- Integration of digital and physical worlds

### 4. **Intersection: Security in CPS** (1:30 - 2:00)
- Why CPS security is critical
- Real-world implications
- Security challenges specific to CPS

### 5. **Conclusion** (2:00 - 2:15)
- Call to action
- Further learning resources

---

## 🛠️ Technical Details

### **Rendering Specifications**
- **Resolution:** 480p (854×480)
- **Frame Rate:** 15 fps
- **Quality:** Low (ql flag)
- **Format:** MP4
- **Duration:** ~2-3 minutes
- **File Size:** ~1.2 MB

### **Design System**
- **Background:** Dark slate (#0f172a)
- **Cyber Domain:** TEAL_A, TEAL_C
- **Physical Domain:** MAROON_A
- **Security:** GOLD_A
- **Supporting:** GRAY_B

### **Animation Timing**
- Voiceover-synchronized (2-3 second waits)
- Approximately 130-150 words per minute pacing
- Scene-based segmentation for easy synchronization

---

## 🚀 Quick Start

### **Prerequisites**
- Python 3.13+
- Manim Community v0.20.1+
- `uv` package manager

### **Installation**
```bash
# Clone repository
git clone https://github.com/MELAI-1/cyberphysical-systems.git
cd cyberphysical-systems/manim_animations/presentation

# Install dependencies
uv sync

# Or manually install
pip install manim>=0.20.1
```

### **Rendering the Animation**
```bash
# Low quality (fast rendering)
uv run manim -ql scene.py CybersecurityAndCPS

# Medium quality
uv run manim -qm scene.py CybersecurityAndCPS

# High quality
uv run manim -qh scene.py CybersecurityAndCPS

# Preview without rendering
uv run manim -p scene.py CybersecurityAndCPS
```

---

## 📝 Code Structure

### **scene.py**
```python
class CybersecurityAndCPS(MovingCameraScene):
    def construct(self):
        # Main animation orchestration
        self.play_intro()
        self.play_cybersecurity()
        self.play_cps()
        self.play_intersection()
        self.play_conclusion()
    
    def build_card(title, body, color, width, height):
        # Reusable card widget factory
        
    def play_intro(), play_cybersecurity(), etc.:
        # Individual section methods
```

### **Key Components**
- `MovingCameraScene` - Allows dynamic camera movement
- `build_card()` - Factory for consistent card styling
- `ShieldSection` - Custom security shield visualization
- `VGroup` - Grouping and layout management

---

## 🎨 Customization

### **Modify Colors**
Edit the color palette in `scene.py`:
```python
from manim import *
CUSTOM_TEAL = "#00CED1"
CUSTOM_GOLD = "#FFD700"
```

### **Adjust Timing**
Change `self.wait(X)` durations to match voiceover:
```python
self.play(Write(title))
self.wait(2)  # 2 seconds for voiceover
```

### **Add New Sections**
Create new methods following the pattern:
```python
def play_new_section(self):
    # Create objects
    # Animate
    # Wait for voiceover
    self.wait(duration)
```

---

## 🎬 Adding Voiceover

### **Method 1: Video Editor**
1. Export MP4 from Manim
2. Use FFmpeg or video editor to add audio
3. Sync audio with animations

### **Method 2: Combine in Python**
```bash
ffmpeg -i CybersecurityAndCPS.mp4 -i voiceover.mp3 \
    -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 \
    output_with_audio.mp4
```

### **Method 3: Automated in Manim**
Use Manim's `add_sound()` method for direct audio integration.

---

## 🐛 Troubleshooting

### **Rendering Errors**
- Ensure Manim v0.20.1 or compatible
- Check for unsupported parameters (like `justify=True`)
- Verify all imports are available

### **Slow Rendering**
- Use `-ql` (low quality) for development
- Reduce frame rate in config
- Render sections separately, then combine

### **Memory Issues**
- Lower resolution
- Render on machine with more RAM
- Break into smaller animations

---

## 📖 Resources

- [Manim Documentation](https://docs.manim.community/)
- [Manim Community GitHub](https://github.com/ManimCommunity/manim)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)
- [Video Production Best Practices](https://en.wikipedia.org/wiki/Video_production)

---

## 🎯 Next Steps

1. **Customize** - Modify colors, timing, content
2. **Add Voiceover** - Sync audio with animations
3. **Export** - Generate final MP4
4. **Publish** - Share on YouTube, Vimeo, etc.
5. **Expand** - Create additional CPS education videos

---

## 📋 Rendering Output

Generated files are stored in:
```
media/
├── videos/
│   └── scene/
│       └── 480p15/
│           └── CybersecurityAndCPS.mp4
├── images/
├── texts/
└── Tex/
```

---

## ✅ Quality Checklist

Before finalizing:
- [ ] All animations render without errors
- [ ] Timing matches voiceover (if added)
- [ ] Colors are consistent and professional
- [ ] No text overlap or visual glitches
- [ ] Video plays smoothly at target resolution
- [ ] Audio (if added) syncs properly
- [ ] File size is optimized

---

## 📞 Support

For Manim-specific issues, visit the official community.

For CPS content questions, refer to the main repository README.

---

## 🎓 Educational Use

These animations are designed for educational purposes. Feel free to modify, extend, and share them with proper attribution.

---

**Created:** 2026-06-30  
**Manim Version:** 0.20.1+  
**Status:** Production Ready ✓
