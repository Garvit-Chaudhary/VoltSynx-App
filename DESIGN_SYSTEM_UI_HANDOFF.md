# VoltSynx Mobile App — Design System & UI Handoff Specification
**Document Version:** 1.0.0  
**Source Codebase:** VoltSynx Web Engine (React 18 / Tailwind CSS v3.4.17 / Framer Motion / HTML5 Canvas)  
**Aesthetic Standard:** WorldQuant Foundry Replica // Industrial Mechanical Minimalist  
**Target Mobile Platforms:** iOS (SwiftUI / Metal) & Android (Jetpack Compose / Canvas / Vulkan)

---

## 1. Executive Summary & Aesthetic Philosophy

VoltSynx employs a strict **Industrial Mechanical Aesthetic** modeled directly on high-performance algorithmic engineering terminals (specifically following the WorldQuant Foundry design architecture). 

### Foundational Tenets for Mobile Developers:
1. **Zero Skewmorphism & Zero Heavy Drop Shadows:** Interfaces are flat, structured, and architectural. No multi-layer blurry drop shadows, no bubbly rounded buttons, and zero consumer-grade neon gradients (no generic purple/blue glow).
2. **Exposed Hairline Grid Architecture:** Surfaces, cards, and modal dialogs are separated by crisp, 1-physical-pixel exposed hairline borders (`rgba(231, 231, 231, 0.12)` in dark mode; `#E5E5E5` in light mode).
3. **Dual-Tier Typography Pairing:** Bold, tight-tracked geometric display headings paired with high-tracking, monospaced technical telemetry counters.
4. **Deliberate Contrast Ratios:** Every card variant utilizes a carefully calibrated text-to-surface contrast system to maintain accessibility while preserving a mechanical, instrument-panel feel.

---

## 2. Color System & Exact Hex Tokens

### 2.1 Core Canvas & Surface Tokens

| Token Name | Hex Code / RGBA | Role & Application | Contrast Rule |
| :--- | :--- | :--- | :--- |
| **Canvas Dark** | `#111111` | Primary background base for Dark Mode. Deep Matte Obsidian Charcoal. | **NEVER** use pure `#000000` or generic navy/blue. |
| **Canvas Light** | `#FDFBF7` | Primary background base for Light Mode. Warm Ivory Off-White. | **NEVER** use harsh sterile `#FFFFFF` for page background. |
| **Surface Dark Elevated** | `#161616` | Elevated cards, hardware tech badges, and modal drawers. | 1-step elevation above `#111111`. |
| **Surface Dark Hover/Active** | `#1C1C1C` | Active selector pill background, pressed card state, drawer list fills. | 2-step elevation above `#111111`. |
| **Surface Dark Recessed** | `#141414` | Drawer containers, receipt modules, telemetry strips. | Subtle depth contrast. |
| **Surface Light Sub-Nav** | `#F8F5EE` | Sticky headers, footer strips, light card recessed areas. | Warm stone tint. |
| **Surface Light Badge** | `#F5F2EA` | Hardware tech badges, inactive segmented controls. | 1-step depth below `#FDFBF7`. |
| **Surface Light Active** | `#F0ECE1` | Selected navigation items and active segmented tabs. | Pronounced tactile state. |

### 2.2 Typography & Foreground Hierarchy

| Token Name | Dark Mode Value | Light Mode Value | Application |
| :--- | :--- | :--- | :--- |
| **Primary Text / Headings** | `#E7E7E7` (Crisp Alabaster) | `#111111` (Matte Obsidian) | Screen titles, H1–H4 display headings, prominent values. |
| **Secondary / Technical Mono** | `#8E8E8E` (Technical Grey) | `#6B6B6B` / `neutral-600` | Monospaced tags, system telemetry, secondary descriptions. |
| **Muted Telemetry / Hairlines** | `#8E8E8E` at 40%–60% | `#111111` at 35%–50% | Inactive labels, table delimiters, sub-headers. |
| **Metallic Accent (Dark)** | `#D4C5B0` (Warm Metallic Sand) | — | Pulsing data nodes, active indicators, hardware tags. |
| **Metallic Accent (Light)** | — | `#936E3B` (Warm Bronze Amber) | High-contrast counterpart for gold/metallic accents on ivory. |

