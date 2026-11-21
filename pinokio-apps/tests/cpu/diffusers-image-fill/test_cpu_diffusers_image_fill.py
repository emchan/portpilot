"""Auto-generated CPU port smoke test for diffusers-image-fill."""

from pathlib import Path


def test_cpu_port_recorded():
    """The per-app report must record a CPU port attempt and result."""
    repo_root = Path(__file__).resolve().parents[3]
    report = repo_root / "results" / "diffusers-image-fill.md"
    assert report.is_file(), f"Missing report: {report}"
    text = report.read_text(encoding="utf-8")
    assert "## CPU test run" in text, "Missing CPU test run section"
    assert "- Result:" in text, "Missing CPU test result"
