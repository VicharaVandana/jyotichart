# Changelog

All notable changes to this project will be documented in this file.

## [5.0.0] - 2026-07-05

### Added
- **Partial Charts**: You can now generate charts with missing planets (e.g., just Sun and Jupiter) by initializing charts with `IsFullChart=False`. The chart will cleanly render without throwing missing planet validation errors.
- **Toggling Aspects**: Added the ability to completely disable planetary aspect lines via `updatechartcfg(aspect=False)` for cleaner, less cluttered outputs (especially useful in Transit Charts).
- **Extensive API Reference**: Massively updated README with complete, copy-pastable code samples, generated visual examples, and a comprehensive method and class reference.

### Fixed
- **Critical Class Variable Leak**: Fixed a major bug where `planets` were stored as a shared class variable. Previously, generating a full natal chart would cause subsequent partial charts to inappropriately display all 9 planets. This state leak has been patched across `NorthChart`, `SouthChart`, `NorthTransitChart`, and `SouthTransitChart`.
- **Retrograde Rendering Cleanup**: Removed the parentheses `()` around retrograde planets to reduce visual noise. Retrograde planets are now exclusively indicated by an underline (e.g. `Ju` underlined).

### Changed
- **Transit Layout Updates**: North and South Indian Transit charts have been structurally refined for better label visibility and inner/outer orbit distinctions.
- **Center Box Text Optimization**: Overhauled the central text area for South Indian charts (and transit charts) to tightly fit Birth Details, Chart Name, and Transit Dates without overlapping the borders.

---

## [4.0.0] - Previous Release
- Initial stable release including base North/South natal and numerical charts.