### 2.3 Architectural Hairline Borders

```css
/* Dark Mode Exposed Hairlines */
border-color: rgba(231, 231, 231, 0.12); /* Standard hairline */
border-color: rgba(231, 231, 231, 0.15); /* Slightly elevated hairline */

/* Light Mode Exposed Hairlines */
border-color: #E5E5E5;                   /* Standard hairline */
border-color: rgba(17, 17, 17, 0.12);    /* Container hairline */
```

### 2.4 The Exact 4-Color Workflow Card Palette

The workflow configuration matrix uses four distinct, high-impact surface fills. Each card maintains strict internal text contrast rules:

```
┌────────────────────────────────────────────────────────────────────────┐
│  CARD 01: STUDIO-GRADE BROADCAST ROUTING                                │
│  Surface Fill:     #111111 (Deep Matte Obsidian Charcoal)               │
│  Display Heading:  #E7E7E7 (Crisp Alabaster Off-White)                  │
│  Body Text:        #D4D4D4 (Neutral-300 / 85% Alabaster)                │
│  Index Counter:    #D4C5B0 (Warm Metallic Sand)                         │
│  Category Tag:     #D4C5B0 (Warm Metallic Sand)                         │
│  Internal Line:    rgba(231, 231, 231, 0.15)                            │
│  Vector Glyph:     #D4C5B0 / #E7E7E7                                    │
├────────────────────────────────────────────────────────────────────────┤
│  CARD 02: SUB-MILLISECOND TACTICAL SYNC                                │
│  Surface Fill:     #608C95 (Muted Industrial Teal)                      │
│  Display Heading:  #111111 (Obsidian Charcoal Contrast)                 │
│  Body Text:        rgba(17, 17, 17, 0.90)                               │
│  Index Counter:    rgba(17, 17, 17, 0.80)                               │
│  Category Tag:     rgba(17, 17, 17, 0.75)                               │
│  Internal Line:    rgba(17, 17, 17, 0.20)                               │
│  Vector Glyph:     #111111 (Obsidian Charcoal Contrast)                 │
├────────────────────────────────────────────────────────────────────────┤
│  CARD 03: SUSTAINED ENDURANCE SESSIONS                                 │
│  Surface Fill:     #E26D45 (Terracotta Burnt Orange)                    │
│  Display Heading:  #111111 (Obsidian Charcoal Contrast)                 │
│  Body Text:        rgba(17, 17, 17, 0.90)                               │
│  Index Counter:    rgba(17, 17, 17, 0.80)                               │
│  Category Tag:     rgba(17, 17, 17, 0.75)                               │
│  Internal Line:    rgba(17, 17, 17, 0.20)                               │
│  Vector Glyph:     #111111 (Obsidian Charcoal Contrast)                 │
├────────────────────────────────────────────────────────────────────────┤
│  CARD 04: UNIVERSAL ANDROID INTEGRATION                                │
│  Surface Fill:     #E8E6E1 (Warm Industrial Grey / Pale Stone)          │
│  Display Heading:  #111111 (Obsidian Charcoal Contrast)                 │
│  Body Text:        rgba(17, 17, 17, 0.90)                               │
│  Index Counter:    rgba(17, 17, 17, 0.80)                               │
│  Category Tag:     rgba(17, 17, 17, 0.75)                               │
│  Internal Line:    rgba(17, 17, 17, 0.20)                               │
│  Vector Glyph:     #111111 (Obsidian Charcoal Contrast)                 │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Typography Stack & Application Hierarchy

The design system is constructed around two contrasting font engines:
1. **Primary Geometric Sans-Serif:** `'Plus Jakarta Sans'` (Alternative/Fallback: `'Syne'`)
2. **Technical Telemetry Monospace:** `'JetBrains Mono'` (Fallback: `ui-monospace`)

### 3.1 Strict Font Application Matrix

```
┌──────────────────────────┬────────────────────────────┬─────────────────────────────┐
│ UI Element               │ Font Family & Weight       │ Styling & Tracking Rules    │
├──────────────────────────┼────────────────────────────┼─────────────────────────────┤
│ Massive Display Headings │ Plus Jakarta Sans (800/700)│ UPPERCASE                   │
│ (Hero, Section Banners)  │ (or Syne 700/800)          │ Tracking: -0.04em (TIGHT)   │
│                          │                            │ Line Height: 0.92 – 0.98    │
│                          │                            │ Block/Split-line stacking   │
├──────────────────────────┼────────────────────────────┼─────────────────────────────┤
│ Feature Card Headings    │ Plus Jakarta Sans (700)    │ UPPERCASE                   │
│                          │                            │ Tracking: -0.03em           │
│                          │                            │ Line Height: 1.04 – 1.08    │
├──────────────────────────┼────────────────────────────┼─────────────────────────────┤
│ Body Paragraphs & Notes  │ Plus Jakarta Sans (400)    │ Sentence case               │
│                          │                            │ Tracking: Normal            │
│                          │                            │ Line Height: 1.55 – 1.65    │
├──────────────────────────┼────────────────────────────┼─────────────────────────────┤
│ Technical Index Counters │ JetBrains Mono (600/700)   │ UPPERCASE                   │
│ (e.g., "01 / 04", "01")  │                            │ Tracking: +0.20em (EXPANDED)│
│                          │                            │ Size: 11pt – 13pt           │
├──────────────────────────┼────────────────────────────┼─────────────────────────────┤
│ Hardware Telemetry Chips │ JetBrains Mono (500/600)   │ UPPERCASE                   │
│ (e.g., "60 FPS // 4K")   │                            │ Tracking: +0.18em – +0.25em │
│                          │                            │ Size: 9pt – 11pt            │
├──────────────────────────┼────────────────────────────┼─────────────────────────────┤
│ Structural Grid Labels   │ JetBrains Mono (500)       │ UPPERCASE                   │
│ (e.g., "INDEX // 02")    │                            │ Tracking: +0.20em           │
│                          │                            │ Size: 10pt – 11pt           │
├──────────────────────────┼────────────────────────────┼─────────────────────────────┤
│ Interactive CTA Labels   │ JetBrains Mono (600)       │ UPPERCASE                   │
│ (Mechanical Buttons)     │                            │ Tracking: +0.20em           │
│                          │                            │ Dual-layer vertical slide   │
└──────────────────────────┴────────────────────────────┴─────────────────────────────┘
```

### 3.2 Typography Anti-Patterns (Strictly Prohibited)
- **NO Loose Tracking on Display Headings:** Never add positive letter-spacing to large headers. They must appear condensed, architectural, and tightly bound.
- **NO Sans-Serif on Telemetry/Data:** Never render data indicators, port badges, FPS counters, or index numbers in Plus Jakarta Sans. Always use JetBrains Mono.
- **NO Lowercase on Navigation or Buttons:** CTAs and navigation items are strictly UPPERCASE with monospaced letter spacing (`tracking-[0.2em]`).

---

## 4. Structural Rules & WorldQuant Layout Architecture

### 4.1 Feature Cards (`rounded-3xl` with Massive Internal Padding)

Unlike standard mobile cards with 12px padding and subtle shadows, VoltSynx feature cards prioritize spatial gravity:

```
┌────────────────────────────────────────────────────────┐
│ [TAG: STUDIO PIPELINE // OBS READY]            [GLYPH] │
│                                                        │
│ MASSIVE DISPLAY HEADING                                │
│ IN PLUS JAKARTA SANS BOLD                              │
│                                                        │
│                                                        │
│                                                        │
│ 01                                             DEPLOY →│
│ ────────────────────────────────────────────────────── │  ← 1px hairline
│ Explanatory body paragraph describing the hardware     │
│ kernel swapchain and zero-overhead performance.        │
└────────────────────────────────────────────────────────┘
```

#### Exact Component Parameters:
- **Corner Radius:** `rounded-3xl` (`28pt` / `32px` on mobile/tablet).
- **Internal Padding:** `p-10` to `p-12` (minimum `28pt` on small screens, `40pt` on tablets).
- **Height Constraints:** Minimum vertical frame `min-h-[420px]` to allow ample breathing room between the top title block and bottom telemetry.
- **Internal Hairline Divider:** `1px` solid line (`h-px my-3.5`) separating the index number from the descriptive body.
- **Elevation / Drop Shadows:** `shadow-sm` only. Zero blurry diffuse shadows. Border is either hairline `1px` or borderless with pure contrasting background color.

### 4.2 Floating Nav Pills & Blur Overlays

Floating elements (e.g., the top navigation pill appearing on scroll, floating status chips, quick actions) follow an encapsulated pill morphology:

- **Geometry:** `rounded-full` (`corner-radius: 9999px`).
- **Color & Opacity:** `#111111` with high-density backdrop blur (`backdrop-filter: blur(16px)` or `UIBlurEffectStyleSystemUltraThinMaterialDark`).
- **Dimensions & Insets:** Horizontal padding `px-8` (`24pt`–`32pt`), vertical padding `py-3` (`12pt`).
- **Floating Position:** Centered horizontally (`top-6 left-1/2 -translate-x-1/2`).
- **Z-Index Layering:** `z-index: 50`.
- **Integrated Elements:**
  - Micro Brand Wordmark: Plus Jakarta Sans 900, `text-xs`, uppercase.
  - Monospace Divider: `//` at 40% opacity (`#8E8E8E/40`).
  - Action Pill Button: Inner nested `rounded-full` button in high-contrast Alabaster (`bg-[#E7E7E7] text-[#111111] px-3 py-1`).

### 4.3 Borders vs. Open Architectural Space

```
┌──────────────────────────────────────────────────────────────────────────┐
│ ARCHITECTURAL BOUNDARY RULE                                              │
├──────────────────────────────────────────────────────────────────────────┤
│ 1. Structural Viewports: Divided by continuous 1px edge-to-edge         │
│    hairlines (rgba(231,231,231,0.12)). No rounded containers here.       │
│                                                                          │
│ 2. Telemetry Bars: Anchored full-width bars (36pt - 44pt height) with    │
│    border-b and border-t dividing the screen into instrument sectors.    │
│                                                                          │
│ 3. Hero & Immersion Stages: Completely borderless open space. The        │
│    content floats over the 3D kinetic particle canvas without artificial │
│    bounding boxes, allowing typography to command the viewport.          │
│                                                                          │
│ 4. Floating Modals / Bottom Sheets: Bordered with top/side 1px hairline │
│    against a dimmed blur backdrop (rgba(0,0,0,0.75) + blur 12px).        │
└──────────────────────────────────────────────────────────────────────────┘
```

### 4.4 Slide-Over / Bottom Sheet Architecture (Beta Drawer)
In the mobile app, the right slide-over drawer maps cleanly to a **Bottom Sheet / Modal Drawer**:
- **Background Fill:** `#141414` (Dark Recessed Obsidian).
- **Hairline Boundary:** Top border `1px solid rgba(231, 231, 231, 0.15)`.
- **Telemetry Header:** Sticky sub-bar showing `BETA ADMISSION // 01 / 01` with monospaced `ESC / CLOSE` control.
- **Selection Chips:** Sharp rectangular or lightly rounded (`rounded-sm`) bordered options with active state transitioning from `border-[#E7E7E7]/15` to solid Alabaster fill (`bg-[#E7E7E7] text-[#111111]`).
- **Receipt / Confirmation Box:** Monospaced data summary with row delimiters (`border-b border-[#E7E7E7]/10`).

---

## 5. Motion, Physics & Kinetic Visual Logic

### 5.1 Framer Motion Spring & Easing Parameters

All transitions in VoltSynx are calibrated to feel like **precision-machined hardware**:

#### 1. Mechanical Cubic-Bezier Curve (The WorldQuant Signature)
- **Curve Definition:** `cubic-bezier(0.76, 0.0, 0.24, 1.0)`
- **Duration:** `300ms` to `350ms`
- **Application:**
  - Drawer slide-in / slide-out (`transform: translateX / translateY`)
  - Dual-layer mechanical text sliding buttons
  - Cycling hero text carousel (`duration: 500ms`)

```swift
// Swift / SwiftUI Equivalent Timing Curve
let mechanicalCurve = Animation.timingCurve(0.76, 0.0, 0.24, 1.0, duration: 0.35)
```

```kotlin
// Jetpack Compose Equivalent
val mechanicalEasing = CubicBezierEasing(0.76f, 0.0f, 0.24f, 1.0f)
val mechanicalAnimation = tween<Float>(durationMillis = 350, easing = mechanicalEasing)
```

#### 2. Spring Physics (Floating Nav Pill)
- **Stiffness:** `300`
- **Damping:** `30`
- **Mass:** `1.0`
- **Application:** Entering from `y: -100, opacity: 0` to `y: 0, opacity: 1`. Provides a tight, damped mechanical snap without loose wobbling.

```swift
// SwiftUI Spring
let pillSpring = Animation.interpolatingSpring(mass: 1.0, stiffness: 300, damping: 30)
```

```kotlin
// Jetpack Compose Spring
val pillSpring = spring<Float>(
    dampingRatio = 30f / (2f * kotlin.math.sqrt(300f)), // Critical damping calculation
    stiffness = 300f
)
```

#### 3. Dual-Layer Mechanical Hover / Tap Micro-Interaction
Every action button encapsulates two vertical text layers inside an `overflow-hidden` container:
- **Resting State:** Layer 1 is visible at `translate-y: 0`. Layer 2 is resting hidden at `translate-y: 100%`.
- **Triggered State (Hover / Press):**
  - Layer 1 translates upward to `-translate-y-full` (`-100%`).
  - Layer 2 translates upward to `translate-y-0` (`0%`).
  - Both layers transition via `cubic-bezier(0.76, 0, 0.24, 1)` over `300ms`.

---

## 6. Native 3D Wavy Particle Background Engine

The website's signature visual element is a **real-time 3D compound harmonic particle wave** running at 60 FPS. Mobile developers should implement this natively using **Metal / SwiftUI Canvas** (iOS) or **Jetpack Compose Canvas / RenderNode / Vulkan** (Android).

### 6.1 Grid Topology & 3D World Dimensions
- **Column Count ($N_x$):** `64` columns across width.
- **Row Count ($N_z$):** `52` rows into the screen depth.
- **Total Particles ($N$):** $64 \times 52 = 3,328$ points.
- **World Coordinate Bounds:**
  - $\text{Span}_X = \text{Viewport Width} \times 1.55$ (extends off-screen to avoid edge artifacts).
  - $X_{\text{start}} = -\text{Span}_X / 2$, $\Delta X = \text{Span}_X / (N_x - 1)$.
  - Depth starts at $Z_{\text{start}} = 120.0$, $\Delta Z = 28.0$.
  - Depth extends from $Z = 120.0$ to $Z \approx 1,548.0$.

### 6.2 Compound Sine Wave Formula
For any grid particle at world coordinate $(x, z)$ at time $t$ (incremented by $\Delta t = 0.016$ per frame):

$$y(x, z, t) = \text{swell}_1 + \text{swell}_2 + \text{swell}_3$$

Where:
$$\text{swell}_1 = \sin(x \cdot 0.0035 + t \cdot 0.85) \cdot \cos(z \cdot 0.0040 + t \cdot 0.70) \cdot 48.0$$
$$\text{swell}_2 = \sin((x + z) \cdot 0.0025 - t \cdot 0.55) \cdot 22.0$$
$$\text{swell}_3 = \cos(x \cdot 0.0070 + t \cdot 1.10) \cdot 8.0$$

### 6.3 Perspective Camera Projection
- **Camera Focal Length ($\text{FOV}$):** `340.0`
- **Camera Elevation ($\text{Elev}$):** `150.0` (looking down at the plane)
- **Horizon Position:** $Y_{\text{horizon}} = \text{Viewport Height} \times 0.52$
- **Scale Factor:** $S = \text{FOV} / z$
- **Screen Projections:**
  $$X_{\text{screen}} = \frac{\text{Viewport Width}}{2} + (x \cdot S)$$
  $$Y_{\text{screen}} = Y_{\text{horizon}} + [(\text{Elev} + y) \cdot S]$$

### 6.4 Particle Radius & Intensity Scaling
- **Radius Function:**
  $$R = \text{clamp}(1.9 \cdot S, 0.7, 2.8) \text{ px}$$
- **Depth Factor:**
  $$\text{depthNorm} = \text{clamp}\left(\frac{z - 120}{52 \times 28}, 0.0, 1.0\right)$$
  $$\text{depthFactor} = 1.0 - (\text{depthNorm} \times 0.6)$$
- **Wave Crest Highlight:**
  $$\text{crestHighlight} = \frac{y + 60.0}{120.0} \quad (\text{normalized } 0 \to 1)$$
- **Particle Intensity:**
  $$I = \text{depthFactor} \times (0.65 + \text{crestHighlight} \times 0.35)$$

### 6.5 Draw Call Optimization: The 4-Bucket Alpha Pipeline
To achieve locked 60 FPS on mobile GPUs without per-particle state changes, bucket all 3,328 particles into 4 alpha bins before calling `draw`:

```
┌──────────┬──────────────────┬──────────────────────────┬──────────────────────────┐
│ Bucket   │ Intensity Range  │ Dark Mode Color / Alpha  │ Light Mode Color / Alpha │
├──────────┼──────────────────┼──────────────────────────┼──────────────────────────┤
│ Bucket 0 │ I < 0.45         │ rgba(231, 231, 231, 0.22)│ rgba(96, 140, 149, 0.32) │
│ Bucket 1 │ 0.45 <= I < 0.65 │ rgba(231, 231, 231, 0.40)│ rgba(96, 140, 149, 0.50) │
│ Bucket 2 │ 0.65 <= I < 0.82 │ rgba(231, 231, 231, 0.60)│ rgba(96, 140, 149, 0.72) │
│ Bucket 3 │ I >= 0.82        │ rgba(231, 231, 231, 0.85)│ rgba(96, 140, 149, 0.95) │
└──────────┴──────────────────┴──────────────────────────┴──────────────────────────┘
```

> **Performance Note:** Light Mode utilizes **Muted Teal (`#608C95`)** for particles to create high-contrast artistic clarity over the Warm Ivory (`#FDFBF7`) canvas.

---

## 7. Shimmer & Aurora Gradient Shaders

### 7.1 Animated Shiny Text (Hardware Badges)
Applied to technical badges like `SUB-MILLISECOND USB TRANSPORT // ZERO PACKET LOSS`:
- **Dark Mode Shimmer Gradient:**
  `linear-gradient(90deg, transparent 0%, #FFFFFF 50%, transparent 100%)`
- **Light Mode Shimmer Gradient:**
  `linear-gradient(90deg, transparent 0%, #111111 50%, transparent 100%)`
- **Animation Loop:** 5 seconds infinite ease-in-out moving background position from `-100px` to `calc(100% + 100px)`.

### 7.2 Aurora Text (Accent Display Words)
Applied to keywords like `Wired`, `Streaming`, and `Zero Capture Card`:
- **Dark Mode 5-Stop Gradient:**
  `linear-gradient(135deg, #E7E7E7 0%, #D4C5B0 25%, #FFFFFF 50%, #D4C5B0 75%, #E7E7E7 100%)`
  (Crisp Alabaster $\to$ Warm Metallic Sand $\to$ Pure White $\to$ Metallic Sand $\to$ Alabaster)
- **Light Mode 5-Stop Gradient:**
  `linear-gradient(135deg, #111111 0%, #936E3B 25%, #1A1A1A 50%, #936E3B 75%, #111111 100%)`
  (Matte Obsidian $\to$ Warm Bronze Amber $\to$ Dark Slate $\to$ Bronze Amber $\to$ Obsidian)
- **Animation Cycle:** 6 seconds infinite smooth translation of gradient background coordinate.

---

## 8. Mobile Implementation Blueprint: Quick Reference

### 8.1 iOS (SwiftUI) Design Tokens

```swift
import SwiftUI

public enum VoltSynxColors {
    // Backgrounds
    public static let canvasDark = Color(hex: "0x111111")
    public static let canvasLight = Color(hex: "0xFDFBF7")
    public static let surfaceDarkElevated = Color(hex: "0x161616")
    public static let surfaceDarkHover = Color(hex: "0x1C1C1C")
    public static let surfaceDarkRecessed = Color(hex: "0x141414")
    public static let surfaceLightElevated = Color(hex: "0xF8F5EE")
    
    // Text
    public static let textPrimaryDark = Color(hex: "0xE7E7E7")
    public static let textPrimaryLight = Color(hex: "0x111111")
    public static let textMuted = Color(hex: "0x8E8E8E")
    
    // Accents
    public static let metallicDark = Color(hex: "0xD4C5B0")
    public static let metallicLight = Color(hex: "0x936E3B")
    
    // Workflow Card Palette
    public static let cardCharcoal = Color(hex: "0x111111")
    public static let cardTeal = Color(hex: "0x608C95")
    public static let cardOrange = Color(hex: "0xE26D45")
    public static let cardGrey = Color(hex: "0xE8E6E1")
    
    // Hairlines
    public static let hairlineDark = Color(white: 0.906, opacity: 0.12)
    public static let hairlineLight = Color(white: 0.898)
}

public enum VoltSynxTypography {
    public static func display(size: CGFloat) -> Font {
        Font.custom("PlusJakartaSans-Bold", size: size)
    }
    public static func mono(size: CGFloat) -> Font {
        Font.custom("JetBrainsMono-Medium", size: size)
    }
}
```

### 8.2 Android (Jetpack Compose) Design Tokens

```kotlin
package com.voltsynx.designsystem

import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.Font
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight

object VoltSynxColors {
    val CanvasDark = Color(0xFF111111)
    val CanvasLight = Color(0xFFFDFBF7)
    val SurfaceDarkElevated = Color(0xFF161616)
    val SurfaceDarkHover = Color(0xFF1C1C1C)
    val SurfaceDarkRecessed = Color(0xFF141414)
    val SurfaceLightElevated = Color(0xFFF8F5EE)

    val TextPrimaryDark = Color(0xFFE7E7E7)
    val TextPrimaryLight = Color(0xFF111111)
    val TextMuted = Color(0xFF8E8E8E)

    val MetallicDark = Color(0xFFD4C5B0)
    val MetallicLight = Color(0xFF936E3B)

    // Workflow Card Palette
    val CardCharcoal = Color(0xFF111111)
    val CardTeal = Color(0xFF608C95)
    val CardOrange = Color(0xFFE26D45)
    val CardWarmGrey = Color(0xFFE8E6E1)

    val HairlineDark = Color(0x1FE7E7E7)
    val HairlineLight = Color(0xFFE5E5E5)
}

object VoltSynxTypography {
    val PlusJakartaSans = FontFamily(
        Font(R.font.plus_jakarta_sans_regular, FontWeight.Normal),
        Font(R.font.plus_jakarta_sans_bold, FontWeight.Bold),
        Font(R.font.plus_jakarta_sans_extrabold, FontWeight.ExtraBold)
    )
    val JetBrainsMono = FontFamily(
        Font(R.font.jetbrains_mono_regular, FontWeight.Normal),
        Font(R.font.jetbrains_mono_medium, FontWeight.Medium),
        Font(R.font.jetbrains_mono_bold, FontWeight.Bold)
    )
}
```

---

## 9. Developer Sign-Off Checklist
Before shipping any mobile screen or component, verify:
- [ ] Primary dark screen background is `#111111` (never `#000000`).
- [ ] Light screen background is `#FDFBF7` (never sterile `#FFFFFF`).
- [ ] All card and section dividers are `1px` hairlines (`rgba(231,231,231,0.12)` / `#E5E5E5`). Zero drop shadow halos.
- [ ] All index markers (`01`, `02 / 04`), badges, and CTAs use `JetBrains Mono` with uppercase tracking $\ge +0.18\text{em}$.
- [ ] All display headings use `Plus Jakarta Sans` or `Syne` with negative tracking ($-0.04\text{em}$).
- [ ] Workflow cards match the exact 4-color palette (`#111111`, `#608C95`, `#E26D45`, `#E8E6E1`) with `#111111` dark text contrast on Teal, Orange, and Grey.
- [ ] Modal drawer enters with `cubic-bezier(0.76, 0.0, 0.24, 1.0)` over `350ms`.
- [ ] 3D wave particle background renders with 4 alpha buckets at locked 60 FPS.
