# Thelia Motion System

## Purpose

Thelia's interface motion is treated as a visual language, not as decoration. Motion should communicate presence, continuity, response, hierarchy, and material weight without becoming the subject of the page.

## Core principles

1. **Purpose before spectacle.** Motion should clarify state, hierarchy, continuity, or interaction. Decorative motion stays subordinate to content.
2. **Continuous response over binary switching.** Pointer-driven elements should respond as if they have inertia rather than snapping between on/off states.
3. **Acceleration and deceleration are part of the motion.** A change in position is not enough. The path should have a believable transfer of energy and a controlled settling phase.
4. **Use physics for direct manipulation.** Pointer-following windows use a spring-damper model with velocity. The pointer establishes a target; the rendered object follows it through force, velocity, damping, and position.
5. **Frame-rate independence.** Animation calculations use elapsed time (`requestAnimationFrame` timestamps), not a fixed per-frame increment. This keeps the motion character stable across 60 Hz, 120 Hz, 144 Hz, and higher-refresh displays.
6. **Small movement, strong perception.** Translation, rotation, and scale remain intentionally restrained. The effect should be felt before it is noticed as an effect.
7. **No abrupt release.** Leaving a window returns its target to rest while preserving its current velocity, allowing the object to settle naturally rather than switching off.
8. **Hierarchy in motion.** Arrival animation is slow and ceremonial; page reveals are calm; direct interaction is responsive but weighted; navigation feedback is lighter; ambient light is the quietest layer.
9. **Motion has a rhythm.** The intended sequence is: arrive → settle → respond → release → settle.
10. **Accessibility is part of the system.** `prefers-reduced-motion` disables non-essential movement.

## Interaction model

For a pointer-driven window:

`pointer position → target → spring force → velocity → damping → position → render`

This is deliberately different from a simple interpolation such as:

`position += (target - position) × smoothing`

Interpolation can look smooth while still feeling like a switch. The spring-damper model gives the object a sense of mass and lets acceleration, momentum, and settling become visible.

## Current window response

The current desktop window interaction uses a restrained spring response approximately equivalent to:

- stiffness: 24
- damping: 9
- mass: 1.3
- translation: approximately 4 px horizontal / 3 px vertical
- rotation: approximately 1.4° / 1.8°
- hover scale: approximately 1.006
- elapsed-time integration with a capped frame delta

These values are intentionally conservative. The goal is a calm, analog response rather than a bouncy toy effect.

## Motion hierarchy

### Arrival

The mark, name, line, and hero enter sequentially. The arrival is intentionally slower than ordinary UI interaction because it establishes Thelia's visual identity.

### Hero

Large typography enters with restrained displacement and a long deceleration. The horizontal rule is a compositional transition, not a loading indicator.

### Scroll reveals

Content enters only when it becomes relevant. Reveal motion is short enough to preserve reading flow and slow enough to avoid looking like a collection of independent popups.

### Windows

Cards, manifesto panels, record links, and the test panel share one interaction language. Pointer position influences their target transform; spring dynamics determine the actual movement.

### Micro-feedback

Borders, ambient light, underline expansion, and text color changes are lower-amplitude responses. They should support the physical movement rather than compete with it.

## Performance

Interactive movement is limited primarily to `transform` and opacity-related effects. The system avoids layout-dependent animation during the pointer loop. `requestAnimationFrame` is used for rendering, and its timestamp is used to make motion independent of display refresh rate.

## Accessibility

The motion system respects `prefers-reduced-motion: reduce`. Non-essential arrival, reveal, and pointer movement are disabled or reduced when the user has requested reduced motion.

## Design references

The system is informed by established motion guidance and practice, including Material Design motion principles, Google's motion design writing, Apple's Human Interface Guidelines for Motion, MDN animation and `requestAnimationFrame` guidance, W3C reduced-motion guidance, and physics-based spring systems used in contemporary interaction libraries.

The implementation is also informed by the broader interaction-design principle that microinteractions should provide feedback and continuity rather than exist merely for spectacle.

## Decision record

The previous pointer implementation used a frame-based interpolation. It produced visible movement but felt like a binary switch: pointer enters, object moves; pointer leaves, object returns. The system was therefore changed to a time-based spring-damper response with explicit velocity and damping.

The intent is not to make every animation slower. The intent is to make motion *continuous*, so that speed, direction, and settling communicate the relationship between the pointer and the object.
