from manim import *


class CybersecurityAndCPS(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#0f172a"
        self.play_intro()
        self.play_cybersecurity()
        self.play_cps()
        self.play_intersection()
        self.play_conclusion()

    def build_card(self, title, body, color, width=3.3, height=2.1):
        bg = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.16,
            stroke_width=2,
            stroke_color=color,
            fill_color="#111827",
            fill_opacity=0.95,
        )
        title_text = Text(title, font_size=22, weight=BOLD, color=color)
        body_text = Text(body, font_size=18, color=GRAY_B, line_spacing=1.08)
        content = VGroup(title_text, body_text).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        content.move_to(bg.get_center()).shift(UP * 0.05)
        return VGroup(bg, content)

    def play_intro(self):
        title = Text(
            "Cybersecurity\n&\nCyber-Physical Systems",
            font_size=44,
            weight=BOLD,
            color=TEAL_A,
            line_spacing=1.1,
        ).move_to(UP * 0.2)
        subtitle = Text(
            "How digital protection shapes the physical world",
            font_size=24,
            color=GRAY_B,
        ).next_to(title, DOWN, buff=0.6)

        ring = Circle(radius=2.4, stroke_color=GOLD_A, stroke_width=2.5, stroke_opacity=0.7)
        pulse = Circle(radius=1.2, stroke_color=TEAL_C, stroke_width=2, stroke_opacity=0.35)
        glow = Dot(color=GOLD_A).scale(0.7)
        hero = VGroup(ring, pulse, glow).move_to(DOWN * 0.6)

        self.play(FadeIn(hero, shift=DOWN), run_time=1.8)
        self.play(Write(title), FadeIn(subtitle, shift=UP), run_time=2.8)
        self.wait(14)
        self.play(FadeOut(hero), FadeOut(title), FadeOut(subtitle), run_time=1.6)

    def play_cybersecurity(self):
        heading = Text("What is Cybersecurity?", font_size=32, weight=BOLD, color=TEAL_A).to_edge(UP, buff=0.3)
        self.play(Write(heading), run_time=1.4)

        intro = Text(
            "Cybersecurity protects the digital systems that modern life depends on.",
            font_size=24,
            color=GRAY_B,
        ).move_to(DOWN * 2.2)
        self.play(FadeIn(intro, shift=UP), run_time=1.2)
        self.wait(8)

        cards = VGroup(
            self.build_card("Confidentiality", "Only authorized people can see sensitive information.", TEAL_C),
            self.build_card("Integrity", "Data remains accurate and unchanged by unauthorized actors.", GOLD_A),
            self.build_card("Availability", "Systems stay reachable and usable when needed.", MAROON_A),
        ).arrange(RIGHT, buff=0.35)
        cards.move_to(DOWN * 0.1)

        self.play(FadeOut(intro), FadeIn(cards, shift=UP), run_time=1.8)
        self.wait(12)

        shield = ShieldSection(color=GOLD_A)
        shield.move_to(ORIGIN)
        self.play(ReplacementTransform(cards, shield), run_time=2.0)
        self.wait(16)
        self.play(FadeOut(heading), FadeOut(shield), run_time=1.4)

    def play_cps(self):
        heading = Text("What are Cyber-Physical Systems?", font_size=32, weight=BOLD, color=GOLD_A).to_edge(UP, buff=0.3)
        self.play(Write(heading), run_time=1.2)

        cyber_box = RoundedRectangle(width=3.3, height=2.1, corner_radius=0.15, stroke_color=TEAL_C, fill_color="#1e293b", fill_opacity=0.95)
        cyber_label = Text("Cyber\nSoftware, networks, logic", font_size=20, color=TEAL_C, line_spacing=1.1).move_to(cyber_box.get_center())
        cyber_group = VGroup(cyber_box, cyber_label).shift(LEFT * 3.2)

        physical_box = RoundedRectangle(width=3.3, height=2.1, corner_radius=0.15, stroke_color=MAROON_A, fill_color="#1e293b", fill_opacity=0.95)
        physical_label = Text("Physical\nMachines, motors, roads", font_size=20, color=MAROON_A, line_spacing=1.1).move_to(physical_box.get_center())
        physical_group = VGroup(physical_box, physical_label).shift(RIGHT * 3.2)

        sensor_arrow = Arrow(cyber_group.get_right(), physical_group.get_left(), color=GRAY_B, buff=0.2, stroke_width=3)
        actuator_arrow = Arrow(physical_group.get_left(), cyber_group.get_right(), color=GRAY_B, buff=0.2, stroke_width=3)
        sensor_label = Text("Sensors monitor", font_size=16, color=GRAY_B).next_to(sensor_arrow, UP, buff=0.15)
        actuator_label = Text("Actuators respond", font_size=16, color=GRAY_B).next_to(actuator_arrow, DOWN, buff=0.15)

        loop_text = Text(
            "They form a feedback loop: observe, compute, act, and adjust.",
            font_size=22,
            color=GRAY_B,
        ).move_to(DOWN * 2.3)

        self.play(FadeIn(cyber_group), FadeIn(physical_group), run_time=1.6)
        self.play(GrowArrow(sensor_arrow), Write(sensor_label), run_time=1.2)
        self.play(GrowArrow(actuator_arrow), Write(actuator_label), run_time=1.2)
        self.play(FadeIn(loop_text, shift=UP), run_time=1.2)
        self.wait(16)

        examples = VGroup(
            Text("Smart grids", font_size=20, color=TEAL_C),
            Text("Autonomous cars", font_size=20, color=GOLD_A),
            Text("Medical devices", font_size=20, color=MAROON_A),
        ).arrange(RIGHT, buff=0.45)
        examples.move_to(DOWN * 0.1)
        self.play(TransformFromCopy(loop_text, examples), run_time=1.8)
        self.wait(14)
        self.play(FadeOut(heading), FadeOut(cyber_group), FadeOut(physical_group), FadeOut(sensor_arrow), FadeOut(actuator_arrow), FadeOut(sensor_label), FadeOut(actuator_label), FadeOut(loop_text), FadeOut(examples), run_time=1.4)

    def play_intersection(self):
        heading = Text("The Dangerous Intersection", font_size=32, weight=BOLD, color=MAROON_A).to_edge(UP, buff=0.3)
        self.play(Write(heading), run_time=1.2)

        plant = VGroup(
            Rectangle(width=2.4, height=1.6, stroke_color=GRAY_B, fill_color="#1e293b", fill_opacity=0.95),
            Text("Water plant", font_size=20, color=GRAY_B).move_to(ORIGIN),
            Line(LEFT * 1.2, RIGHT * 1.2, color=GRAY_B).shift(UP * 0.8),
            Line(LEFT * 1.2, RIGHT * 1.2, color=GRAY_B).shift(DOWN * 0.8),
        ).move_to(LEFT * 2.2)

        warning = Text("⚠", font_size=48, color=MAROON_A).move_to(ORIGIN)
        attack_label = Text("A hacked controller can change pressure, flow, or motion.", font_size=22, color=GRAY_B).move_to(RIGHT * 2.2)
        self.play(FadeIn(plant, shift=LEFT), FadeIn(warning, shift=UP), FadeIn(attack_label, shift=RIGHT), run_time=2.0)
        self.wait(12)

        stuxnet = Text("Stuxnet showed this in industrial centrifuges.", font_size=22, color=GOLD_A).move_to(DOWN * 1.8)
        self.play(Write(stuxnet), run_time=1.2)
        self.wait(14)

        final_warning = Text("When CPS is compromised, the real world can be harmed.", font_size=24, color=WHITE).move_to(DOWN * 2.7)
        self.play(Transform(stuxnet, final_warning), run_time=1.6)
        self.wait(14)
        self.play(FadeOut(heading), FadeOut(plant), FadeOut(warning), FadeOut(attack_label), FadeOut(stuxnet), run_time=1.4)

    def play_conclusion(self):
        heading = Text("The Future of Secure Systems", font_size=32, weight=BOLD, color=TEAL_A).to_edge(UP, buff=0.3)
        self.play(Write(heading), run_time=1.2)

        pillars = VGroup(
            Text("Secure by design", font_size=24, color=TEAL_C),
            Text("Resilient by default", font_size=24, color=GOLD_A),
            Text("Human-aware and transparent", font_size=24, color=MAROON_A),
        ).arrange(DOWN, buff=0.3)
        pillars.move_to(ORIGIN)
        self.play(FadeIn(pillars, shift=UP), run_time=1.8)
        self.wait(12)

        closing = Text(
            "Cybersecurity is no longer just about data.\nIt is about protecting people, infrastructure, and trust.",
            font_size=24,
            color=GRAY_B,
            line_spacing=1.2,
        ).move_to(DOWN * 1.8)
        self.play(Write(closing), run_time=2.0)
        self.wait(14)
        self.play(FadeOut(heading), FadeOut(pillars), FadeOut(closing), run_time=1.4)


class ShieldSection(VGroup):
    def __init__(self, color=GOLD_A, **kwargs):
        super().__init__(**kwargs)
        shield = Polygon(
            [-1.0, 1.0, 0],
            [1.0, 1.0, 0],
            [1.0, -0.45, 0],
            [0.0, -1.35, 0],
            [-1.0, -0.45, 0],
            color=color,
            stroke_width=3,
            fill_color="#111827",
            fill_opacity=0.95,
        ).scale(1.2)
        lock = Text("🔒", font_size=36, color=color).move_to(ORIGIN)
        label = Text("Security guards the digital world", font_size=22, color=GRAY_B).next_to(shield, DOWN, buff=0.4)
        self.add(shield, lock, label)